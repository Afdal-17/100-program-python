import os
os.system ("cls")

def is_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Masukkan angka: "))
if is_prima(n):
    print(f"{n} adalah bilangan prima")
else:
    print(f"{n} bukan bilangan prima")