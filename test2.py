#PERCEPATAN RATA RATA
# a = V2 - V1 / t2 -t1

print("\033[92m===============================")
print("     PERCEPATAN RATA RATA     ")
print("-------------------------------")
v2 = float(input("masukan kecepatan awal: "))
v1 = float(input("masukan kecepatan akhir: "))

t2 = float(input("masukan waktu awal: "))
t1 = float(input("masukan waktu akhir: "))

v = float(v2)-float(v1)
t = float(t2)-float(t1)

hasil = float(v)/float(t)

print("\033[1m"f"\nHasilnya adalah: {round (hasil)/2} m/s")

print("_________________________________")