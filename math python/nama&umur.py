def main():
    print("Selamat datang di program sederhana!")
    
    nama = input("Masukkan nama Anda: ")
    
    try:
        umur = int(input("Masukkan umur Anda: "))
    except ValueError:
        print("Umur harus berupa angka!")
        return
    
    print(f"Halo, {nama}!")
    if umur < 18:
        print("Anda masih muda! Nikmati masa-masa indah ini.")
    elif 18 <= umur <= 50:
        print("Anda berada di usia produktif. Tetap semangat!")
    else:
        print("Anda penuh dengan pengalaman hidup. Bagikan kebijaksanaan Anda!")
    
    print("Terima kasih telah menggunakan program ini!")


if __name__ == "__main__":
    main()
