from PyQt6.QtWidgets import *

aa = QApplication([])

def tiklama():
    alert = QMessageBox()
    alert.setText('Tıkladın')
    alert.exec()

pencere = QWidget()
pencere.setFixedSize(200,100)
pencere.show()

icerik = QVBoxLayout()
icerik.addWidget(QPushButton('Dene'))
button1 = QPushButton('Tıkla')
icerik.addWidget(button1)
button1.clicked.connect(tiklama)
icerik.addWidget(QLabel('Bilgi'))

pencere.setLayout(icerik)
aa.exec()

# tiklama()


