print("="*40)
print("RUMUS BOLA")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung rumus bola

jari_jari = int(input("Masukan jari jari: "))
lp = lambda r: 4*3.14*(r*r)
v = lambda j: 4/3*3.14*(j*3)
print("Luas permukaan bola: ",lp(jari_jari))
print("Volume bola: ",v(jari_jari))

