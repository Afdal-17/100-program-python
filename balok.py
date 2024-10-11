print("="*40)
print("RUMUS BALOK")
print("="*40)
# Dibuat oleh : Afdal
# Tanggal pengerjaan : 9 oktober
# Program menghitung rumus balok

def balok(p,l,t):
    v = p*l*t
    return v

volume = balok(3,2,5)
print("Volume:",volume)

def balok(p,l,t):
    lp = 2*(p*l+p*t+l*t)
    return lp

luas_permukaan = balok(3,2,5)
print("Luas permukaan:",luas_permukaan)
   