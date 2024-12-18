import os
os.system("cls")
print("=========================")
print("  CONTOH PENGGUNAAN EVAL ")
print("=========================")

kondisi = "30 > 20 "
hasil = eval(kondisi)
print("Hasil:", hasil)

kondisi = "20 > 30 "
hasil = eval(kondisi)
print("Hasil:", hasil)

operasi ="200+250*78/2"
h = eval(operasi)
print("Hasil:",h)
