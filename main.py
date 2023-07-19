import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPainter, QPen, QPixmap, QCursor
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButtonStart.clicked.connect(self.start_worker)

        self.image = QImage(self.size(), QImage.Format.Format_RGB32)
        self.image.fill(Qt.GlobalColor.white)

        #self.ui.lbl.setPixmap(QPixmap(self.image))

        # Устанавливаем изображение в QLabel
        #self.ui.groupBox.setPixmap(QPixmap(self.image))

        #self.ui.verticalLayout_2.addWidget(self.ui.label_11)
        #self.ui.groupBox.setPixmap(QPixmap.fromImage(self.image))

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
        cursor_pos = QCursor.pos()
        window_pos = self.mapFromGlobal(cursor_pos)
        print("Cursor Position (Window):", window_pos.x(), window_pos.y())
        groupBox_pos = self.ui.groupBox.pos()
        print(groupBox_pos.x(), groupBox_pos.y())
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec())
