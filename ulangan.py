PHI = 3.14
r = float(input("masukan jari jari: "))
s = float(input("masukan s: "))
t = float(input("masukan t: "))
luas_selimut = PHI*r*s
luas_permukaan = (PHI*r*s)+(PHI*r*r)
keliling = 1/3*PHI*r*r*t

print("luas s:",luas_selimut)
print("luas p:",luas_permukaan)
print("keliling:",keliling)