print("="*40)
print("RUMUS KERUCUT")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung rumus kerucut


luas_permukaan = lambda r,s: 3.14*r*(r+s)
luas_alas= lambda r :3.14*r*r
luas_selimut = lambda r,s : 3.14*r*s
volume = lambda r,t : 1/3*3.14*(r*2)*t

print("Luas permukaan kerucut: ",luas_permukaan(5,3))
print("Luas alas kerucut: ",luas_alas(2))
print("Luas selimut: ",luas_selimut(3,4))
print("Volume: ",volume(4,7))