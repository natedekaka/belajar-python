# Modul 6: Perulangan (Loop)

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menggunakan `for` loop untuk iterasi data
- Menggunakan `while` loop untuk kondisi berulang
- Membedakan kapan pakai `for` vs `while`
- Mengontrol loop dengan `break`, `continue`, `else`
- Membuat nested loop

---

## 1. For Loop — Iterasi Koleksi Data

`for` loop digunakan untuk **melewati setiap item** dalam suatu koleksi (list, string, tuple, dictionary, range, dll).

```python
# Loop list
siswa = ["Budi", "Ani", "Citra"]
for s in siswa:
    print(f"Halo {s}!")
# Output:
# Halo Budi!
# Halo Ani!
# Halo Citra!
```

```python
# Loop string (setiap karakter)
for c in "Python":
    print(c, end="-")
# Output: P-y-t-h-o-n-
```

```python
# Loop dictionary
nilai = {"Budi": 85, "Ani": 92, "Citra": 78}
for nama, n in nilai.items():
    print(f"{nama}: {n}")
```

### Range — Loop dengan Angka

`range()` adalah fungsi yang menghasilkan urutan angka. Sangat berguna.

```python
# range(stop) → 0 sampai stop-1
for i in range(5):
    print(i)   # 0, 1, 2, 3, 4

# range(start, stop) → start sampai stop-1
for i in range(3, 7):
    print(i)   # 3, 4, 5, 6

# range(start, stop, step) → dengan langkah
for i in range(0, 10, 2):
    print(i)   # 0, 2, 4, 6, 8

for i in range(10, 0, -2):
    print(i)   # 10, 8, 6, 4, 2
```

### Loop dengan Index (Enumerate)

```python
siswa = ["Budi", "Ani", "Citra"]

# Cara tidak Pythonic:
for i in range(len(siswa)):
    print(f"{i+1}. {siswa[i]}")

# Cara Pythonic dengan enumerate 🔥
for i, s in enumerate(siswa):
    print(f"{i+1}. {s}")
# Output:
# 1. Budi
# 2. Ani
# 3. Citra
```

## 2. While Loop — Loop Bersyarat

`while` loop berjalan **selama kondisi masih True**.

```python
# Hitung mundur
hitungan = 5
while hitungan > 0:
    print(f"{hitungan}...")
    hitungan -= 1  # Jangan lupa kurangi! Kalau lupa, loop forever
print("Go! 🚀")
```

### Infinite Loop — Bahaya!

```python
# ⚠️ INI BERBAHAYA — loop tidak akan pernah berhenti
# x = 1
# while x > 0:
#     print("Forever...")

# Cara aman: pastikan ada sesuatu yang mengubah kondisi
x = 1
while x > 0:
    print(x)
    x += 1
    if x >= 10:   # Safety break
        break
```

> 💡 Di Omarchy Linux, kalau kejebak infinite loop: tekan `Ctrl+C` untuk menghentikan.

### Kapan For vs While?

| For Loop | While Loop |
|----------|------------|
| Jumlah iterasi **sudah diketahui** | Jumlah iterasi **tidak pasti** |
| Iterasi data (list, range) | Loop sampai kondisi terpenuhi |
| Proses setiap item dalam koleksi | Validasi input sampai benar |
| Contoh: cetak semua nilai siswa | Contoh: ulang minta password sampai benar |

```python
# FOR — kita tau persis jumlah siswa
siswa = ["Budi", "Ani", "Citra"]
for s in siswa:
    print(s)

# WHILE — kita tidak tau kapan user akan jawab benar
tebak = ""
while tebak != "python":
    tebak = input("Tebak kata rahasia: ")
    if tebak != "python":
        print("Salah, coba lagi!")
print("Benar! 🎉")
```

## 3. Break — Hentikan Loop

`break` menghentikan loop **sepenuhnya**:

```python
# Cari angka pertama yang habis dibagi 7
for i in range(1, 100):
    if i % 7 == 0:
        print(f"Ketemu: {i}")
        break   # Berhenti setelah ketemu
# Output: Ketemu: 7
```

```python
# Validasi input — repeat sampai benar
while True:  # Loop "forever" — tapi akan di-break
    password = input("Masukkan password (min 6 karakter): ")
    if len(password) >= 6:
        print("Password diterima ✅")
        break
    print("Terlalu pendek, coba lagi!")
```

## 4. Continue — Lompat ke Iterasi Berikutnya

`continue` **melewati** sisa kode di iterasi saat ini dan lanjut ke iterasi berikutnya:

```python
# Cetak angka 1-10, skip yang genap
for i in range(1, 11):
    if i % 2 == 0:
        continue   # Skip genap
    print(i)
# Output: 1, 3, 5, 7, 9
```

