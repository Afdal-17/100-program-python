import os
os.system("cls")
def Persegi():
    sisi = int(input("sisi\t\t: "))
    luas = lambda s : s*s
    keliling = lambda s: 4*s
    print("luas\t\t:",luas(sisi),"cm2")
    print("keliling\t:",keliling(sisi),"cm")
    

while True:
    Persegi()
    ulang = input('Mau diulang? (y/n) : ')
    if ulang == "n":
        break
