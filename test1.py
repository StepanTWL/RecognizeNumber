from PyQt6 import QtCore
from PyQt6.QtGui import QImage
from PyQt6.QtWidgets import QFileDialog
from pyqt_drawer.drawer import Drawer


def init_image(self):
    # вставка изображение в поле редактирования
    fname, _ = QFileDialog.getOpenFileName(
        self, 'Выбрать картинку', '',
        'Картинка (*.jpg);;Все файлы (*)')

    if not fname:
        #        fname = 'images/123.jpg'
        self.image = QImage(QtCore.QSize(800, 600), QImage.Format_ARGB32)  # !!!
        self.image.fill(QtCore.Qt.GlobalColor.white)  # (QtCore.Qt.white) белый   # !!!
    else:
        self.image = QImage(fname)

    self.drawer = Drawer(self.image.width(), self.image.height())
    self.canvas_layout.addWidget(self.drawer, 1, 1, 1, 1)
    self.drawer.setImage(self.image)