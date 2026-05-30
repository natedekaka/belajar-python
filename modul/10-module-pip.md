# Modul 10: Module, Package & pip

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Mengimpor modul bawaan Python (`import`)
- Membuat modul sendiri
- Menginstall package dengan `pip`
- Menggunakan virtual environment dengan benar
- Memahami struktur package Python

---

## 1. Apa Itu Module?

Module = file `.py` yang berisi kode Python (fungsi, class, variabel) yang bisa dipakai di file lain.

**Kenapa perlu module?**
- **Organisasi** — kode terpisah per fungsi
- **Reusable** — tulis sekali, impor di mana saja
- **Namespace** — tidak tabrakan nama

## 2. Import Modul Bawaan

Python punya **banyak modul bawaan** (standard library). Tidak perlu install.

```python
# Cara 1: Import seluruh modul
import math
print(math.pi)           # 3.141592653589793
print(math.sqrt(16))     # 4.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4

# Cara 2: Import spesifik
from math import pi, sqrt
print(pi)                # 3.141592653589793
print(sqrt(25))          # 5.0

# Cara 3: Alias
import math as m
print(m.sin(0))          # 0.0

# Cara 4: Import semua (⚠️ hati-hati, bisa tabrakan nama)
from math import *       # Tidak disarankan untuk modul besar
```

### Modul Bawaan yang Sering Dipakai

```python
# random — angka acak 🔥
import random
print(random.randint(1, 10))     # Angka acak 1-10
print(random.choice(["Budi", "Ani", "Citra"]))  # Pilih acak
print(random.shuffle([1,2,3,4])) # Acak urutan

# os — sistem operasi
import os
print(os.getcwd())       # Direktori saat ini
print(os.listdir("."))   # Daftar file di folder
os.mkdir("folder_baru")  # Buat folder

# datetime — tanggal dan waktu
from datetime import datetime
sekarang = datetime.now()
print(sekarang)                    # 2026-05-10 14:30:00
print(sekarang.strftime("%A, %d %B %Y"))  # Sunday, 10 May 2026

# time — delay
import time
print("Mulai...")
time.sleep(2)            # Tunggu 2 detik
print("Selesai!")

# sys — informasi sistem
import sys
print(sys.version)       # Versi Python
print(sys.argv)          # Argumen command line

# json — baca/tulis JSON (sudah di Modul 9)
import json

# csv — baca/tulis CSV (sudah di Modul 9)
import csv
```

> 💡 **Standard Library Python itu luas.** Sebelum install package pihak ketiga, cek dulu apakah sudah ada di standard library.

### Cek Modul Bawaan

```bash
# Di terminal
python -m pydoc math  # Dokumentasi modul math
python -m pydoc list  # Dokumentasi method list
```

## 3. Membuat Modul Sendiri

Ini yang bikin Python powerful — kita bisa bikin modul sendiri.

### Langkah 1: Buat file module

Buat file `utils_sekolah.py`:

```python
"""Modul utilitas untuk keperluan sekolah"""

def hitung_rata(daftar_nilai):
    """Hitung rata-rata dari list nilai"""
    if not daftar_nilai:
        return 0
    return sum(daftar_nilai) / len(daftar_nilai)

def grade(nilai):
    """Konversi nilai ke grade A/B/C/D/E"""
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

def lulus(nilai):
    """Cek apakah lulus (nilai >= 75)"""
    return nilai >= 75

# Variabel
NAMA_SEKOLAH = "SMA Negeri 1"
KEPALA_SEKOLAH = "Dr. H. Ahmad, M.Pd."
```

### Langkah 2: Import dan pakai

Buat file `main.py` di **folder yang sama**:

```python
import utils_sekolah as us

# Pake fungsi
nilai_budi = [85, 90, 78, 80, 92]
rata = us.hitung_rata(nilai_budi)
print(f"Rata-rata Budi: {rata}")
print(f"Grade: {us.grade(rata)}")
print(f"Lulus: {us.lulus(rata)}")

# Pake variabel
print(f"Sekolah: {us.NAMA_SEKOLAH}")
```

```bash
python main.py
# Output:
# Rata-rata Budi: 85.0
# Grade: B
# Lulus: True
# Sekolah: SMA Negeri 1
```

### __name__ == "__main__" — Proteksi untuk Module

Kadang kita mau kode di module hanya jalan kalau dijalankan langsung, bukan ketika di-import.

```python
# utils_sekolah.py
def hitung_rata(daftar):
    return sum(daftar) / len(daftar)

# Kode ini hanya jalan kalau file ini di-RUN langsung
if __name__ == "__main__":
    # Test module
    print("Testing utils_sekolah...")
    print(hitung_rata([1, 2, 3, 4, 5]))
```

