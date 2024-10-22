print('SELAMAT DATANG DI ATM')
print('PILIH OPSI:') 
print('1. check saldo saya')
print('2. ambil saldo saya')
print('3. tabung saldo saya')
option=int(input('silahkan pilih opsi :'))
uang_kamu=15000000
if option==1:
    print('saldo saya berjumlah Rp.150.000.00')
elif option==2:
    print('saldo saya berjumlah Rp.150.000.00, ingin mengambil berapa?')
    print('1. Rp.30.000.00')
    print('2. Rp.60.000.00')
    print('3. Rp.150.000.00')
    option2=int(input('opsi:'))
    if option2==1:
        hasil=uang_kamu-3000000
        print('uang anda sekarang berjumlah ',hasil)
    elif option2==2:
        hasil2=uang_kamu-6000000
        print('uang anda sekarang berjumlah ',hasil2)
    elif option2==3:
        hasil3=uang_kamu-15000000
        print('uang anda sekarang berjumlah ',hasil3)
    else:
        print('keyword anda salah,mohon ulangi lagi!')
elif option==3:
    print('uang saya berjumlah Rp.150.000.00, mau tabung berapa?')
    option3=int(input('masukkan jumlah uang:'))
    hasil3=uang_kamu+option3
    print('jumlah uang kamu sekarang adalah',hasil3)
else:
    print("pilihan anda salah, silahkan ulangi lagi")