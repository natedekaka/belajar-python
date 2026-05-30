# Modul 1: Variabel & Tipe Data

## 🏆 Target Pemahaman (Buat Ngajar)

Setelah modul ini, kamu bisa:
- Menjelaskan apa itu **variabel** ke murid
- Membedakan 4 tipe data dasar: `int`, `float`, `str`, `bool`
- Menjelaskan perbedaan `int` vs `float` — kenapa ada dua jenis angka?
- Menggunakan `type()` untuk cek tipe data
- Melakukan operasi matematika dasar
- Konversi tipe data (casting)

---

## 1. Apa Itu Variabel?

Variabel = **kotak penyimpanan** yang punya nama. Kita taruh data di dalamnya, lalu panggil namanya kapan saja.

```python
# Sintaks: nama_variabel = nilai
nama = "Budi"       # String (teks)
usia = 16           # Integer (angka bulat)
tinggi = 165.5      # Float (angka desimal)
siswa_aktif = True  # Boolean (True/False)

print(nama)   # Output: Budi
print(usia)   # Output: 16
```

> 💡 Di Python, kita **tidak perlu** mendeklarasikan tipe data. Python otomatis tahu.

### Aturan Penamaan Variabel

| ✅ Boleh | ❌ Tidak Boleh |
|----------|---------------|
| `nama_siswa` | `nama-siswa` (strip) |
| `data2` | `2data` (angka di depan) |
| `_private` | `class` (keyword Python) |
| `nilaiAkhir` | `nilai akhir` (spasi) |

> 💡 **Konvensi Python:** pakai `snake_case` — huruf kecil dengan underscore. Contoh: `rata_rata`, `jumlah_siswa`.

## 2. Tipe Data Dasar

Python punya 4 tipe data dasar yang wajib dikuasai:

### int (Integer) — Bilangan Bulat

```python
umur = 17
tahun = 2026
negatif = -5
nol = 0

print(type(umur))   # <class 'int'>
```

### float (Floating Point) — Bilangan Desimal

```python
phi = 3.14
suhu = -2.5
berat = 55.0       # tetap float walau .0

print(type(phi))    # <class 'float'>
```

> ⚠️ **Jebakan umum murid:** `5` adalah `int`, tapi `5.0` adalah `float`. Di Python, mereka beda tipe.

### str (String) — Teks

```python
nama = "Budi"
kelas = 'XII IPA 1'            # pakai kutip 1 atau 2, sama saja
pesan = "Dia berkata: 'Halo'"  # kutip di dalam kutip

# Multiline string (3 kutip)
puisi = """Belajar Python
Sangat menyenangkan
Bikin ketagihan"""

print(type(nama))   # <class 'str'>
```

### bool (Boolean) — True/False

```python
lulus = True
gagal = False

print(type(lulus))  # <class 'bool'>
```

> 💡 `True` dan `False` **wajib** huruf besar diawali. `true` atau `false` (kecil) akan error.

## 3. Operasi Matematika pada Angka

```python
a = 10
b = 3

print(a + b)    # 13   — Penjumlahan
print(a - b)    # 7    — Pengurangan
print(a * b)    # 30   — Perkalian
print(a / b)    # 3.33 — Pembagian (hasil selalu float)
print(a // b)   # 3    — Pembagian bulat (integer division)
print(a % b)    # 1    — Sisa bagi (modulus)
print(a ** b)   # 1000 — Pangkat (10^3)
```

> ⚠️ **Ini penting buat ngajar:** `a / b` vs `a // b` — murid sering bingung.
> - `/` = hasil desimal (float)
> - `//` = hasil dibulatkan ke bawah (integer)

### Prioritas Operasi (mirip matematika)

Ingat **KABATAKU** (Kurung, Akar, Bagi, Kali, Tambah, Kurang):

```python
hasil = 5 + 3 * 2      # 11 (bukan 16!)
# Karena perkalian duluan: 3*2=6, 5+6=11

hasil2 = (5 + 3) * 2   # 16 — kurung diutamakan
```

## 4. Operasi pada String

```python
# Gabung string (concatenation)
nama_depan = "Budi"
nama_belakang = "Santoso"
nama_lengkap = nama_depan + " " + nama_belakang
print(nama_lengkap)   # Budi Santoso

# Mengulang string
teriak = "A" * 10
print(teriak)   # AAAAAAAAAA

# Menggabung string dengan angka — ERROR kalau beda tipe!
# print("Umur: " + 17)  # ❌ TypeError!
print("Umur: " + str(17))  # ✅ Harus di-cast dulu

# Cara modern: f-string 👈 INI FAVORIT
nama = "Budi"
umur = 17
print(f"Nama saya {nama}, umur {umur} tahun")
# Output: Nama saya Budi, umur 17 tahun
```

