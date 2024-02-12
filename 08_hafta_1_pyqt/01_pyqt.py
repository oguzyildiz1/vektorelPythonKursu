from PyQt6.QtWidgets import *

class CeviriPenceresi(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Çeviri")

        icerik = QVBoxLayout()

        icerik.addWidget(QLabel("Çevrilecek: "))
        icerik.addWidget(QComboBox())
        icerik.addWidget(QDial())
        icerik.addWidget(QLineEdit())
        icerik.addWidget(QPushButton("Çevir"))
        icerik.addWidget(QLabel("Sonuc: "))

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

uygulama = QApplication([])

pencere = CeviriPenceresi()

pencere.show()

uygulama.exec()