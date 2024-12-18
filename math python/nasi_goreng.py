import os
os.system ("cls")
class NasiGoreng:
    def __init__(self):
        self.bahan = []
        self.langkah = []

    def tambah_bahan(self, bahan):
        self.bahan.append(bahan)

    def tambah_langkah(self, langkah):
        self.langkah.append(langkah)

    def masak(self):
        print("Membuat Nasi Goreng:")
        print("\nBahan:")
        for b in self.bahan:
            print(f"- {b}")
        
        print("\nLangkah-langkah:")
        for i, l in enumerate(self.langkah, 1):
            print(f"{i}. {l}")

# Membuat NasiGoreng
nasi_goreng = NasiGoreng()

# tambahkan bahan
nasi_goreng.tambah_bahan("Nasi")
nasi_goreng.tambah_bahan("Minyak Goreng")
nasi_goreng.tambah_bahan("Bawang Merah")
nasi_goreng.tambah_bahan("Bawang Putih")
nasi_goreng.tambah_bahan("Kecap Manis")
nasi_goreng.tambah_bahan("Telur")
nasi_goreng.tambah_bahan("Sayuran (wortel, kacang polong)")

# Menambahkan langkah
nasi_goreng.tambah_langkah("Panaskan minyak dalam wajan.")
nasi_goreng.tambah_langkah("Tumis bawang merah dan bawang putih hingga harum.")
nasi_goreng.tambah_langkah("Masukkan telur, aduk hingga setengah matang.")
nasi_goreng.tambah_langkah("Tambahkan nasi dan aduk rata.")
nasi_goreng.tambah_langkah("Tambahkan kecap manis dan sayuran, aduk hingga semua tercampur.")
nasi_goreng.tambah_langkah("Sajikan nasi goreng dalam piring.")

# Memasak
nasi_goreng.masak()
