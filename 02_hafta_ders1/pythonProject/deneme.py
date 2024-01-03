
def selamla():
    print("Merhaba")
    print("Nasılsın")


def topla(aa,bb):
    print(aa, "ile", bb, "toplamı:", aa+bb)


def cikar(aa,bb):
    print(aa, "ile", bb, "farkı:", aa - bb)


def carp(aa,bb):
    print(aa, "ile", bb, "çarpımı:", aa * bb)


def bol(aa,bb):
    print(aa, "ile", bb, "bölümü", aa / bb)


def tamBol(aa,bb):
    print(aa, "ile", bb, "tam bölümü", aa // bb)


def ustAl(aa,bb):
    print(aa, "üzeri",bb,"=",aa**bb)


xx = 20
yy = 10
topla(xx,yy)
carp(xx,yy)
bol(xx,yy)
cikar(xx,yy)
tamBol(xx,yy)
ustAl(xx,2)