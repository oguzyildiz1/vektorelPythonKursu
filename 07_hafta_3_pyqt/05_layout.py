from PyQt6.QtWidgets import *

aa = QApplication([])

ww = QWidget()

icerik = QVBoxLayout()

icerik.addWidget(QPushButton('Tıkla'))
icerik.addWidget(QPushButton('Dene'))
icerik.addWidget(QLabel('Tıkla'))

ww.setLayout(icerik)

ww.show()

aa.exec()