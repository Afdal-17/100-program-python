import os
os.system("cls")

print("\033[0;37m="*40)
jurusan = ["PPLG","TJKT","MPLB","PS","AKKUL"]
pertanyaan = "Jurusan mana yang akan anda pilih?:"


print(pertanyaan) 
for i in jurusan:
    print(i)
print("="*40)

jawab = input("Jawab:")
print("="*40)

if jawab == "PPLG":
    print(jurusan[0])
    print('''\033[0;32mPengembangan Perangkat Lunak dan Gim atau PPLG
Adalah jurusan yang berfokus pada dunia codingan dan bidang it
.Codingan adalah berkomunikasi dengan bahasa komputer menggunakan
syntax''')

elif jawab == "TJKT":
    print(jurusan[1])
    print('''\033[0;33mTeknik Jaringan Komputer dan Telekomunikasi 
(TJKT) memegang peran penting dalam menghubungkan dunia 
melalui jaringan komputer dan sistem telekomunikasi. 
Artikel ini akan membahas konsep dasar TJKT, fokus pada 
technopreneurship, dan menggali potensi di bidang ini.''')

elif jawab == "MPLB":
    print(jurusan[2])
    print('''\033[0;35mManajemen Perkantoran dan Layanan Bisnis (MPLB)
/Otomatisasi dan Tata Kelola Perkantoran (OTKP) merupakan program
/kompetensi keahlian yang membekali peserta didik dengan keterampilan
, pengetahuan dan sikap untuk menjadi tenaga kerja tingkat menengah 
yang memiliki kecakapan dan kompeten dalam bidang pengelolaan administrasi perkantoran. ''')
    
elif jawab == "PS":
    print(jurusan[3])
    print('''\033[31m jurusan Pemasaran adalah salah satu jurusan di bidang bisnis 
yang berfokus pada pembelajaran mengenai cara memasarkan produk dan jasa, baik
secara langsung maupun digital. Jurusan ini mempersiapkan siswa untuk menjadi tenaga
profesional di bidang pemasaran, dengan kemampuan dalam menarik minat konsumen,
mengelola penjualan, dan memahami perilaku pasar.''')
     
elif jawab == "AKKUL":
    print(jurusan[4])
    print('''\033[34m Jurusan AKKUL adalah singkatan dari Administrasi Keuangan dan Kewirausahaan. 
Jurusan ini mempersiapkan siswa untuk bekerja di bidang administrasi keuangan, akuntansi,
serta mengembangkan keterampilan kewirausahaan untuk menjalankan atau mengelola bisnis. 
Jurusan ini sangat relevan dengan dunia usaha, karena mengajarkan keterampilan dalam mengelola
keuangan dan operasional bisnis secara efisien.''')

print("="*40)