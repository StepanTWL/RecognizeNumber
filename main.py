import sys

import qimage2ndarray
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPainter, QPen, QPixmap, QCursor, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from numpy import asarray

import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.datasets import mnist         # библиотека рукописных цифр
from sklearn.model_selection import train_test_split # разделение выборонов�

from ui_mainwindow import Ui_MainWindow

def number():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    x_train = x_train / 255
    x_test = x_test / 255


    plt.imshow(x_test[0], cmap=plt.cm.binary)
    plt.show()

    y_train_cat = keras.utils.to_categorical(y_train, 10)
    y_test_cat = keras.utils.to_categorical(y_test, 10)

    size_val = 10000
    x_val_split = x_train[:size_val]
    y_val_split = y_train_cat[:size_val]

    x_train_split = x_train[size_val:]
    y_train_split = y_train_cat[size_val:]

    model = keras.Sequential(
        [Flatten(input_shape=(28, 28, 1)), Dense(128, activation='relu'), Dense(10, activation='softmax')])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    x_train_split, x_val_split, y_train_split, y_val_split = train_test_split(x_train, y_train_cat, test_size=0.2)

    # model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2) # после каждых 32 изображений будут обновляться весовые коеф., 5 проходов, 80%/20% обучение/валидация (проверка что не идет переобучение выборки)
    model.fit(x_train, y_train_cat, batch_size=32, epochs=1, validation_data=(x_val_split, y_val_split))

    model.evaluate(x_test, y_test_cat)  # проверка на тестовой выборке

    n = 100
    x = np.expand_dims(x_test[n], axis=0)  # что бы из 2х мерной матрицы сделать 3х мерную
    res = model.predict(x)  # можно подавать только 3х мерную матрицу (несколько изображений)
    #plt.imshow(x_test[n], cmap=plt.cm.binary)
    #plt.show()

    pred = model.predict(x_test)
    pred = np.argmax(pred, axis=1)  # axis=1 во второй области списка (слой3)

    mask = pred != y_test
    x_false = x_test[mask]
    y_false = pred[mask]

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        color = QColor(240, 240, 240)
        self.image.fill(color)

        self.drawings = False
        self.brushSize = 7
        self.brushColor = Qt.GlobalColor.black
        self.lastPoint = QPoint()

        self.ui.pushButton_recognize.clicked.connect(self.recognize_picture)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.check_position():
            self.drawings = True
            self.lastPoint = event.position()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton and self.check_position():
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine))
            painter.drawLine(self.lastPoint, event.position())
            self.lastPoint = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton and self.check_position():
            self.drawings = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        if self.check_position():
            canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def check_position(self) -> bool:
        cursor_pos = QCursor.pos()
        window_pos = self.mapFromGlobal(cursor_pos)
        if self.ui.groupBox.x() < window_pos.x() < self.ui.groupBox.x() + self.ui.groupBox.width() and self.ui.groupBox.y() < window_pos.y() < self.ui.groupBox.y() + self.ui.groupBox.height():
            return True
        else:
            return False

    def save_picture(self):
        cropped_pixmap = self.image.copy(10, 193, 380, 380)
        cropped_pixmap.save('image.png')

    def recognize_picture(self):
        cropped_pixmap = self.image.copy(10, 193, 380, 380)
        cropped_pixmap = cropped_pixmap.scaled(28, 28)
        numpydata = qimage2ndarray.recarray_view(cropped_pixmap)
        #print(type(numpydata))
        number()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec())
