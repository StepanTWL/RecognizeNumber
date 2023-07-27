from PyQt6.QtCore import Qt
import sys
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication
from PyQt6.QtGui import QPixmap, QImage


class Example(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		hbox = QHBoxLayout(self)

		image = QImage(100, 100, QImage.Format.Format_RGB32)
		image.fill(Qt.GlobalColor.white)
		pixmap = QPixmap(image)

		lbl = QLabel(self)
		lbl.setPixmap(pixmap)

		hbox.addWidget(lbl)
		#self.setLayout(hbox)

		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec())
