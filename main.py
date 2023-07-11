
import sys

from PyQt6 import QtCore, QtWidgets, QtGui



from ui_mainwindow import Ui_MainWindow




class MiniPdkWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButtonStart.clicked.connect(self.start_worker)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MiniPdkWindow()
    main.show()
    sys.exit(app.exec())
