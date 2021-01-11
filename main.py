print("===== APLIKASI PENGOLAHAN DATA NILAI MAHASISWA =====")
while True:
    print("MENU : \n 1. Tambah Data \n 2. Ubah Data \n 3. Hapus Data \n 4. Cari Data \n 5. Keluar Aplikasi")
    pilih = int(input("Pilih Menu (1/2/3/4/5) : "))
    if pilih == 1:
        tambah_data()
        input_data()
    elif pilih == 2:
        print("Data siapa yang akan diubah ?")
        siapa = input("Masukkan Nama Mahasiswa yang akan diubah : ")
        #daftar_nilai.ubah_data(xsiapa=siapa)
    elif pilih == 3:
        hapus_data()
    elif pilih == 4:
        cari_data()
    elif pilih == 5:
        break
    else:
        print("!!! === ERROR! Pilihan yg anda masukan salah === !!!")