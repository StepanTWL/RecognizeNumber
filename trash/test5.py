from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGroupBox, QLabel

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GroupBox Location")
        layout = QVBoxLayout()

        group_box = QGroupBox("My GroupBox")
        layout.addWidget(group_box)

        label = QLabel("Hello, World!")
        group_box.setLayout(QVBoxLayout())
        group_box.layout().addWidget(label)

        self.setLayout(layout)

        self.printGroupBoxLocation(group_box)

    def printGroupBoxLocation(self, group_box):
        group_box_pos = group_box.pos()
        print("GroupBox Location (x, y):", group_box_pos.x(), group_box_pos.y())

    def sizeHint(self):
        return QSize(400, 300)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
