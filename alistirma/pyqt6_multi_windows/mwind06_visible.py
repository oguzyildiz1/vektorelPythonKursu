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
        self.w = AnotherWindow()
        self.button = QPushButton("Push for window")
        self.button.clicked.connect(self.toggle_window)
        self.setCentralWidget(self.button)


    def show_new_window(self, checked):
        self.w.show()

    #----- pencereyi gösterip saklamak için
    def toggle_window(self, checked):
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()