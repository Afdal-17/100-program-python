#Buatlah program jumlah ulang tahun
#inputan nya tahun lahir dan berapa kali dia ulang tahun
import os
os.system ("cls")

tahun_lahir = int(input("Masukkan tahun lahir: "))
jml_ulang_tahun = int(input("Masukkan berapa kali ingin hitung ulang tahun: "))

print("Tahun ulang tahun:")
for i in range(1, jml_ulang_tahun + 1):
    tahun_ulang_tahun = tahun_lahir + i
    print(f"Ulang tahun ke-{i}: {tahun_ulang_tahun}")
