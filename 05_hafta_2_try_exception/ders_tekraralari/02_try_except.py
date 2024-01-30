a = 5000
b = "6000"

try:
    print((a + b)/ 2)
except TypeError:
    print("Kardeşim doğru gir.")
except:
    print("Bilinmeyen bir hata oluştu")