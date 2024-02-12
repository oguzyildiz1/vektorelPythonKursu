import sys
from PyQt6.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Q Grid example")
        layout = QGridLayout()

        layout.addWidget(QPushButton("Button at 0, 0"), 0, 0)
        layout.addWidget(QPushButton("Button at 0, 0"), 1, 0)
        layout.addWidget(QPushButton("Button at 0, 0"), 2, 0)
        layout.addWidget(QPushButton("Button at 0, 0"), 0, 1)
        layout.addWidget(QPushButton("Button at 0, 0"), 1, 1, 1, 2)
        layout.addWidget(QPushButton("Button at 0, 0"), 2, 1)
        layout.addWidget(QCheckBox("Chekcbox 1"), 3, 0)
        layout.addWidget(QCheckBox("Chekcbox 1"), 3, 1)
        layout.addWidget(QCheckBox("Chekcbox 1"), 3, 2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
