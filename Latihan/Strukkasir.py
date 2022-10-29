# Membuat Struk Belanja
import datetime

waktu = datetime.datetime.now().strftime("%X")
tanggal = datetime.datetime.now().strftime("%x")

# Nama kasir
namaKasir = input("Masukkan nama kasir: ")

# Tampilan awal
print(f"""
            Enneagram Cafe
    Jl. Am. Sangadji Gonof Km. 12 masuk
                Klasaman
                Sorong
            081247271277

    {tanggal} {waktu}   KSR : {namaKasir}
""")

tambahBarang = 'y'
while('y' in tambahBarang):


    # Nama barang
    namaBarang = input("Masukkan nama barang: ")

    # Harga barang
    hargaBarang = int(input("Masukkan harga barang: "))

    # Jumlah barang
    jumlahBarang = int(input("Masukkan jumlah barang: "))

    # Tampilkan barang
    print(f"""
    {namaBarang}
    PCS     {jumlahBarang}    {hargaBarang:,}     {hargaBarang * jumlahBarang:,}
    """)

    # Kalkulasi total belanja dan jumlah belanja
    totalBelanja += (hargaBarang * jumlahBarang)
    jumlahBelanja += jumlahBarang
    
    # Tambah barang atau tidak
    tambahBarang = input("Ada barang lagi?(y/n): ")

# Tampikan total dan quality
print(f"""
{jumlahBelanja} Item
Total Belanja   : Rp.   {totalBelanja}
=================================
""")

print("Terima kasih, silahkan datang kembali :)")