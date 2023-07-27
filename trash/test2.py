import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore, QtWidgets, QtMultimedia
import pygame as pg
import pygame
pygame.init()
pg.init()


class Text_class:
    def __init__(self, x, y, text, color1, color2):
        self.t = 'text'
        self.x = x
        self.y = y
        self.text = text
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color1)
        painter.setFont(QFont('Helvetica', 48))
        painter.drawText(self.x, self.y, self.text)


class BrushPoint:
    def __init__(self, x, y, color1, color2):
        self.t = 'brush'
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color1)
        painter.drawEllipse(self.x - 5, self.y - 5, 9, 9)


class Line:
    def __init__(self, sx, sy, ex, ey, color1, color2):
        self.t = 'line'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        painter.drawLine(self.sx, self.sy, self.ex, self.ey)


class Circle:
    def __init__(self, cx, cy, x, y, color1, color2):
        self.t = 'circle'
        self.cx = cx
        self.cy = cy
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        radius = int(((self.cx - self.x) ** 2 + (self.cy - self.y) ** 2) ** 0.5)
        painter.drawEllipse(self.cx - radius, self.cy - radius, radius * 2, radius * 2)


class Rectangle:
    def __init__(self, sx, sy, ex, ey, color1, color2):
        self.t = 'rect'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        painter.drawRect(self.sx, self.sy, self.ex - self.sx, self.ey - self.sy)


class RoundedRect:
    def __init__(self, sx, sy, ex, ey, color1, color2):
        self.t = 'rounders'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        painter.drawRoundedRect(self.sx, self.sy, self.ex - self.sx, self.ey - self.sy, 30.0, 15.0)


class Oval:
    def __init__(self, sx, sy, ex, ey, color1, color2):
        self.t = 'oval'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        painter.drawRoundedRect(self.sx, self.sy, self.ex - self.sx, self.ey - self.sy, 360.0, 360.0)


class Arc:
    def __init__(self, sx, sy, ex, ey, color1, color2):
        self.t = 'arc'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        painter.drawArc(self.sx, self.sy, self.ex - self.sx, (self.ey - self.sy) * 4, 30 * 16, 120 * 16)


class Chord:
    def __init__(self, sx, sy, ex, ey, color1, color2):
        self.t = 'chord'
        self.sx = sx
        self.sy = sy
        self.ex = ex
        self.ey = ey
        self.color1 = color1
        self.color2 = color2

    def draw(self, painter):
        painter.setBrush(QBrush(self.color1))
        painter.setPen(self.color2)
        painter.drawChord(self.sx, self.sy, (self.ex - self.sx), int((self.ey - self.sy) * 4), 30 * 16, 120 * 16)


