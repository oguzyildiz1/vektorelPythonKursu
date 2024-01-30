import os

print(os.path.isfile("C:\\Python\\NEWS.txt"))

print(os.path.isdir("C:\\Python\\NEWS.txt"))

print(os.getcwd())

test = os.getcwd().split("\\")

print(test)

aaa = "-".join(test)

print(aaa.split("-"))