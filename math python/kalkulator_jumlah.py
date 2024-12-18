import os
os.system("cls")
def kalkulator_penjumlahan():
    print("Kalkulator Penjumlahan Sederhana")
    print("=" * 30)
    print("Masukkan angka (ketik 'q' untuk keluar)\n")
    
    while True:
        angka1 = input("Masukkan angka pertama: ")
        if angka1.lower() == 'q':  
            print("Keluar dari program. Terima kasih!")
            break
        
        angka2 = input("Masukkan angka kedua: ")
        if angka2.lower() == 'q':  
            print("Keluar dari program. Terima kasih!")
            break
        
        try:
            
            hasil = float(angka1) + float(angka2)
            print(f"Hasil penjumlahan: {hasil}\n")
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.\n")


kalkulator_penjumlahan()
