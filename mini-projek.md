# 🎯 Mini Projek untuk Murid (Per Level)

Projek-projek kecil yang bisa dikerjakan murid setelah menguasai modul tertentu.

---

## 🟢 Level Pemula (Modul 1-2)

### Projek 1: Kalkulator BMI

**Konsep:** Input, casting, operasi matematika, f-string  
**Prerequisite:** Modul 1

```python
# Spesifikasi:
# 1. Minta berat badan (kg)
# 2. Minta tinggi badan (cm → m: bagi 100)
# 3. Hitung BMI = berat / (tinggi ** 2)
# 4. Tampilkan BMI dengan 1 desimal
#
# Bonus: cari tahu kategori BMI-nya
# < 18.5: Kurang
# 18.5-24.9: Normal
# 25-29.9: Berlebih
# >= 30: Obesitas
```

### Projek 2: Pembalik Nama

**Konsep:** String, slicing, f-string  
**Prerequisite:** Modul 2

```python
# Input: "Budi Santoso"
# Output: "Santoso, Budi"
#
# Bonus: input 3 kata, output: "Kata3,Kata1,Kata2"
```

### Projek 3: Tabungan Harian

**Konsep:** Variabel, loop, akumulasi  
**Prerequisite:** Modul 1

```python
# Program tracking tabungan:
# 1. Minta target tabungan
# 2. Setiap hari minta jumlah yang ditabung
# 3. Tampilkan total dan sisa target
# 4. Berhenti kalau target tercapai
```

---

## 🟡 Level Dasar (Modul 3-5)

### Projek 4: Daftar Tugas (To-Do List Sederhana)

**Konsep:** List, append, loop, percabangan  
**Prerequisite:** Modul 3, 5

```python
# Program CLI dengan menu:
# 1. Tambah tugas
# 2. Lihat semua tugas (dengan nomor)
# 3. Hapus tugas (pilih nomor)
# 4. Tandai selesai
# 5. Keluar
#
# Data disimpan di list (sementara, belum ke file)
```

### Projek 5: Buku Telepon

**Konsep:** Dictionary, loop, percabangan  
**Prerequisite:** Modul 4, 5

```python
# Program buku telepon:
# 1. Tambah kontak (nama, nomor)
# 2. Cari kontak (berdasarkan nama)
# 3. Lihat semua kontak
# 4. Hapus kontak
# 5. Keluar
#
# Data disimpan di dictionary
```

### Projek 6: Game Tebak Angka

**Konsep:** While, random, break, percabangan  
**Prerequisite:** Modul 5, 6

```python
# 1. Komputer pilih angka acak 1-100
# 2. User menebak
# 3. Komputer kasih petunjuk "Terlalu besar/kecil"
# 4. Hitung jumlah tebakan
# 5. Kalau benar → "Selamat! Kamu menebak X kali"
# 6. Batas maksimal 7 tebakan
```

### Projek 7: Bataan Stok Barang

**Konsep:** Dictionary, loop, list  
**Prerequisite:** Modul 4, 5, 6

```python
# Program stok barang toko:
# 1. Tambah barang (nama, jumlah)
# 2. Lihat semua barang
# 3. Cari barang
# 4. Update stok (tambah/kurang)
# 5. Barang hampir habis (stok < 5)
# 6. Keluar
```

---

## 🟠 Level Madya (Modul 6-9)

### Projek 8: Quiz Interaktif

**Konsep:** Dictionary, loop, function, skor  
**Prerequisite:** Modul 4, 5, 6, 7

```python
# Quiz dengan 10 soal pilihan ganda:
soal = [
    {
        "soal": "Apa tipe data dari 3.14?",
        "opsi": ["a. int", "b. float", "c. str", "d. bool"],
        "jawaban": "b"
    },
    # ... tambahkan 9 soal lagi
]

# Fitur:
# - Tampilkan soal 1 per 1
# - Validasi input a/b/c/d
# - Hitung skor akhir
# - Tampilkan hasil: "Kamu benar 7 dari 10"
# - Tampilkan grade (A/B/C/D/E)
```

### Projek 9: Pengelola Nilai (CLI)

**Konsep:** Function, dictionary, loop, file I/O  
**Prerequisite:** Modul 7, 9

```python
# Program pengelola nilai siswa:
# Fungsi:
# 1. tambah_siswa(nama, kelas) → dict
# 2. tambah_nilai(siswa, mapel, nilai)
# 3. hitung_rata(siswa) → float
# 4. grade(siswa) → string
# 5. laporan(siswa) → cetak rapi
# 6. simpan(siswa_list, filename) → file JSON
# 7. muat(filename) → list siswa
#
# Menu utama interaktif
```

### Projek 10: Membaca & Menganalisis File Nilai CSV

**Konsep:** File I/O, CSV, analisis data  
**Prerequisite:** Modul 9

```python
# Baca file nilai_siswa.csv dengan format:
# Nama,MTK,IPA,ING,PPKn
# Budi,85,90,78,80
# ...

# Cetak:
# 1. Rata-rata setiap siswa
# 2. Ranking dari tertinggi ke terendah
# 3. Statistik: rata-rata kelas, nilai tertinggi, terendah
# 4. Jumlah siswa lulus (rata-rata >= 75)
# 5. Buat file ranking.txt berisi hasil ranking
```

