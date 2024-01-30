#findin match cases

import re


text = "Bugün eve geç gittim. Bugün ayın 18'i"

x = re.findall("[ü]", text) #\s finds numbers if available

if x:
    print("Evet kelime cümle içinde bulundu")
    text2 = re.sub("[üçı]","[uci]",text,3)
else:
    print("Bulunamadı")
print(x)

print("değişti :", text2)