class Canvas(QWidget):
    def __init__(self):
        super(Canvas, self).__init__()

        self.objects = []  # это массив где находятся все фигуры чтоб не пропали после рисования
        self.instrument = 'brush'  # по умолчанию кисточка
        self.color1 = QColor(255, 0, 255)
        self.color2 = QColor(255, 0, 255)
        # self.mus = pg.mixer.Sound('mus.mp3')

    def paintEvent(self, event):  # основной процесс отрисовки и отображения
        painter = QPainter()
        painter.begin(self)
        for obj in self.objects:
            obj.draw(painter)
        painter.end()

    def mousePressEvent(self, event):  # тут происходит чтение данных с помощью курсора мыши
        if self.instrument == 'brush':
            self.objects.append(BrushPoint(event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'line':
            self.objects.append(Line(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'circle':
            self.objects.append(Circle(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'rect':
            self.objects.append(Rectangle(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'rounders':
            self.objects.append(RoundedRect(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'oval':
            self.objects.append(Oval(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'arc':
            self.objects.append(Arc(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'chord':
            self.objects.append(Chord(event.x(), event.y(), event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'text':
            self.objects.append(Text_class(event.x(), event.y(), '/', self.color1, self.color2))
            self.update()
        elif self.instrument == 'eraser':
            x = event.x()
            y = event.y()

            for i in self.objects:
                if i.t == 'circle':
                    radius = int(((i.cx - i.x) ** 2 + (i.cy - i.y) ** 2) ** 0.5)
                    if i.cx - radius * 2 < x and x < i.cx and i.cy - radius * 2 < y and y < i.cy:
                        self.objects.remove(i)
                        self.update()
                        break

                elif i.t == 'brush' or i.t == 'text':
                    if i.x - 5 < x and x < i.x + 5 and i.y - 5 < y and y < i.y + 5:
                        self.objects.remove(i)
                        self.update()
                        break

                elif i.sx < x and x < i.ex and i.sy < y and y < i.ey:
                    self.objects.remove(i)
                    self.update()
                    break

    def mouseMoveEvent(self, event):  # тут так же но эта выполняет функции при движении
        if self.instrument == 'brush':
            self.objects.append(BrushPoint(event.x(), event.y(), self.color1, self.color2))
            self.update()
        elif self.instrument == 'line':
            self.objects[-1].ex = event.x()  # чтоб продолжить обращаемся к последнему месту нахождения мыши
            self.objects[-1].ey = event.y()
            self.update()
        elif self.instrument == 'circle':
            self.objects[-1].x = event.x()
            self.objects[-1].y = event.y()
            self.update()
        elif self.instrument == 'rect':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
            self.update()
        elif self.instrument == 'rounders':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
            self.update()
        elif self.instrument == 'oval':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
            self.update()
        elif self.instrument == 'arc':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
            self.update()
        elif self.instrument == 'chord':
            self.objects[-1].ex = event.x()
            self.objects[-1].ey = event.y()
            self.update()
    # тут просто меняем инструменты по нажатию кнопок

    def setEraser(self):
        self.instrument = 'eraser'

    def setText(self):
        self.instrument = 'text'

    def setBrush(self):
        self.instrument = 'brush'

    def setLine(self):
        self.instrument = 'line'

    def setCircle(self):
        self.instrument = 'circle'

    def setRect(self):
        self.instrument = 'rect'

    def setRoundedRect(self):
        self.instrument = 'rounders'

    def setOval(self):
        self.instrument = 'oval'

    def setArc(self):
        self.instrument = 'arc'

    def setChord(self):
        self.instrument = 'chord'

    def setColIn(self):
        self.color1 = QColorDialog.getColor()

    def setCol2(self):
        self.color2 = QColorDialog.getColor()

    # def Music_on(self):
        # self.mus.play()

    # def Music_off(self):
        # self.mus.stop()

    def setClear(self):
        self.objects.clear()
        self.update()


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        uic.loadUi('window.ui', self)  # подключения дизайна

        self.setWindowTitle("Graphic designer v3.0")
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)  # главный виджет делаем Canvas
        self.capsLck = False

        # self.setWindowIcon(QIcon('image.png'))

        self.action_eraser.triggered.connect(self.centralWidget().setEraser)
        self.action_text.triggered.connect(self.centralWidget().setText)
        self.action_brush.triggered.connect(self.centralWidget().setBrush)
        self.action_line.triggered.connect(self.centralWidget().setLine)
        self.action_circle.triggered.connect(self.centralWidget().setCircle)
        self.action_rect.triggered.connect(self.centralWidget().setRect)
        self.action_rectangle.triggered.connect(self.centralWidget().setRoundedRect)
        self.action_oval.triggered.connect(self.centralWidget().setOval)
        self.action_arc.triggered.connect(self.centralWidget().setArc)
        self.action_chord.triggered.connect(self.centralWidget().setChord)
        self.action_color_inside.triggered.connect(self.centralWidget().setColIn)
        self.action__color_outside.triggered.connect(self.centralWidget().setCol2)
        # self.action_music_on.triggered.connect(self.centralWidget().Music_on)
        # self.action_music_off.triggered.connect(self.centralWidget().Music_off)
        self.action_clear.triggered.connect(self.centralWidget().setClear)

    def keyPressEvent(self, e):
        if self.canvas.objects[-1].tür == "text":
            i = e.key()
            letter = ''
            if i == 32:
                letter = ' '
            if 1040 <= i and i <= 1105:
                if self.capsLck:
                    letter = chr(i)
                else:
                    letter = chr(i + 32)
            if letter != '':
                self.canvas.objects[-1].text += letter
                self.canvas.update()
            if e.key() == QtCore.Qt.Key_Backspace:
                if len(self.canvas.objects[-1].text) == 1:
                    self.canvas.objects.remove(self.canvas.objects[-1])
                    self.canvas.update()
                else:
                    self.canvas.objects[-1].text = self.canvas.objects[-1].text[:-1]
                    self.canvas.update()
            if e.key() == QtCore.Qt.Key_CapsLock:
                if self.capsLck:
                    self.capsLck = False
                else:
                    self.capsLck = True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())