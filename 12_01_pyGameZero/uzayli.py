import pgzrun
import time
from pgzero.actor import Actor

WIDTH = 600
HEIGTH = 375
TITLE = "UZAYLI"

karakter = Actor('uzayli', (50,240))
arkaplan = Actor('uzaylı_arkaplan')
kutu = Actor('box', (650,270))
ari = Actor('box',())

def draw():
    arkaplan.draw()
    karakter.draw()
    kutu.draw()


def update():
    karakter.x += 5
    if karakter.x > 600 : karakter.x = -50
    karakter.angle += 1

pgzrun.go() # olay döngüsünü başlat.