import os
os.system ("cls")

teks = input("Masukkan sebuah teks: ")
terbalik = teks[::-1]
print(f"Teks {teks} jika dibalik menjadi {terbalik}.\n")

user = input("Lagi?: ")

while teks!= user:
    if user == "y":
        teks = input("Masukkan sebuah teks: ")
        print(f"Teks {teks} jika dibalik menjadi {terbalik}.\n")
        user = input("Lagi?: ")
    
    else:
        break



