print("=====================================")
print("         soal pengkondisian          ")
print("=====================================")

a = int(input("Masukan nilai a:"))


if a >= 1 and a <= 50:
    print("Kelompok A")
if a >= 1 and a <= 25:
    print("Sub A1")
elif a >= 26 and a <= 50:
    print("Sub A2")

if a >= 51 and a <= 100:
    print("Kelompok B")
if a >= 51 and a <= 75:
    print("Sub B1")
elif a >= 76 and a <= 100:
    print("Sub A2")

