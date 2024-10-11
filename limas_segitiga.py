import os
os.system("cls")
print("="*40)
print("RUMUS LIMAS SEGITIGA")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung segitiga


luas_alas = lambda a,t: 1/2*a*t
luas_permukaan = lambda g,y: g+y
volume_limas = lambda la,tl: 1/3*la*tl
                    
print("Luas alas:",luas_alas(2,5))
print("Luas permukaan:",luas_permukaan(3,2))
print("Volume:",volume_limas(6,6))