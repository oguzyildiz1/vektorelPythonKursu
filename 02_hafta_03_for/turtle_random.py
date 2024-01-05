import turtle as t
import random as r

t.speed(10)

t.color("green")

for a in range(10): #10 açılı dönüyor tam
    t.penup()
    t.goto(r.randint(-100,100),r.randint(-150,150))
    t.pendown()
    for b in range(4):
        t.color("red")
        t.forward(100)
        t.right(90)

