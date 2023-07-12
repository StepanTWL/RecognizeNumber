import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPainter, QPen, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButtonStart.clicked.connect(self.start_worker)

        #self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        #self.image.fill(Qt.GlobalColor.white)

        #self.ui.label_11.setPixmap(QPixmap(self.image))

        self.image = QImage(self.ui.label_11.size().width(), self.ui.label_11.size().height(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)

        # Устанавливаем изображение в QLabel
        #self.ui.label_11.setPixmap(QPixmap.fromImage(self.image))

        self.drawings = False
        self.brushSize = 7
        self.brushColor = Qt.GlobalColor.black
        self.lastPoint = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawings = True
            self.lastPoint = event.position()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.PenStyle.SolidLine))
            painter.drawLine(self.lastPoint, event.position())
            self.lastPoint = event.position()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.drawings = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec())
