import os
os.system ("cls")
import random

n = random.randrange(1,10)

user = int(input("Masukan angka: "))
while n!= user:

    if user < n:
        print("Tiris")

        user = int(input("Masukan angka lagi: "))

    elif user > n:
        print("paranas")

        user = int(input("Masukan angka lagi: "))

    else:
        break
    print("ETA PISANN")
    print("HANUPIS,Hatur Nuhun Pisan")