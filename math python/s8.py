import os
os.system ('cls')

matematika= int(input("Masukan nilai:"))
indo = int(input("Masukan nilai:"))
pab = int(input("Masukan nilai:"))
pkn = int(input("Masukan nilai:"))
rata = (matematika+indo+pab+pkn)/3
print("rata rata:",rata)

if rata>90:
    print("Nilai anda : A")

elif 70<rata<85:
    print("NIlai anda: B")

elif 60<rata<70:
    print("Nilai anda: C")

else:
    print("Nilai anda: D")




