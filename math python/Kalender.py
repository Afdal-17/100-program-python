import os
os.system ("cls")

import calendar

tahun = int(input("Masukkan tahun: "))
bulan = int(input("Masukkan bulan: "))

print(calendar.month(tahun, bulan))

