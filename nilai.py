nilai = []
jml = int(input("Jumlah data yang akan diinput: "))

for i in range(jml):
    nilai.append(float(input(f"Nilai ke-{i+1}: ")))

total = max = 0
min = nilai[0]

total = rata2 = max = min = 0
for data in nilai:
    total += (data)
    if data > max :
        max = data

    min = data
    if data < min:
        min = data

print(total)
print(f"Rata rata : {total/jml}")
print(f"Nilai terbesar : {max}")
print(f"Nilai terkecil : {min}")
