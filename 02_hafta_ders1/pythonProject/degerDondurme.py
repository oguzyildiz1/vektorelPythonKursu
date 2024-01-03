
def selamla():
    print("Merhaba")
    print("Nasılsın")


def topla(aa,bb):
    print(aa, "ile", bb, "toplamı:", aa+bb)
    return aa + bb


def cikar(aa,bb):
    print(aa, "ile", bb, "farkı:", aa - bb)
    return aa - bb


def carp(aa,bb):
    print(aa, "ile", bb, "çarpımı:", aa * bb)
    return aa * bb


def bol(aa,bb):
    print(aa, "ile", bb, "bölümü", aa / bb)
    return aa / bb


def tamBol(aa,bb):
    print(aa, "ile", bb, "tam bölümü", aa // bb)
    return aa // bb


def ustAl(aa,bb):
    print(aa, "üzeri",bb,"=",aa**bb)
    return aa ** 2


xx = 20
yy = 10
topla(xx,yy)
carp(xx,yy)
bol(xx,yy)
cikar(xx,yy)
tamBol(xx,yy)
ustAl(xx,2)

print(carp(xx,33))