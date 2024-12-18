#Buat aplikasi sebuah menghitung luas permukaan dengan rumus tabung 
#phi*r2+2*phi*r*
import os
os.system ("cls")

PHI = 3.14 
r = int(input("Masukan jari:"))
t = int(input("Masukan tinggi:"))

luas = PHI*(r*r)+2*PHI*r*t

print("Luas:",luas)
