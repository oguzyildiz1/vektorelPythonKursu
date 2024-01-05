import turtle

turtle.speed(10)

##for a in range(16):
for i in range(8):
    if i%2 == 0:
        turtle.color("red")
    else:
        turtle.color("blue")    
    for j in range(4):
        turtle.forward(50)
        turtle.right(40)
    turtle.right(25)

