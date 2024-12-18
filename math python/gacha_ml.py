import os
os.system ("cls")
print("="*60)
print("SELAMAT DATANG DI GACHA SKIN COLECTOR MOBILE LEGENDS")
print("="*60)

import random

g = 1500
k = 250
print("silahkan memulai untuk gacha dengan harga 250 DM")
x = ("ya","no")
for i in x:
    print(i)

isi = ["Magic dust","Koin 1000","Rank protection","Level up card","Arlot Colector","Skin epic Phoveus","Avatar","Skin trial pack","Hero trial pack","Ticket","Emote","Fragment","Lucky Ticket","Choice chest","Premium fragment","Vexana","Magic Wheel potion","Rare skin fragment"]

user = input("Masukan: ")

target = "Arlot Colector"
        
while isi!= user and g>0:

    if user == "ya":
        pilihan = random.choice(isi)
        print("Selamat Anda Mendapatkan: ",pilihan)
        
        g -= k

        print("Sisa diamond anda: ",g)
        
        user = input("Mau lagi?: ")

    elif user == "no":
        print("Terimakasih sudah meng gacha!")
        print("Sisa diamond anda:",g)
        
        
    elif pilihan == [4]:
        print("Selamat anda telah Mendapatkan skin utama:")
        print("==========================================")
        print("\033[0;33mARLOT COLECTOR")
        print("==========================================")
        break

    elif g<=0 :
        print("Mohon maaf Diamond anda sudah habis silahkan isi ulang")
        break   


