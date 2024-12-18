import os
os.system ("cls")

batas = int(input("Masukkan batas angka: "))

print("Angka ganjil dari 1 sampai", batas, ":")
for i in range(1, batas + 1):
    if i % 2 != 0:
        print(i)