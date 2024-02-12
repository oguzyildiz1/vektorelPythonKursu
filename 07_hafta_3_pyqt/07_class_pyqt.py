from PyQt6.QtWidgets import *

class Pencere(QMainWindow):
    pass


uygulama = QApplication([])

anaPencere = Pencere()

anaPencere.setWindowTitle('Deneme')

anaPencere.show()

uygulama.exec()