```python
# main.py — import module
import utils_sekolah

# Saat import, kode di bawah if __name__ TIDAK jalan
print(utils_sekolah.hitung_rata([10, 20, 30]))
```

```bash
# Kalau jalanin utils_sekolah.py langsung:
python utils_sekolah.py
# Output: Testing utils_sekolah... 3.0

# Kalau jalanin main.py:
python main.py
# Output: 20.0 (kode test di module tidak ikut jalan)
```

> 💡 **Pola `if __name__ == "__main__"`** sangat penting. Pakai selalu untuk kode test di module.

## 4. Package — Kumpulan Module

Package = folder yang berisi kumpulan module, ditandai dengan file `__init__.py`.

```
sekolah_package/          ← Package (folder)
├── __init__.py           ← Wajib (bisa kosong) — menandakan folder ini package
├── siswa.py              ← Module
├── guru.py               ← Module
└── nilai.py              ← Module
```

```python
# __init__.py — bisa dikosongkan, atau diisi import
```

```python
# siswa.py
def daftar_siswa():
    return ["Budi", "Ani", "Citra"]
```

```python
# main.py
from sekolah_package import siswa
print(siswa.daftar_siswa())
```

> 💡 Untuk sekarang, cukup pahami konsepnya. Package berguna untuk project besar.

## 5. pip — Package Installer

`pip` adalah tools untuk menginstall **package pihak ketiga**.

```bash
# Cek pip
pip --version

# Install package
pip install requests

# Install versi tertentu
pip install pandas==2.0.0

# Install dari requirements file
pip install -r requirements.txt

# Lihat package terinstall
pip list

# Info package
pip show requests

# Hapus package
pip uninstall requests
```

### Package Pihak Ketiga yang Berguna untuk Guru

```python
# requests — ambil data dari internet
import requests
response = requests.get("https://api.contoh.com/data")
data = response.json()

# beautifulsoup4 — scraping web (parse HTML)
from bs4 import BeautifulSoup

# pandas — analisis data (seperti Excel di Python)
import pandas as pd
df = pd.read_csv("nilai.csv")
print(df.describe())  # Statistik otomatis!

# matplotlib — bikin grafik
import matplotlib.pyplot as plt
plt.bar(["Budi", "Ani"], [85, 92])
plt.show()  # Muncul grafik

# flask — bikin web app
from flask import Flask
```

> 💡 **Ingat:** Install package di dalam **virtual environment**, jangan global!

## 6. Requirements File

Biasanya project Python punya file `requirements.txt` yang berisi daftar dependency:

```txt
requests==2.31.0
pandas>=2.0.0
matplotlib>=3.5.0
flask>=2.3.0
```

```bash
pip install -r requirements.txt  # Install semua sekaligus
```

---

## 🧪 Latihan Modul 10

### Latihan 1: Bikin Module Sendiri

```python
# Buat file "alat_math.py" dengan fungsi-fungsi:
# - tambah(a, b)
# - kurang(a, b) 
# - kali(a, b)
# - bagi(a, b) — handle ZeroDivisionError
# - pangkat(a, b)
# - faktorial(n) — loop saja
# - apakah_prima(n) — True/False
#
# Di dalam `if __name__ == "__main__":`, test fungsi-fungsi tersebut.
#
# Lalu buat "main.py" yang import dan pake module tersebut.
```

### Latihan 2: Generator Soal Matematika

```python
# Buat module "soal_matematika.py" yang:
# - generate_soal_tambah() → return (soal_str, jawaban)
# - generate_soal_kali() → return (soal_str, jawaban)
# - kuis( jumlah=5 ) → jalanin kuis interaktif
#
# Pakai random.randint() untuk generate angka.
# main.py: panggil fungsi kuis(10) untuk kuis 10 soal.
```

### Latihan 3: Gunakan pip

```bash
# 1. Aktifkan virtual environment
source ~/belajar-python/.venv/bin/activate

# 2. Install requests
pip install requests

# 3. Buat program yang ambil data dari API publik
# Contoh: https://api.publicapis.org/entries
# Tampilkan 5 API random
```

### Latihan 4: Bikin requirements.txt

```bash
# 1. Cek package terinstall: pip list
# 2. Simpan ke file: pip freeze > requirements.txt
# 3. Baca isi requirements.txt
# 4. Buat venv baru, install dari file: pip install -r requirements.txt
```

---

## ✅ Checklist Paham

- [ ] Saya bisa `import` modul bawaan Python
- [ ] Saya tau cara `from ... import ...` dan `import ... as ...`
- [ ] Saya bisa bikin modul sendiri (file .py)
- [ ] Saya paham `if __name__ == "__main__"`
- [ ] Saya paham konsep package (folder + `__init__.py`)
- [ ] Saya bisa install package dengan `pip`
- [ ] Saya selalu install package di dalam venv

**Kalau semua checklist tercentang → lanjut ke Modul 11.**
