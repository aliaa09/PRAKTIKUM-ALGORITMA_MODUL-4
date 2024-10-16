# Fungsi untuk menentukan jumlah hari dalam suatu bulan
def jumlah_hari(bulan, tahun):
    # Daftar jumlah hari di setiap bulan
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Memeriksa tahun 
    if bulan == 2:
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            return 29  # Februari pada tahun kabisat
    return hari_per_bulan[bulan - 1]

# Input bulan dan tahun dari pengguna
while True:
    try:
        bulan = int(input("Masukkan bulan (1-12): "))
        tahun = int(input("Masukkan tahun: "))
        
        if 1 <= bulan <= 12:
            break  # Keluar dari perulangan jika input valid
        else:
            print("Bulan harus antara 1 dan 12. Coba lagi.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Menghitung dan menampilkan jumlah hari
hari = jumlah_hari(bulan, tahun)
print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah: {hari}")
