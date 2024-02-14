from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Uygulama(QMainWindow):
    def __init__(self):
        super(Uygulama, self).__init__()

        self.setWindowTitle("My App")
        widget = QLabel("Hello")
        widget.setText("Merhaba")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
        widget.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(widget)

app = QApplication([])

anapencere = Uygulama()

anapencere.show()

app.exec()