### Projek 11: Enkripsi Sederhana (Caesar Cipher)

**Konsep:** String, loop, function, ord()/chr()  
**Prerequisite:** Modul 2, 6, 7

```python
# Caesar Cipher — geser huruf sesuai key
# enkripsi("abc", 1) → "bcd"
# dekripsi("bcd", 1) → "abc"
#
# Fitur:
# 1. Input pesan
# 2. Input key (angka geser)
# 3. Pilih enkripsi/dekripsi
# 4. Tampilkan hasil
# 5. Simpan ke file
```

---

## 🔴 Level Mahir (Modul 10-12)

### Projek 12: Web Scraper Berita

**Konsep:** pip, requests, BeautifulSoup, error handling  
**Prerequisite:** Modul 10

```python
# Install: pip install requests beautifulsoup4
#
# Ambil 5 berita terbaru dari situs berita
# Tampilkan: judul, tanggal, link
# Simpan ke file JSON
```

### Projek 13: Sistem Perpustakaan (OOP)

**Konsep:** OOP, class, method, file I/O  
**Prerequisite:** Modul 9, 12

```python
# Class Buku: judul, penulis, tahun, tersedia (bool)
# Class Anggota: nama, id, daftar pinjam
# Class Perpustakaan: daftar_buku, daftar_anggota
#
# Method:
# - tambah_buku()
# - cari_buku(judul)
# - pinjam_buku(id_anggota, judul)
# - kembalikan_buku(id_anggota, judul)
# - lihat_buku_tersedia()
# - simpan_data() / muat_data() → JSON
```

### Projek 14: Aplikasi Catatan dengan Tanggal

**Konsep:** datetime, file I/O, dictionary, sorting  
**Prerequisite:** Modul 9, 10

```python
# Aplikasi catatan harian:
# 1. Tambah catatan (otomatis timestamp)
# 2. Lihat semua catatan (urut tanggal)
# 3. Cari catatan (berdasarkan kata kunci)
# 4. Hapus catatan
# 5. Export ke file .txt
# 6. Simpan/muat dari JSON

from datetime import datetime
```

---

## 🏆 Level Expert (Full Stack)

### Projek 15: Web App Nilai dengan Flask

**Prerequisite:** Modul 10, 12

```bash
pip install flask
```

```python
# Ubah proyek Modul 13 jadi web app:
# - Flask route untuk setiap fitur
# - HTML template untuk tampilan
# - Form input nilai
# - Tabel ranking
# - Grafik (pakai matplotlib atau chart.js)
```

### Projek 16: Database dengan SQLite

**Prerequisite:** Modul 9, 10, 12

```python
import sqlite3
# Ganti penyimpanan JSON ke SQLite
# Buat tabel: siswa, nilai, mapel
# Query: JOIN, ORDER BY, GROUP BY
```

---

## 📋 Tabel Projek & Tingkat Kesulitan

| # | Projek | Level | Modul | Perkiraan Jam |
|---|--------|-------|-------|---------------|
| 1 | Kalkulator BMI | 🟢 Pemula | 1 | 1 JP |
| 2 | Pembalik Nama | 🟢 Pemula | 2 | 1 JP |
| 3 | Tabungan Harian | 🟢 Pemula | 1 | 1 JP |
| 4 | To-Do List | 🟡 Dasar | 3, 5 | 2 JP |
| 5 | Buku Telepon | 🟡 Dasar | 4, 5 | 1 JP |
| 6 | Tebak Angka | 🟡 Dasar | 5, 6 | 2 JP |
| 7 | Stok Barang | 🟡 Dasar | 4, 5, 6 | 2 JP |
| 8 | Quiz Interaktif | 🟠 Madya | 7 | 2 JP |
| 9 | Pengelola Nilai | 🟠 Madya | 7, 9 | 3 JP |
| 10 | Analisis CSV | 🟠 Madya | 9 | 2 JP |
| 11 | Caesar Cipher | 🟠 Madya | 2, 6, 7 | 1 JP |
| 12 | Web Scraper | 🔴 Mahir | 10 | 2 JP |
| 13 | Sistem Perpus | 🔴 Mahir | 12 | 3 JP |
| 14 | Catatan + Tgl | 🔴 Mahir | 9, 10 | 2 JP |
| 15 | Flask Web App | 🏆 Expert | Flask | 4 JP |
| 16 | SQLite DB | 🏆 Expert | sqlite3 | 3 JP |

---

## 💡 Tips Assign Projek ke Murid

1. **1 projek per 2-3 minggu** — jangan tiap minggu
2. **Berikan template kode awal** — jangan suruh mulai dari 0 terus
3. **Kriteria penilaian:**
   - Program jalan (tidak error) — 40%
   - Fitur sesuai spesifikasi — 40%
   - Kode rapi (indentasi, nama variabel jelas) — 20%
4. **Pair programming** — 2 murid 1 komputer, bergantian ngetik
5. **Presentasi** — minta murid demo hasilnya di depan kelas
6. **Bonus challenge** di setiap projek untuk murid yang cepat selesai
