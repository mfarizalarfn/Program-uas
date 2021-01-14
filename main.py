from model.daftar_nilai import ubah_data, hapus_data, cari_data
from view.input_nilai import tambah_data

print("=================================================")
print("\tAPLIKASI PENGOLAHAN DATA NILAI MAHASISWA\t")
print("=================================================")
print(" NAMA\t\t: Mohamad Farizal arifin\t\t\t")
print(" NIM\t\t: 312010231\t\t\t\t\t\t\t")
print(" KELAS\t\t: TI.20.B.1\t\t\t\t\t\t\t")
print("=================================================")
while True:
    print("MENU : \n 1. Tambah Data \n 2. Ubah Data \n 3. Hapus Data \n 4. Cari Data \n 5. Keluar Aplikasi")
    pilih = int(input("Pilih Menu (1/2/3/4/5) : "))
    if pilih == 1:
        tambah_data()
    elif pilih == 2:
        print("Data siapa yang akan diubah ?")
        siapa = input("Masukkan Nama Mahasiswa yang akan diubah : ")
        ubah_data(xsiapa=siapa)
    elif pilih == 3:
        print("========== HAPUS DATA NILAI MAHASISWA ==========")
        print("Data siapa yang akan diubah ?")
        hsiapa = input("Masukkan Nama Mahasiswa yang akan diubah : ")
        hapus_data(hsiapa)
    elif pilih == 4:
        print(" Pencarian berdasarkan NIM ")
        pencarian = input("Masukkan Nama yang akan dicari : ")
        cari_data(csiapa=pencarian)
    elif pilih == 5:
        print("========== ANDA KELUAR DARI APLIKASI ==========")
        break
    else:
        print("!!! === ERROR! Pilihan yang anda masukan salah === !!!")