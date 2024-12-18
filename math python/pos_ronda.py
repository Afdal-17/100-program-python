import os
os.system ("cls")

import random
jadwal = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu"]
waktu = ["20:00","22:00","21;00","00:00","23:00"]
tugas = ["Nangkap maling","Ngeburu Hantu Jawa","Ciduk pelakor","ngeburu yang ngepet","Nangkap jodoh"]
s = input("Apakah kamu siap pos ronda?: ")

if s == "Yes":
    print("Jadwal kamu:",random.choice(jadwal))
    print("Waktu kamu:",random.choice(waktu))
    print("Tugas kamu kamu:",random.choice(tugas))

else:
    print("See you the next time")