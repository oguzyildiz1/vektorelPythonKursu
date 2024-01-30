import re

text = "The rain in spain"

x = re.findall("[a-m]", text)
print(x)