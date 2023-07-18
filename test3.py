import sys
from PyQt5.Qt import *
from PyQt5 import QtGui, QtCore, QtWidgets, uic


class Canvas(QWidget):
	def __init__(self):
		super(Canvas, self).__init__()
		self.setFixedSize(600, 600)

		self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
		self.image.fill(QtCore.Qt.white)
		self.imageDraw = QtGui.QImage(self.size(), QtGui.QImage.Format_ARGB32)
		self.imageDraw.fill(QtCore.Qt.transparent)

		self.drawing = False
		self.brushSize = 10
		self._clear_size = 20
		self.brushColor = QtGui.QColor(QtCore.Qt.blue)
		self.lastPoint = QtCore.QPoint()
		self.change = False

	def mousePressEvent(self, event):
		if event.button() == QtCore.Qt.LeftButton:
			self.drawing = True
			self.lastPoint = event.pos()

	def mouseMoveEvent(self, event):
		if event.buttons() and QtCore.Qt.LeftButton and self.drawing:
			painter = QtGui.QPainter(self.imageDraw)
			painter.setPen(QtGui.QPen(
				self.brushColor,
				self.brushSize,
				QtCore.Qt.SolidLine,
				QtCore.Qt.RoundCap,
				QtCore.Qt.RoundJoin
			))
			if self.change:
				r = QtCore.QRect(QtCore.QPoint(), self._clear_size * QtCore.QSize())
				r.moveCenter(event.pos())
				painter.save()
				painter.setCompositionMode(QtGui.QPainter.CompositionMode_Clear)  # 1!!
				painter.eraseRect(r)  # 1!!
				painter.restore()
			else:
				painter.drawLine(self.lastPoint, event.pos())
			painter.end()
			self.lastPoint = event.pos()
			self.update()

	def mouseReleaseEvent(self, event):
		if event.button == QtCore.Qt.LeftButton:
			self.drawing = False

	def paintEvent(self, event):
		canvasPainter = QtGui.QPainter(self)
		canvasPainter.drawImage(self.rect(), self.image, self.image.rect())
		canvasPainter.drawImage(self.rect(), self.imageDraw, self.imageDraw.rect())

	def erase(self):
		self.change = not self.change
		if self.change:
			pixmap = QtGui.QPixmap(QtCore.QSize(1, 1) * self._clear_size)
			pixmap.fill(QtCore.Qt.transparent)
			painter = QtGui.QPainter(pixmap)
			painter.setPen(QtGui.QPen(QtCore.Qt.black, 2))
			painter.drawRect(pixmap.rect())
			painter.end()
			cursor = QtGui.QCursor(pixmap)
			QtWidgets.QApplication.setOverrideCursor(cursor)
		else:
			QtWidgets.QApplication.restoreOverrideCursor()


class Window(QMainWindow):
	def __init__(self):
		super(Window, self).__init__()

		uic.loadUi('window.ui', self)  # подключения дизайна

		self.setFixedSize(870, 639)
		self.setWindowTitle("Graphic designer v3.0")

		self.canvas = Canvas()
		self.setCentralWidget(self.canvas)  # главный виджет делаем Canvas

		self.action_eraser.triggered.connect(self.canvas.erase)  # !!!


if __name__ == '__main__':
	app = QApplication(sys.argv)
	wnd = Window()
	wnd.show()
	print(wnd.size())
	sys.exit(app.exec_())