# Pengenalan string

# Srting itu bisa dengn tanda (') atau ("")

nama_depan = 'Nur '
nama_tengah1 = 'Arins '
nama_tengah2 = 'Putri '
nama_belakang = 'Raya'

print ("Nama Depan :", nama_depan)
print ("Nama Tengah I :", nama_tengah1)
print ("Nama Tengah II :", nama_tengah2)
print ("Nama Belakang :",nama_belakang)

nama_lengkap = nama_depan + nama_tengah1 + nama_tengah2 + nama_belakang
print ("Nama Lengkap : ", nama_lengkap)

# panjang string
panjang_nama = len(nama_lengkap)
print (panjang_nama)

cekKata = "Put" in nama_lengkap
print (cekKata)


# format
print (f"Teman saya {nama_tengah1}")

uangSaku = 1000000
print (f'Uang saya ada {uangSaku:,}')