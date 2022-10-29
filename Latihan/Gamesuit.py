# Membuat game suit

import random
print("==== Game Suit ====\n")
inputUser = input("Apakah kamu ingin bermain? : ")

# Komputer
komputer = ""
rand = random.randrange(0, 11)
while inputUser == 'ya':
    
    player = input("Masukkan [batu, gunting, kertas]: ").lower()
    if rand >= 0 and rand <= 3:
        komputer = "Gunting"
        # tentukan rule
        if "kertas" in player: hasil = "Kamu Kalah"
        elif "batu" in player: hasil = "Kamu Menang"
        else: hasil = "Kita Seri"

    if rand > 3 and rand <= 6:
        komputer = "Kertas"
        # tentukan rule
        if "batu" in player: hasil = "Kamu Kalah"
        elif "gunting" in player: hasil = "Kamu Menang"
        else: hasil = "Kita Seri"

    else:
        komputer = "Batu"
        # tentukan rule
        if "gunting" in player: hasil = "Kamu Kalah"
        elif "kertas" in player: hasil = "Kamu Menang"
        else: hasil = "Kita Seri"

    print(f"Saya {komputer} kamu {player} hasilnya {hasil}")

    inputUser = input("Mau main lagi? : ")

print("Oke,terima kasih sudah bermain")