import os
os.system("cls")
print("="*40)
print("RUMUS PERSEGI PANJANG")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung persegi panjang


p = int(input("Masukan panjang:" ))
l = int(input("Masukan lebar: "))

luas = lambda p,l: p*l
keliling = lambda p,l: 2*(p+l)

print("Luas: ",luas(p,l),"cm2")
print("Keliling: ",keliling(p,l),"cm2")