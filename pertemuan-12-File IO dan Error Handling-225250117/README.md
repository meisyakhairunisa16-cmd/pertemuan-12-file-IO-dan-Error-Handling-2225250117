# Pertemuan 12 - File I/O dan Error Handling

Nama: meisya khairunisha priatna
NIM: 2225250117
Kelas: 3F

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file
menggunakan Python.

## Format File Input
File nilai.txt menggunakan format:

NIM,nilai

Contoh:
A001,85
A002,78

## Cara Menjalankan
Jalankan perintah berikut dari root folder proyek:

python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
python tugas/rekap_nilai_file.py

## Error yang Ditangani
- FileNotFoundError
- ValueError

## Test Case

| Kasus | Hasil yang Diharapkan |
|---|---|
| Semua data valid | Seluruh data diproses |
| File tidak ditemukan | Program menampilkan pesan error |
| Nilai tidak valid | Baris dilewati |
| Baris kosong | Baris dilewati |
| Nilai 60 | Dihitung sebagai lulus |

## Refleksi
Program dapat membaca dan mengolah data dari file.
FileNotFoundError ditangani ketika file tidak ditemukan,
sedangkan ValueError ditangani ketika format data tidak valid.
Data yang valid tetap diproses meskipun terdapat baris
yang mengalami kesalahan.