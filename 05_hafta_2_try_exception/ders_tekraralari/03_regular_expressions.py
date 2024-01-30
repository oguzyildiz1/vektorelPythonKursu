#finding numbers

import re


text = "Bugün eve geç gittim. Bugün ayın 18'i"

x = re.findall("\s", text) #\s finds numbers if available

if x:
    print("Evet kelime cümle içinde bulundu")
else:
    print("Bulunamadı")
print(x)