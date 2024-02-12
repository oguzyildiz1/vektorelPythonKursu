from PyQt6.QtWidgets import *

aa = QApplication([])

button = QPushButton('Click')

def aaa():
    alert = QMessageBox()
    alert.setText('Tıkladın!')
    alert.exec()
    print('Tıklama gerçekleşti...')


button.clicked.connect(aaa)

button.show()

aa.exec()