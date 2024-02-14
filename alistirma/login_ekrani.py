#pyqt kütüphanesi ile login ekranı oluşturma.

import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

window = QMainWindow()

window.setWindowTitle("Login screen")
# window.setFixedWidth(200)
# window.setFixedHeight(100)

layout = QVBoxLayout()

layout.addWidget(QLabel("Kullanıcı adı:"))
layout.addWidget(QLineEdit())
layout.addWidget(QLabel("Şifre:"))
layout.addWidget(QLineEdit())
layout.addWidget(QCheckBox("Beni hatırla"))
layout.addWidget(QPushButton("Giriş yap"))
layout.addWidget(QLabel("..."))



widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)
window.show()
app.exec()