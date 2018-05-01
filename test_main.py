import sys
import pdb
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import gui
import test6


class TestWnd(QMainWindow, gui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(TestWnd, self).__init__(parent)
        wnd = self.setupUi(self)


def mywindow():
    mywindow = TestWnd()
    mywindow.show()
    return mywindow
app = QApplication(sys.argv)
myobj = mywindow()
test6.music_recommend("smile", 10)

sys.exit(app.exec_())




