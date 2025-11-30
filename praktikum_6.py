# Program Manajemen Nilai Mahasiswa
# Menggunakan fungsi-fungsi untuk operasi CRUD

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

def tambah():
    """Fungsi untuk menambah data mahasiswa"""
    print("\n=== TAMBAH DATA MAHASISWA ===")
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    
    # Cek apakah nama sudah ada
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            print(f"Data mahasiswa dengan nama '{nama}' sudah ada!")
            return
    
    # Tambah data baru
    data_mahasiswa.append({
        'nama': nama,
        'nilai': nilai
    })
    print(f"Data mahasiswa '{nama}' berhasil ditambahkan!")

def tampilkan():
    """Fungsi untuk menampilkan semua data mahasiswa"""
    print("\n=== DAFTAR NILAI MAHASISWA ===")
    
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
    
    print("-" * 40)
    print(f"{'No.':<4} {'Nama':<20} {'Nilai':<10}")
    print("-" * 40)
    
    for i, mhs in enumerate(data_mahasiswa, 1):
        print(f"{i:<4} {mhs['nama']:<20} {mhs['nilai']:<10.2f}")
    
    print("-" * 40)
    print(f"Total mahasiswa: {len(data_mahasiswa)}")

def hapus(nama):
    """Fungsi untuk menghapus data mahasiswa berdasarkan nama"""
    print(f"\n=== HAPUS DATA MAHASISWA: {nama.upper()} ===")
    
    for i, mhs in enumerate(data_mahasiswa):
        if mhs['nama'].lower() == nama.lower():
            data_mahasiswa.pop(i)
            print(f"Data mahasiswa '{nama}' berhasil dihapus!")
            return
    
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan!")

def ubah(nama):
    """Fungsi untuk mengubah data mahasiswa berdasarkan nama"""
    print(f"\n=== UBAH DATA MAHASISWA: {nama.upper()} ===")
    
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            print(f"Data saat ini: Nama = {mhs['nama']}, Nilai = {mhs['nilai']}")
            
            # Input data baru
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            nilai_baru = input("Masukkan nilai baru (kosongkan jika tidak diubah): ")
            
            # Update data jika ada input baru
            if nama_baru:
                # Cek apakah nama baru sudah ada (kecuali jika sama dengan nama lama)
                if nama_baru.lower() != nama.lower():
                    for mhs_lain in data_mahasiswa:
                        if mhs_lain['nama'].lower() == nama_baru.lower():
                            print(f"Data mahasiswa dengan nama '{nama_baru}' sudah ada!")
                            return
                mhs['nama'] = nama_baru
            
            if nilai_baru:
                mhs['nilai'] = float(nilai_baru)
            
            print("Data berhasil diubah!")
            return
    
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan!")

def menu_utama():
    """Fungsi untuk menampilkan menu utama"""
    while True:
        print("\n" + "=" * 50)
        print("SISTEM MANAJEMEN NILAI MAHASISWA")
        print("=" * 50)
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
        print("-" * 50)
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == '1':
            tambah()
        elif pilihan == '2':
            tampilkan()
        elif pilihan == '3':
            if data_mahasiswa:
                tampilkan()
                nama = input("\nMasukkan nama mahasiswa yang akan dihapus: ")
                hapus(nama)
            else:
                print("Belum ada data mahasiswa.")
        elif pilihan == '4':
            if data_mahasiswa:
                tampilkan()
                nama = input("\nMasukkan nama mahasiswa yang akan diubah: ")
                ubah(nama)
            else:
                print("Belum ada data mahasiswa.")
        elif pilihan == '5':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid! Silakan pilih 1-5.")

# Menambahkan beberapa data contoh
def data_contoh():
    """Fungsi untuk menambahkan data contoh (opsional)"""
    data_mahasiswa.extend([
        {'nama': 'Budi Santoso', 'nilai': 85.5},
        {'nama': 'Siti Aminah', 'nilai': 92.0},
        {'nama': 'Ahmad Rizki', 'nilai': 78.5}
    ])
    print("Data contoh telah ditambahkan!")

# Jalankan program
if __name__ == "__main__":
    # Opsional: tambah data contoh
    tambah_contoh = input("Tambahkan data contoh? (y/n): ").lower()
    if tambah_contoh == 'y':
        data_contoh()
    
    # Jalankan menu utama
    menu_utama()