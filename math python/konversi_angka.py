import os
os.system ("cls")

angka = int(input("Masukkan angka (1-10): "))
teks = ["satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan", "sepuluh"]

if 1 <= angka <= 10:
    print(f"Angka {angka} dalam teks adalah '{teks[angka - 1]}'")
else:
    print("Angka di luar rentang 1-10")
