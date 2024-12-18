import os
os.system ("cls")
suhu = int(input("Masukan suhu:"))

if suhu>=0:
    print("cair")
elif suhu>=100:
    print("gas")
elif suhu<=0:
    print("es")

