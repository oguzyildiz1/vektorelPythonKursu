from PyQt6.QtWidgets import *
import mysql.connector

app = QApplication([])

class Login(QMainWindow):
    def tiklama1(self):
        kullanici = self.ka.text()
        sifre = self.sf.text()
        dogruKullanici = "Oguz"
        dogruSifre = "123456"
        mesaj = QMessageBox()

        if kullanici == dogruKullanici and sifre == dogruSifre:
            mesaj.setText("Programa giriş yapabilirsin")
            self.close()
            self.xx = Uygulamaekrani()
            self.xx.show()

        else:
            mesaj.setText("Yanlış giriş.")
        # mesaj.setText("tıklandı")
        # mesaj.setText(f"Kullanıcı adı: {kullanici} Şifre: {sifre} ")
        mesaj.exec()

    def tiklama(self):
        print("Tıklandı")

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Kullanıcı adı: "))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Şifre: "))
        self.sf = QLineEdit()
        icerik.addWidget(self.sf)
        bt = QPushButton("Giriş yap")
        bt.clicked.connect(self.tiklama1)
        icerik.addWidget(bt)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

class Uygulamaekrani(QMainWindow):
    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        bt1 = QPushButton("Uygulama 1")
        icerik.addWidget(bt1)
        bt1.clicked.connect(self.ceviriac)
        bt2 = QPushButton("Uygulama 2")
        icerik.addWidget(bt2)
        # bt2.clicked.connect(Uygulamaekrani())

        

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

    def ceviriac(self):
        self.cevir = Ceviriprogrami()
        self.cevir.show()

class Ceviriprogrami(QMainWindow):
    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout()
        icerik.addWidget(QLabel("Ceviri programı"))
        self.le1 = QLineEdit()

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

ekran = Login()


ekran.show()

app.exec()