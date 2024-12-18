#Buatlah program dengan sebuah pertanyaan pg
import os
os.system("cls")

pertanyaan = "Siapa penemu bahasa pemrograman Python?"
pilihan = ["1. Guido van Rossum", "2. Afdal ganteng", "3. Asep puloh", "4. Agus peyeum"]
jawaban_benar = "1"


print(pertanyaan)
for p in pilihan:
    print(p)

jawaban = input("Pilih jawaban (1-4): ")

if jawaban == jawaban_benar:
    print("Bjirrrrr Benar si eta!")
else:
    print("Salah woi!")


