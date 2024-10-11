import os
os.system("cls")
print("="*40)
print("RUMUS PERSEGI")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung rumus persegi

def Persegi():
    s = int(input("Masukan s:"))
    l = lambda s: 2*s
    k = lambda s: 4*s


    print("sisi:",l(s),"cm2")
    print("keliling:",k(s),"cm2")

while True:
    Persegi()
    ulang = input('Mau diulang? (y/n) : ')
    if ulang == "n":
        break



