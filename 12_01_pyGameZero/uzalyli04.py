import pgzrun
from pgzero.actor import Actor
from keyboard import *


WIDTH = 600
HEIGHT = 375
TITLE = "UZAYLI"

uzayli = Actor('uzayli', (50,240))
arkaplan = Actor('uzaylı_arkaplan')
kutu = Actor('box', (650,270))
ari = Actor('arı',(750,100))
new_image = 'uzayli'



def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    ari.draw()


def update(dt):
    global new_image

    if kutu.x > -20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else: kutu.x = WIDTH + 20   

    if (keyboard.left or keyboard.a) and uzayli.x > 20:
        uzayli.x = uzayli.x - 5
        if new_image != 'uzaylı_sol':
            uzayli.image = 'uzaylı_sol'
            new_image = 'uzaylı_sol'
    elif (keyboard.right or keyboard.d) and uzayli.x < 600:
        uzayli.x = uzayli.x + 5
        if new_image != 'uzaylı_sağ':
            uzayli.image = 'uzaylı_sağ'
            new_image = 'sağ'
    else:
        uzayli.image = 'uzaylı'
        new_image = 'uzaylı'


    # if keyboard.space:
    #     karakter.y = 100
    #     animate(karakter, tween='bounce_end', duration=1, y=240)


def on_key_down(key):
    if keyboard.space:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)

"""
def update():
    karakter.x += 5
    if karakter.x > 600 : karakter.x = -50
    karakter.angle += 1
"""
    
pgzrun.go() # olay döngüsünü başlat.