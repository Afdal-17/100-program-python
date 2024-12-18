import os
os.system ("cls")

n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))
fibonacci = [0, 1]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(f"Deret Fibonacci ({n} bilangan) adalah: {fibonacci}\n")

user = input("lagi?: ")

while n!= user:
    if user == "y":
        n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))
        print(f"Deret Fibonacci ({n} bilangan) adalah: {fibonacci}\n")
        user = input("lagi?")


    else:
        break