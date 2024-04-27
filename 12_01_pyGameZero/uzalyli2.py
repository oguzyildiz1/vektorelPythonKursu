import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 375
TITLE = "UZAYLI"

karakter = Actor('uzayli', (50,240))
arkaplan = Actor('uzaylı_arkaplan')
kutu = Actor('box', (650,270))
ari = Actor('arı',(750,100))

def draw():
    arkaplan.draw()
    karakter.draw()
    kutu.draw()
    ari.draw()


def update():
    kutu.x -= 4
    if kutu.x < 0: kutu.x = 650
    kutu.angle += 3
    ari.x -=3
    if ari.x < 0: ari.x = 750

    if keyboard.left:
        karakter.x -= 5
    if keyboard.right:
        karakter.x += 5
    # if keyboard.space:
    #     karakter.y = 100
    #     animate(karakter, tween='bounce_end', duration=1, y=240)


def on_key_down(key):
    if keyboard.space:
        karakter.y = 100
        animate(karakter, tween='bounce_end', duration=2, y=240)

"""
def update():
    karakter.x += 5
    if karakter.x > 600 : karakter.x = -50
    karakter.angle += 1
"""
    
pgzrun.go() # olay döngüsünü başlat.