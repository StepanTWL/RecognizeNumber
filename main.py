import sys

from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPainter, QPen, QPixmap, QCursor, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow

from ui_mainwindow import Ui_MainWindow


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

        self.ui.pushButton_save.clicked.connect(self.save_picture)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec())
