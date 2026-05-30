# Modul 9: File I/O (Baca & Tulis File)

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Membaca isi file teks dengan Python
- Menulis data ke file
- Menggunakan `with` statement untuk manajemen file otomatis
- Membaca dan memproses file CSV (nilai siswa!)
- Membuat program yang menyimpan data

---

## 1. Membuka File

Untuk bekerja dengan file, kita perlu **membuka** file terlebih dahulu.

```python
# Sintaks: open(nama_file, mode)
file = open("data.txt", "r")  # "r" = read mode
isi = file.read()
print(isi)
file.close()  # ⚠️ Jangan lupa tutup!
```

### Mode File

| Mode | Arti | File Tidak Ada |
|------|------|----------------|
| `"r"` | Read (baca) | ❌ Error |
| `"w"` | Write (tulis) — **timpa** isi lama | ✅ Buat baru |
| `"a"` | Append (tambah ke akhir) | ✅ Buat baru |
| `"x"` | Exclusive create (buat baru) | ✅ Buat baru, error kalau sudah ada |
| `"r+"` | Read & Write | ❌ Error |

File bisa teks (default) atau binary (tambah `"b"`, misal `"rb"`).

> ⚠️ **`"w"` akan MENIMPA file yang sudah ada!** Hati-hati.

## 2. With Statement — Cara Aman untuk File

Masalah dengan `open()` manual: kita bisa lupa `close()`. Solusi: `with` statement, yang **otomatis menutup file** setelah selesai.

```python
# ← REKOMENDASI: selalu pakai 'with'
with open("data.txt", "r") as file:
    isi = file.read()
    print(isi)
# File otomatis tertutup di sini
```

> 💡 **`with` adalah cara standar Python untuk bekerja dengan file.** Selalu pakai ini.

## 3. Membaca File (Read)

### Membaca Semua Isi

```python
# Buat dulu file contoh
with open("contoh.txt", "w") as f:
    f.write("Baris 1: Nama, Nilai\n")
    f.write("Baris 2: Budi, 85\n")
    f.write("Baris 3: Ani, 92\n")

# Baca semua
with open("contoh.txt", "r") as f:
    isi = f.read()
    print(isi)
# Output:
# Baris 1: Nama, Nilai
# Baris 2: Budi, 85
# Baris 3: Ani, 92
```

### Membaca Per Baris

```python
# Cara 1: readlines() → list baris
with open("contoh.txt", "r") as f:
    baris_list = f.readlines()
    print(baris_list)   # ['Baris 1: Nama, Nilai\n', 'Baris 2: Budi, 85\n', ...]

# Cara 2: loop langsung 🔥 (paling efisien untuk file besar)
with open("contoh.txt", "r") as f:
    for baris in f:
        print(f"> {baris.strip()}")  # strip() hapus \n
```

### Membaca Sebagian

```python
with open("contoh.txt", "r") as f:
    print(f.read(10))    # Baca 10 karakter pertama
    print(f.read(10))    # Baca 10 berikutnya (cursor otomatis maju)
```

## 4. Menulis File (Write)

### Menulis — Menimpa

```python
with open("output.txt", "w") as f:
    f.write("Halo, ini ditulis oleh Python!\n")
    f.write("Baris kedua.\n")
    f.write(f"Angka: {42}\n")
# File akan dibuat (atau ditimpa kalau sudah ada)
```

### Append — Menambah

```python
with open("output.txt", "a") as f:
    f.write("Baris tambahan di akhir.\n")
    f.write("Ini tidak menghapus isi sebelumnya.\n")
```

## 5. Bekerja dengan Path File

```python
import os

# Cek apakah file ada
if os.path.exists("data.txt"):
    print("File ada!")
else:
    print("File tidak ada")

# Gabung path (aman untuk Linux/Windows)
path = os.path.join("folder", "subfolder", "data.txt")
print(path)  # folder/subfolder/data.txt

# Dapatkan direktori script saat ini
dir_sekarang = os.path.dirname(__file__)
```

> 💡 Di Omarchy Linux, path menggunakan `/` (forward slash). Contoh: `~/belajar-python/data/nilai.csv`

## 6. Membaca & Menulis CSV (Paling Berguna Buat Guru!)

CSV = **Comma-Separated Values**. Format file untuk data tabular. Sangat berguna untuk data nilai siswa.

### Tanpa Library CSV (Manual)

```python
# Data yang akan disimpan
data_nilai = [
    ["Nama", "MTK", "IPA", "ING"],
    ["Budi", 85, 90, 78],
    ["Ani", 92, 88, 95],
    ["Citra", 76, 80, 82]
]

# Menulis CSV manual
with open("nilai.csv", "w") as f:
    for baris in data_nilai:
        baris_str = [str(item) for item in baris]
        f.write(",".join(baris_str) + "\n")

print("File nilai.csv berhasil dibuat!")
```

