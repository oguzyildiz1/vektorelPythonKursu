puan = int(input("Matematik puanın kaç? "))
cins = input("Cinsiyetin nedir? ")
if puan < 0 or puan > 100: print("Yanlış giriş")
else:
    if puan > 85: print("B+ aldın")
    elif puan > 75: print("C+ aldın")
    elif puan > 65: print("C- aldın")
    else: print("Kalmışsın.")

if puan > 85 and (cins == "erkek" or cins == "Erkek"):
    print("Futbol takımına girebilirsin.")
else:
    print("Takıma giremezsiniz.")