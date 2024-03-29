from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def tiklama(self):
        alert = QMessageBox()
        alert.setText('Tıkladın!')
        alert.exec()

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()

        icerik.addWidget(QPushButton('Dene'))
        button1 = QPushButton('Tıkla')
        icerik.addWidget(button1)
        button1.clicked.connect(self.tiklama)

        icerik.addWidget(QLabel('Bilgi'))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)


aa = QApplication([])

pencere = AnaPencere()
pencere.show()
aa.exec()