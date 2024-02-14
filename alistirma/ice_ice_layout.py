from PyQt6.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_con = QVBoxLayout()
        #adı bölümü
        ver_con1 = QHBoxLayout()
        ver_con1.addWidget(QLabel("Adı"))
        ver_con1.addWidget(QLineEdit())

        main_con.addLayout(ver_con1)
        #soyadi bölümü
        ver_con2 = QHBoxLayout()
        ver_con2.addWidget(QLabel("Soyadı"))
        ver_con2.addWidget(QLineEdit())
        main_con.addLayout(ver_con2)

        pencere = QWidget()
        pencere.setLayout(main_con)
        # pencere.setFixedWidth()
        self.setCentralWidget(pencere)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()