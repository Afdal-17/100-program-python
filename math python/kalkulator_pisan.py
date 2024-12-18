import os
os.system ("cls")

print("Pilih operasi: \n1. Tambah \n2. Kurang \n3. Kali \n4. Bagi")
pilihan = int(input("Masukkan pilihan (1/2/3/4): "))
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))

if pilihan == 1:
    hasil = a + b
elif pilihan == 2:
    hasil = a - b
elif pilihan == 3:
    hasil = a * b
elif pilihan == 4:
    hasil = a / b
else:
    hasil = "Pilihan tidak valid"

print(f"Hasil: {hasil}")