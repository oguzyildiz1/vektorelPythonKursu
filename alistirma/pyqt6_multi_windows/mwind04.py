#temporary windows
from PyQt6.QtWidgets import *
import sys
from random import randint


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        self.label = QLabel("Another Window %d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.w = None
        self.button = QPushButton("Push for window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)


    def show_new_window(self, checked):
        if self.w is None:
            self.w = AnotherWindow() #self ile w değişkeni yok olmuyor.
            self.w.show()
        else:
            self.w.close()
            self.w = None



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()