> 💡 **f-string** (`f"..."`) adalah cara terbaik menggabung teks dan variabel di Python modern. Gunakan ini, tinggalkan concatenation pakai `+`.

## 5. Operasi Boolean

```python
print(True and True)    # True
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

Akan kita pelajari lebih dalam di Modul 5 (Percabangan).

## 6. Konversi Tipe Data (Casting)

Kadang kita perlu mengubah tipe data:

```python
# String → Angka
umur_str = "17"
umur_int = int(umur_str)     # 17 (int)
tinggi_str = "165.5"
tinggi_float = float(tinggi_str)  # 165.5 (float)

# Angka → String
nilai = 90
laporan = "Nilai: " + str(nilai)

# Float → Integer (kehilangan desimal!)
pi = 3.14
pi_int = int(pi)
print(pi_int)  # 3 (dipotong, bukan dibulatkan)
```

> ⚠️ **Error umum:** `int("17.5")` akan error karena "17.5" bukan format integer. Harus `float("17.5")` dulu baru di-`int()`.

### Fungsi `type()` — Cek Tipe Data

```python
x = 5
print(type(x))       # <class 'int'>

y = "Hello"
print(type(y))       # <class 'str'>

z = 5.0
print(type(z))       # <class 'float'>
```

Berguna banget buat debugging dan buat ngajar — "loh, ini tipe datanya apa sih?"

## 7. Input dari Keyboard

```python
# input() SELALU mengembalikan string
nama = input("Masukkan nama: ")
print(f"Halo {nama}!")

# Kalau mau angka, harus di-cast
umur = int(input("Masukkan umur: "))
print(f"Tahun depan kamu berusia {umur + 1} tahun")
```

> ⚠️ **Peringatan:** `input("...")` selalu return `str`. Kalau kamu mau angka, jangan lupa `int()` atau `float()`.

---

## 🧪 Latihan Modul 1

### Latihan 1: Perkenalan Diri

```python
# Buat program yang:
# 1. Minta nama user
# 2. Minta umur user
# 3. Minta kota tinggal
# 4. Cetak: "Halo [nama], umur [umur] tahun, dari [kota]"
```

### Latihan 2: Kalkulator Sederhana

```python
# Buat program yang:
# 1. Minta dua angka dari user
# 2. Tampilkan: jumlah, selisih, kali, bagi, sisa bagi
# Contoh output:
#   Angka 1: 10
#   Angka 2: 3
#   10 + 3 = 13
#   10 - 3 = 7
#   ...
```

### Latihan 3: Konversi Suhu

```python
# Buat program yang:
# 1. Minta suhu dalam Celcius
# 2. Tampilkan dalam Fahrenheit: (C * 9/5) + 32
```

### Latihan 4 (Bonus — konsep yang sering ditanyakan murid)

Jalankan kode berikut di REPL, tebak outputnya dulu sebelum enter:

```python
print(type(3.0))
print(type(3))
print(10 / 4)
print(10 // 4)
print(int(3.999))
```

---

## 📝 Ringkasan Buat Ngajar

Kalau kamu jelasin ke murid, sampaikan ini:

> **Variabel** itu seperti **kotak yang kita kasih label**. Kita bisa taruh angka, teks, atau data lain di dalamnya. Python pinter — dia otomatis tahu jenis data yang kita taruh. Makanya kita tinggal tulis `nama = "Budi"` tanpa bilang "ini string ya".

Empat tipe data dasar:
1. **int** — bilangan bulat (3, -10, 1000)
2. **float** — bilangan desimal (3.14, -0.5)
3. **str** — teks ("Halo", "XII IPA 1")
4. **bool** — True/False

## ✅ Checklist Paham

- [ ] Saya bisa bedain `int`, `float`, `str`, `bool`
- [ ] Saya bisa pake f-string (`f"..."`)
- [ ] Saya paham perbedaan `/` dan `//`
- [ ] Saya bisa nulis input dan cast ke tipe yang benar
- [ ] Saya bisa cek tipe data pake `type()`
- [ ] Saya tau cara penulisan variabel yang benar (`snake_case`)

**Kalau semua checklist tercentang → lanjut ke Modul 2.**
