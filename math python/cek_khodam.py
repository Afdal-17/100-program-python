import os
os.system ("cls")
print("="*57)
print(" SELAMAT DATANG DI CEK KHODAM, SILAHKAN MASUKAN NAMA ANDA ")
print("="*57)
import random
khodam = ["Naga sawah","Superstar Jumbo","Sapu","Ambalabu","Ambatukang","Mejikom","Asbak bali","Taplak Meja","Rusdi","Si imut","Ambasing"]
name = input("Masukan nama anda: ")

if name:
    print("Khodam anda adalah: ",random.choice(khodam)) 

