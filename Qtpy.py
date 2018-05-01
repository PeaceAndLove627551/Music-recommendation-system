import sys
from PyQt5 import (QtWidgets, QtCore)

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(480, 320)
widget.setWindowTitle("music_recommendation")
widget.show()
sys.exit(app.exec())
