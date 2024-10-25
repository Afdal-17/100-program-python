ipas = int(input("masukan nilai ipas: "))
b_indo = int(input("masukan nilai b indo: "))
b_sigma = int(input("masukan nilai b sigma: "))
b_mewing = int(input("masukan nilai b mewing: "))
total_nilai = ipas + b_indo + b_sigma + b_mewing

if total_nilai >= 200:
    print("kamu lulus menjadi siswa gyat")

else:
    print("oh no kamu bukan gyat")