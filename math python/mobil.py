import os
os.system ("cls")
class Mobil:
    def __init__(self, merek, warna):
        self.merek = merek  
        self.warna = warna  

    def deskripsi(self):
        return f"Mobil ini adalah {self.warna} {self.merek}."


mobil1 = Mobil("Toyota", "Merah")
mobil2 = Mobil("Honda", "Biru")


print(mobil1.deskripsi())  
print(mobil2.deskripsi())  