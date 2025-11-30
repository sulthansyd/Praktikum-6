# Praktikum-6
Penjelasan Detail Program Manajemen Nilai Mahasiswa
Struktur Program Secara Keseluruhan
Program ini adalah sistem manajemen data nilai mahasiswa sederhana yang mengimplementasikan operasi CRUD (Create, Read, Update, Delete) menggunakan fungsi-fungsi Python.

1. Variabel Global
```
data_mahasiswa = []
Fungsi: Menyimpan semua data mahasiswa dalam bentuk list of dictionaries

Struktur Data: [{'nama': 'Budi', 'nilai': 85.5}, {'nama': 'Siti', 'nilai': 92.0}]

Scope: Global, bisa diakses oleh semua fungsi
```
2. Fungsi tambah()
Tujuan: Menambahkan data mahasiswa baru
```
def tambah():
    print("\n=== TAMBAH DATA MAHASISWA ===")
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
Alur Eksekusi:
Input Data: Meminta nama (string) dan nilai (float)
```
Validasi Duplikasi:

```
for mhs in data_mahasiswa:
    if mhs['nama'].lower() == nama.lower():
        print(f"Data mahasiswa dengan nama '{nama}' sudah ada!")
        return
```
Mengecek apakah nama sudah ada di database

Case-insensitive (BUDI = budi = Budi)

Jika ada, program berhenti dengan return

Simpan Data:

```
data_mahasiswa.append({
    'nama': nama,
    'nilai': nilai
})
Menambahkan dictionary baru ke list data_mahasiswa
```
3. Fungsi tampilkan()
Tujuan: Menampilkan semua data dalam format tabel
```
def tampilkan():
    if not data_mahasiswa:
        print("Belum ada data mahasiswa.")
        return
```
Alur Eksekusi:
Cek Data Kosong: Jika list kosong, tampilkan pesan dan berhenti

Format Tabel:

```
print("-" * 40)
print(f"{'No.':<4} {'Nama':<20} {'Nilai':<10}")
print("-" * 40)
:<4 = alignment left dengan width 4 karakter
```
Membuat header tabel yang rapi

Looping Data:

```
for i, mhs in enumerate(data_mahasiswa, 1):
    print(f"{i:<4} {mhs['nama']:<20} {mhs['nilai']:<10.2f}")
enumerate(..., 1): memberikan nomor urut mulai dari 1

{mhs['nilai']:<10.2f}: format nilai dengan 2 digit desimal
````

4. Fungsi hapus(nama)
Tujuan: Menghapus data berdasarkan nama
```
def hapus(nama):
    for i, mhs in enumerate(data_mahasiswa):
        if mhs['nama'].lower() == nama.lower():
            data_mahasiswa.pop(i)
            print(f"Data mahasiswa '{nama}' berhasil dihapus!")
            return
Alur Eksekusi:
Search Data:

Looping dengan enumerate() untuk mendapatkan index (i) dan data (mhs)

Pencarian case-insensitive

Hapus Data:

data_mahasiswa.pop(i): menghapus item pada index ke-i

return: keluar dari fungsi setelah berhasil menghapus

Data Tidak Ditemukan:

Jika loop selesai tanpa menemukan data, tampilkan pesan error
```

5. Fungsi ubah(nama)
Tujuan: Mengubah data mahasiswa berdasarkan nama
```
def ubah(nama):
    for mhs in data_mahasiswa:
        if mhs['nama'].lower() == nama.lower():
            print(f"Data saat ini: Nama = {mhs['nama']}, Nilai = {mhs['nilai']}")
Alur Eksekusi:
Cari Data: Sama seperti fungsi hapus

Tampilkan Data Saat Ini: Memberi konteks ke user
```
Input Data Baru:

```
nama_baru = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
nilai_baru = input("Masukkan nilai baru (kosongkan jika tidak diubah): ")
Mengizinkan partial update (hanya nama atau hanya nilai)
```

Validasi Nama Baru:

```
if nama_baru.lower() != nama.lower():
    for mhs_lain in data_mahasiswa:
        if mhs_lain['nama'].lower() == nama_baru.lower():
            print(f"Data mahasiswa dengan nama '{nama_baru}' sudah ada!")
            return
```
Cek duplikasi hanya jika nama diubah

Boleh sama dengan nama lama

Update Data:

```
if nama_baru:
    mhs['nama'] = nama_baru
if nilai_baru:
    mhs['nilai'] = float(nilai_baru)
Hanya update field yang diisi user
```
6. Fungsi menu_utama()
Tujuan: Menyediakan interface interaktif untuk user

```
def menu_utama():
    while True:
        print("\n" + "=" * 50)
        print("SISTEM MANAJEMEN NILAI MAHASISWA")
        print("=" * 50)
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Data Mahasiswa")
        print("3. Hapus Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Keluar")
Alur Eksekusi:
Infinite Loop: while True untuk menjaga program tetap berjalan
```
Switch Case Manual:

```
if pilihan == '1':
    tambah()
elif pilihan == '2':
    tampilkan()
Validasi untuk Menu 3 & 4:

python
if data_mahasiswa:
    tampilkan()  # Tampilkan data dulu
    nama = input("\nMasukkan nama mahasiswa yang akan dihapus: ")
    hapus(nama)
else:
    print("Belum ada data mahasiswa.")
Cek apakah ada data sebelum operasi hapus/ubah
```
Tampilkan data terlebih dahulu untuk referensi user

7. Fungsi data_contoh() & Main Block
```
def data_contoh():
    data_mahasiswa.extend([
        {'nama': 'Budi Santoso', 'nilai': 85.5},
        {'nama': 'Siti Aminah', 'nilai': 92.0},
        {'nama': 'Ahmad Rizki', 'nilai': 78.5}
    ])

if __name__ == "__main__":
    tambah_contoh = input("Tambahkan data contoh? (y/n): ").lower()
    if tambah_contoh == 'y':
        data_contoh()
    menu_utama()
```
Konsep Penting:
```
if __name__ == "__main__": Memastikan code hanya dijalankan ketika file dieksekusi langsung, bukan ketika diimport

User Choice: Memberi opsi untuk menambah data contoh atau tidak
```
8. Fitur Keamanan & User Experience
Error Handling:
```
Input Nilai: float(input(...)) - otomatis konversi ke numeric

Case-Insensitive: .lower() untuk konsistensi pencarian

Empty Data Check: if not data_mahasiswa untuk handling data kosong

User Feedback:
Pesan sukses: "Data berhasil ditambahkan!"

Pesan error: "Data tidak ditemukan!"

Konfirmasi: Menampilkan data sebelum hapus/ubah
````
9. Kelebihan Program

Modular: Setiap fungsi memiliki satu tanggung jawab

User-Friendly: Interface yang jelas dan petunjuk step-by-step

Robust: Handling berbagai edge cases (data kosong, duplikasi, dll)

Extensible: Mudah ditambah fitur baru (sorting, filtering, dll)

10. Contoh Output
```text
==================================================
SISTEM MANAJEMEN NILAI MAHASISWA
==================================================
1. Tambah Data Mahasiswa
2. Tampilkan Data Mahasiswa
3. Hapus Data Mahasiswa
4. Ubah Data Mahasiswa
5. Keluar
--------------------------------------------------
Pilih menu (1-5): 2

=== DAFTAR NILAI MAHASISWA ===
----------------------------------------
No.  Nama                 Nilai     
----------------------------------------
1    Budi Santoso         85.50     
2    Siti Aminah          92.00     
3    Ahmad Rizki          78.50     
----------------------------------------
Total mahasiswa: 3