```bash
# Isi file nilai.csv:
# Nama,MTK,IPA,ING
# Budi,85,90,78
# Ani,92,88,95
# Citra,76,80,82
```

```python
# Membaca CSV manual
with open("nilai.csv", "r") as f:
    for baris in f:
        # Hapus \n, pisah dengan koma
        kolom = baris.strip().split(",")
        print(kolom)
```

### Dengan Library CSV (Lebih Baik)

```python
import csv

# Membaca CSV
with open("nilai.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Baris pertama = header
    print(f"Header: {header}")
    
    for row in reader:
        nama = row[0]
        mtk = int(row[1])
        ipa = int(row[2])
        ing = int(row[3])
        rata = (mtk + ipa + ing) / 3
        print(f"{nama}: rata-rata {rata:.1f}")
```

```python
# Menulis CSV dengan library
import csv

data = [
    ["Nama", "MTK", "IPA", "ING"],
    ["Budi", 85, 90, 78],
    ["Ani", 92, 88, 95],
    ["Citra", 76, 80, 82]
]

with open("nilai_baru.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("File CSV berhasil ditulis!")
```

### Membaca CSV sebagai Dictionary

```python
import csv

with open("nilai.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # row adalah dictionary: {"Nama": "Budi", "MTK": "85", ...}
        nama = row["Nama"]
        mtk = int(row["MTK"])
        ipa = int(row["IPA"])
        ing = int(row["ING"])
        rata = (mtk + ipa + ing) / 3
        print(f"{nama}: {rata:.1f}")
```

## 7. JSON — Format Data Modern

JSON mirip dictionary Python. Sering dipakai untuk menyimpan data terstruktur.

```python
import json

# Data sebagai dictionary
data_kelas = {
    "kelas": "XII IPA 1",
    "tahun": 2026,
    "siswa": [
        {"nama": "Budi", "nilai": 85},
        {"nama": "Ani", "nilai": 92},
        {"nama": "Citra", "nilai": 78}
    ]
}

# Simpan ke JSON
with open("kelas.json", "w") as f:
    json.dump(data_kelas, f, indent=2)  # indent=2 biar rapi

# Baca dari JSON
with open("kelas.json", "r") as f:
    data_baca = json.load(f)
    print(f"Kelas: {data_baca['kelas']}")
    for s in data_baca['siswa']:
        print(f"  {s['nama']}: {s['nilai']}")
```

> 💡 JSON lebih disarankan daripada CSV untuk data kompleks (nested). Tapi CSV lebih universal untuk dibuka di Excel.

---

## 🧪 Latihan Modul 9

### Latihan 1: Catatan Harian

```python
# Program catatan harian sederhana:
# 1. Setiap kali dibuka, tampilkan isi catatan sebelumnya
# 2. Minta user menulis catatan baru (input)
# 3. Simpan catatan ke file (append)
# 4. Tampilkan semua catatan
# Gunakan file "catatan.txt"
```

### Latihan 2: Pengelola Nilai CSV

```python
# Buat sistem sederhana:
# 1. Input data siswa (nama, mtk, ipa, ing) → simpan ke CSV
# 2. Baca CSV → tampilkan laporan (nama + rata-rata)
# 3. Cari siswa berdasarkan nama → tampilkan detailnya
# 4. (Bonus) Hitung statistik kelas: rata-rata per mapel, tertinggi, terendah
```

### Latihan 3: JSON Buku Telepon

```python
# Buku telepon berbasis JSON:
# Data disimpan di "kontak.json"
# Menu:
# 1. Lihat semua kontak
# 2. Tambah kontak (nama, nomor, email)
# 3. Cari kontak
# 4. Hapus kontak
# 5. Keluar
# Data otomatis tersimpan di file
```

### Latihan 4: Membaca Nilai dari CSV + Analisis

```python
# Buat file "kelas_xii.csv" dengan data:
# Nama,MTK,IPA,ING,PPKn
# Budi,85,90,78,80
# Ani,92,88,95,85
# Citra,76,80,82,78
# Dedi,88,85,90,92
# Eva,95,92,88,90

# Program membaca CSV dan mencetak:
# 1. Daftar siswa + rata-rata masing-masing
# 2. Siswa dengan rata-rata tertinggi
# 3. Siswa yang lulus (rata-rata >= 75)
# 4. Ranking siswa berdasarkan rata-rata (urutan dari tertinggi)

# (Bonus) export ranking ke file "ranking.txt"
```

---

## ✅ Checklist Paham

- [ ] Saya bisa baca file teks dengan `with open()`
- [ ] Saya bisa tulis file dengan `"w"` dan `"a"`
- [ ] Saya paham beda `"r"`, `"w"`, `"a"`
- [ ] Saya bisa baca file per baris dengan loop
- [ ] Saya bisa baca dan tulis CSV (manual & library)
- [ ] Saya bisa baca dan tulis JSON
- [ ] Saya paham `with` otomatis menutup file

**Kalau semua checklist tercentang → lanjut ke Modul 10.**