```python
# Proses data — skip yang tidak valid
data = [85, -1, 92, 78, -5, 88, 100]
for nilai in data:
    if nilai < 0:
        continue   # Skip nilai negatif
    print(f"Nilai: {nilai}")
```

## 5. Else di Loop (Unique Python!)

Python punya fitur unik: **`else` di loop**. Blok `else` dijalankan kalau loop **selesai normal** (tidak di-break).

```python
# Cari angka prima
angka = 17

for i in range(2, angka):
    if angka % i == 0:
        print(f"{angka} bukan prima, habis dibagi {i}")
        break
else:  # Ini dijalankan kalau loop tidak di-break
    print(f"{angka} adalah bilangan prima ✅")
```

```python
# Cari item di list
keranjang = ["apel", "pisang", "jeruk", "anggur"]
cari = "mangga"

for item in keranjang:
    if item == cari:
        print(f"'{cari}' ditemukan!")
        break
else:
    print(f"'{cari}' tidak ada di keranjang")
```

> 🏆 **Poin ngajar:** "`else` di loop itu seperti 'kalau gak ada yang nge-break, jalankan ini'. Ini fitur unik Python, gak ada di bahasa lain."

## 6. Nested Loop (Loop di Dalam Loop)

```python
# Cetak tabel perkalian
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j:2d}", end="  ")
    print()  # Baris baru
# Output:
# 1x1= 1  1x2= 2  1x3= 3
# 2x1= 2  2x2= 4  2x3= 6
# 3x1= 3  3x2= 6  3x3= 9
```

```python
# Cetak pola segitiga
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# Output:
# *
# **
# ***
# ****
# *****
```

```python
# Nested loop dengan nested list
nilai_siswa = [
    ["Budi", 85, 90, 78],
    ["Ani", 92, 88, 95],
    ["Citra", 76, 80, 82]
]

for siswa in nilai_siswa:
    nama = siswa[0]
    nilai = siswa[1:]
    total = sum(nilai)
    rata = total / len(nilai)
    print(f"{nama}: rata-rata {rata:.1f}")
```

## 7. List Comprehension — Loop Singkat (Preview)

Ini fitur Python yang sangat populer. Akan dibahas detail di Modul 11.

```python
# Buat list dari loop (cara biasa)
kuadrat = []
for i in range(10):
    kuadrat.append(i**2)
print(kuadrat)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Cara list comprehension (jauh lebih singkat)
kuadrat2 = [i**2 for i in range(10)]
print(kuadrat2)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

## 🧪 Latihan Modul 6

### Latihan 1: Deret Angka

```python
# Cetak deret berikut menggunakan loop:
# 1. 1, 2, 3, 4, ..., 20
# 2. 2, 4, 6, 8, ..., 20
# 3. 10, 9, 8, 7, ..., 1
# 4. 1, 4, 9, 16, 25, ..., 100 (bilangan kuadrat)
```

### Latihan 2: FizzBuzz

```python
# Cetak angka 1-50
# Kelipatan 3 → "Fizz"
# Kelipatan 5 → "Buzz"
# Kelipatan 3 dan 5 → "FizzBuzz"
# Selainnya → angka
# Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, ...
```

### Latihan 3: Game Tebak Angka

```python
# Program:
# 1. Pilih angka acak 1-50 (import random; angka = random.randint(1, 50))
# 2. User menebak
# 3. Kalau terlalu besar → "Terlalu besar!"
# 4. Kalau terlalu kecil → "Terlalu kecil!"
# 5. Kalau benar → "Benar!" + tampilkan jumlah tebakan
# 6. Batas maksimal 7 tebakan
# Hint: pake while loop
```

### Latihan 4: Pola Bintang

```python
# Minta input tinggi segitiga
# Cetak:
# *
# **
# ***
# ****
# *****
# (segitiga siku-siku)
#
# Kemudian cetak versi terbalik:
# *****
# ****
# ***
# **
# *
```

### Latihan 5: Password Checker

```python
# Program yang terus meminta password sampai memenuhi syarat:
# - Minimal 8 karakter
# - Mengandung huruf besar
# - Mengandung angka
# - Kalau semua terpenuhi, "Password kuat ✅" dan program selesai
# Tampilkan petunjuk yang hilang setiap kali salah
```

---

## ✅ Checklist Paham

- [ ] Saya bisa pake `for` untuk loop data dan range
- [ ] Saya paham cara kerja `while` loop
- [ ] Saya tau kapan pake `for` vs `while`
- [ ] Saya paham `break` dan `continue` — beda dan kapan pakainya
- [ ] Saya paham konsep `else` di loop (uniquely Python)
- [ ] Saya bisa bikin nested loop
- [ ] Saya waspada dengan infinite loop

**Kalau semua checklist tercentang → lanjut ke Modul 7.**
