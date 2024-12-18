import os
os.system ("cls")

a = input("Masukkan nilai a: ")
b = input("Masukkan nilai b: ")
a, b = b, a
print(f"Setelah ditukar, nilai a: {a}, nilai b: {b}")