#oranlı bir şekilde içeriği dağıtıyor.

from numpy import random

x2 = random.choice([3, 5], p=[0.2, 0.8], size=(5, 6)) #yüze kadar olan sayılardan 5 elemanlı bir dizi üret demek

print("3 ten 0.2, 5 ten 0.8 oranlı kullanarak yeni dizi: \n", x2)
