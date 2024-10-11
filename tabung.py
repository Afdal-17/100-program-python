print("="*40)
print("RUMUS TABUNG")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung rumus tabung


r = int(input("Masukan jari jari: "))
t = int(input("Masukan tinggi:"))

v = 3.14*(r*2)*t
lp = 2*3.14*r*(r+t)

print("Volume tabung: ",v)
print("Luas permukaan tabung: ",lp)