import turtle as t


t.speed(100)

def kare(x):
    if x < 10: return x
    else:
        for i in range(4):
            t.forward(x)
            t.right(90)
        
        return kare(x-10)


aa = int(input("Karenin uzun kenarı ne kadar?"))

kare(aa)

def kare2(x):
    if x < 20: return x
    else:
        for i in range(6):
            t.forward(x)
            t.right(90)
        
        return kare(x-10)

bb = int(input("Hello "))

kare2(bb)

input()




