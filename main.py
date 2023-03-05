import os

nama_file = 'SI4602.txt'

print("==========================================")
print("Program CRUD Sistem Informasi Mahasiswa")
print("Kelas SI-46-02\n")
print("1. Mulai")
print("2. Keluar")
print("==========================================")

def main_menu():
    while True:
        print("\nPilih aksi:")
        print("1. Lihat Data")
        print("2. Cari Data")
        print("3. Tambah Data")
        print("4. Update Data")
        print("5. Hapus Data")
        print("6. Keluar")

        choice = input("Masukkan pilihan (1/2/3/4/5/6): ")
        print("\n")

        if choice == "1":
            show_data()
        elif choice == "2":
            search_data()
        elif choice == "3":
            add_data()
        elif choice == "4":
            update_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            print("Terima kasih")
            exit

def show_data():
    open_file = open(nama_file, 'r')
    lines = []
    for line in open_file:
        print(line)
        lines.append(line)
    open_file.close()
    return lines

def search_data():
    print("## Cari Data Mahasiswa ##")
    search = input("Cari Berdasarkan Kata Kunci (NIM/Nama/Alamat/Hobi): ")
    found = False
    lines = []
    open_file = open(nama_file, 'r')
    for line in open_file:
        if search.lower() in line.lower():
            found = True
            print(line)
        lines.append(line)
    open_file.close()

    if not found:
        print("Data Tidak Ditemukan.")
    
    return lines

def add_data():
    print("## Input Data Baru ##")
    data_nama = input("Masukkan Nama Lengkap: ")
    data_NIM = input("Masukkan NIM: ")
    data_alamat = input("Masukkan Alamat: ")
    data_hobi = input("Masukkan Hobi: ")
    file = open(nama_file, 'a')
    file.write(data_nama + " " + data_NIM + " " + data_alamat + " " + data_hobi  + '\n')
    file.close()
    print("\nData berhasil ditambahkan ke dalam file.\n")

def update_data():
    lines = show_data()
    found = False
    data_nama = input("Masukkan NIM data yang akan diupdate: ")
    if found:
        new_data_nama = input("Masukkan Nama Baru: ")
        new_data_NIM = input("Masukkan NIM Baru: ")
        new_data_alamat = input("Masukkan Alamat Baru: ")
        new_data_hobi = input("Masukkan Hobi Baru: ")
        file = open(nama_file, 'w')
        for line in lines:
            if data_nama.lower() in line.lower():
                file.write(new_data_nama + " " + new_data_NIM + " " + new_data_alamat + " " + new_data_hobi + '\n')
            else:
                file.write(line)
        file.close()
        print("\nData berhasil diupdate.\n")
    else:
        print("Data Tidak Ditemukan.")


def delete_data():
    lines = show_data()
    data_nama = input("Masukkan NIM yang akan dihapus: ")
    file = open(nama_file, 'w')
    for line in lines:
        if data_nama.lower() not in line.lower():
            file.write(line)
    file.close()
    print("Data berhasil dihapus.\n")

pilih = int(input("Masukkan pilihan (1/2): "))
if pilih == 1:
    main_menu()
elif pilih == 2:
    exit
else:
    print("Masukkan pilihan (1/2) saja, EXIT")