import os
os.system ("cls")

try:
    angka = int(input("Masukan angka:"))
except ValueError:
    print("Itu bukan angka!")
    