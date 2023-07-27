import sys
import cv2

from PIL import Image
from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QImage, QPainter, QPen, QCursor, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow

import numpy as np
import qimage2ndarray
from tensorflow import keras

import number
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
		self.brushSize = 25
		self.brushColor = Qt.GlobalColor.black
		self.lastPoint = QPoint()
		
		self.ui.pushButton_recognize.clicked.connect(self.recognize_picture)
		self.ui.pushButton_clear.clicked.connect(self.clearDisplay)
		
		self.neural_network = number.NN_number()
		self.neural_network.predict()
	
	def mousePressEvent(self, event):
		if event.button() == Qt.MouseButton.LeftButton and self.check_position():
			self.drawings = True
			self.lastPoint = event.position()
	
	def mouseMoveEvent(self, event):
		if event.buttons() & Qt.MouseButton.LeftButton and self.check_position():
			painter = QPainter(self.image)
			painter.setPen(QPen(self.brushColor,
			                    self.brushSize,
			                    Qt.PenStyle.SolidLine,
			                    Qt.PenCapStyle.RoundCap,
			                    Qt.PenJoinStyle.RoundJoin))
			painter.drawLine(self.lastPoint, event.position())
			painter.end()
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
		if (self.ui.groupBox.x() + (self.brushSize + 1) // 2) < window_pos.x() < (self.ui.groupBox.x() + self.ui.groupBox.width() - (self.brushSize + 1) // 2) and \
			(self.ui.groupBox.y() + (self.brushSize + 1) // 2) < window_pos.y() < (self.ui.groupBox.y() + self.ui.groupBox.height() - (self.brushSize + 1) // 2):
			return True
		else:
			return False
	
	def replace_color(self, qimage, old_color, new_color):
		image_array = qimage2ndarray.rgb_view(qimage)
		mask = np.all(image_array == old_color, axis=-1)
		image_array[mask] = new_color
		new_qimage = qimage2ndarray.array2qimage(image_array)
		return new_qimage
	
	def recognize_picture(self):
		cropped_pixmap = self.image.copy(10, 193, 380, 380)
		cropped_pixmap = self.replace_color(cropped_pixmap, [240, 240, 240], [255, 255, 255])
		cropped_pixmap.save('image.png')
		img_path = 'image.png'
		
		img = keras.preprocessing.image.load_img(img_path)
		image = img.resize((28, 28), Image.BILINEAR)
		image.save('image.png')
		img = cv2.imread('image.png')
		image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		image = np.array(image)
		self.neural_network.recognize_picture(image)
	
	def clearDisplay(self):
		color = QColor(240, 240, 240)
		self.image.fill(color)
		self.update()
	
	def setProgressBars(self, arr):
		self.ui.progressBar_0.setValue(int(arr[0][0] * 100))
		self.ui.progressBar_1.setValue(int(arr[0][1] * 100))
		self.ui.progressBar_2.setValue(int(arr[0][2] * 100))
		self.ui.progressBar_3.setValue(int(arr[0][3] * 100))
		self.ui.progressBar_4.setValue(int(arr[0][4] * 100))
		self.ui.progressBar_5.setValue(int(arr[0][5] * 100))
		self.ui.progressBar_6.setValue(int(arr[0][6] * 100))
		self.ui.progressBar_7.setValue(int(arr[0][7] * 100))
		self.ui.progressBar_8.setValue(int(arr[0][8] * 100))
		self.ui.progressBar_9.setValue(int(arr[0][9] * 100))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	main = Window()
	main.show()
	sys.exit(app.exec())
