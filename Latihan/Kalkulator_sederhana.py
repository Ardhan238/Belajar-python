# Membuat kalkulator sederhana

print("===== Kalkulator Sederhana =====\n")

# input angka dan operator
angka1 = int(input("Masukkan angka pertama: "))
aritmatika = input("Masukkan Operator MTK: ")
angka2 = int(input("Masukkan angka kedua: "))
hasil = 0

# pengecekan dan hasil
if aritmatika == "+":
    hasil = angka1 + angka2
    print(f"Hasil dari {angka1} + {angka2} = {hasil}")
elif aritmatika == "-":
    hasil = angka1 - angka2
    print(f"Hasil dari {angka1} - {angka2} = {hasil}")
elif aritmatika == "*":
    hasil = angka1 * angka2
    print(f"Hasil dari {angka1} * {angka2} = {hasil}")
elif aritmatika == "/":
    hasil = angka1 / angka2
    print(f"Hasil dari {angka1} / {angka2} = {hasil}")
else :
    print("Operator tidak diketahui")