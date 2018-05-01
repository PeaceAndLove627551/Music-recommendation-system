from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(n))

        layout = QHBoxLayout()

        for n in range(10):
            btn = QPushButton(str(n))
            btn.clicked().connect(lambda n=n: self.my_custom_fn(n))
            layout.addWidget(btn)

        widget = QWidget
        widget.setLayout(layout)

        self.setWindowTitle("Music Recommendation System")

        # label = QLabel("Music!!!")
        # label.setAlignment(Qt.AlignCenter)
        #
        # self.setCentralWidget(label)

    # def onWindowTitleChange(self, s):
    #     print(s)

    def my_custom_fn(self, a):
        print(a)


app = QApplication(sys.argv)

window = MainWindow()
# window.show()

app.exec_()

