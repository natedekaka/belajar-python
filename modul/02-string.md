# Modul 2: String — Manipulasi Teks

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjelaskan konsep **index** dan **slicing** string
- Menggunakan method-method string bawaan Python
- Memformat teks dengan f-string
- Membedakan string immutable vs mutable

---

## 1. String Itu Kumpulan Karakter

String sebenarnya adalah **kumpulan karakter** yang berurutan. Setiap karakter punya **nomor index**.

```python
kata = "PYTHON"
# Index:  012345
```

| P | Y | T | H | O | N |
|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 |

```python
kata = "PYTHON"
print(kata[0])   # P
print(kata[1])   # Y
print(kata[5])   # N
print(kata[-1])  # N — index negatif dari belakang
print(kata[-2])  # O
```

### Index Negatif

Python punya fitur keren: index dari **belakang** pake angka negatif.

```
Index positif:  0   1   2   3   4   5
               P   Y   T   H   O   N
Index negatif: -6  -5  -4  -3  -2  -1
```

```python
teks = "Python"
print(teks[-1])  # n
print(teks[-3])  # h
```

## 2. Slicing — Memotong String

Slicing = mengambil **sebagian** string.

```python
# Sintaks: string[mulai:akhir:langkah]
# mulai: index awal (diikutkan, default 0)
# akhir: index akhir (tidak diikutkan, default sampai akhir)
# langkah: step (default 1)

s = "Python Programming"

print(s[0:6])       # 'Python'     — index 0 sampai 5
print(s[7:18])      # 'Programming' — index 7 sampai 17
print(s[:6])        # 'Python'     — dari awal sampai index 5
print(s[7:])        # 'Programming' — dari index 7 sampai akhir
print(s[:])         # 'Python Programming' — seluruh string

# Slicing dengan langkah
print(s[0:6:2])     # 'Pto' — index 0,2,4
print(s[::-1])      # 'gnimmargorP nohtyP' — dibalik! 🔥
```

> 💡 **`[::-1]`** adalah idiom Python untuk **membalik string**. Hafalkan — ini sering ditanyain di kelas dan tes.

### Teka-teki Slicing buat Murid

```python
# Coba tebak outputnya:
print("INFORMATIKA"[0:5])     # ??
print("INFORMATIKA"[5:])      # ??
print("INFORMATIKA"[2:9:3])   # ??
print("INFORMATIKA"[::-1])    # ??
```

## 3. Method-Method String (Built-in)

Method = fungsi yang nempel di data. String punya banyak method berguna.

### PENTING: String Method Tidak Mengubah String Asli

String di Python **immutable** (tidak bisa diubah). Semua method string **mengembalikan string baru**.

```python
s = "  Python Itu Seru!  "

# Merubah huruf
print(s.upper())          # '  PYTHON ITU SERU!  '
print(s.lower())          # '  python itu seru!  '
print(s.title())          # '  Python Itu Seru!  '
print(s.capitalize())     # '  python itu seru!  '

# Menghapus spasi di pinggir
print(s.strip())          # 'Python Itu Seru!'
print(s.lstrip())         # 'Python Itu Seru!  '
print(s.rstrip())         # '  Python Itu Seru!'

# Cek isi string
print(s.isupper())        # False
print("PYTHON".isupper()) # True
print("123".isdigit())    # True
print("abc123".isalnum()) # True
print("abc".isalpha())    # True

# Mencari dan mengganti
s2 = "Belajar Python itu menyenangkan"
print(s2.find("Python"))    # 8 — index mulai kata "Python"
print(s2.find("Java"))      # -1 — tidak ditemukan
print(s2.count("a"))        # 3 — huruf 'a' muncul 3x
print(s2.replace("menyenangkan", "seru"))  # 'Belajar Python itu seru'

# Memisah dan menggabung
kalimat = "satu-dua-tiga"
print(kalimat.split("-"))   # ['satu', 'dua', 'tiga']

daftar = ["satu", "dua", "tiga"]
print("-".join(daftar))     # 'satu-dua-tiga'
```

> 💡 Method yang paling sering dipake: `.lower()`, `.strip()`, `.split()`, `.replace()`, `.find()`.

## 4. Mengecek Keberadaan Substring

```python
teks = "Python adalah bahasa pemrograman"

# Operator IN
print("Python" in teks)      # True
print("Java" in teks)        # False

# Operator NOT IN
print("Java" not in teks)    # True
```

Ini sangat berguna buat validasi input — kita akan pakai di Modul 5 (Percabangan).

## 5. Escape Characters

Kadang kita perlu karakter khusus di dalam string:

```python
print("Dia berkata: \"Halo\"")   # Petik dua di dalam petik dua
print('It\'s fine')              # Petik satu di dalam petik satu
print("Baris 1\nBaris 2")       # \n = newline (enter)
print("Kolom 1\tKolom 2")       # \t = tab
print("Backslash: \\")           # \\ = backslash literal
```

## 6. Format String — F-String (Wajib Kuasai)

Ini adalah **cara modern** dan **paling sering dipakai** di Python 3.6+.

```python
nama = "Budi"
nilai = 88.5
kelas = "XII IPA 1"

# Basic
print(f"Siswa {nama} dari kelas {kelas}")

# Angka dengan format
print(f"Nilai: {nilai:.1f}")       # 88.5 — 1 desimal
print(f"Nilai: {nilai:.0f}")       # 88 — dibulatkan

# Lebar minimum
print(f"Nama: |{nama:10}|")       # |Budi      | — rata kiri
print(f"Nama: |{nama:>10}|")      # |      Budi| — rata kanan
print(f"Nama: |{nama:^10}|")      # |   Budi   | — tengah

# Angka dengan leading zero
print(f"{7:03d}")                  # 007
print(f"{12:03d}")                 # 012

# Persentase
print(f"{0.85:.1%}")              # 85.0%
```

> 💡 **Latih f-string sampai hafal.** Ini yang paling berguna di dunia nyata.

## 7. String Immutable — Konsep Penting

String **tidak bisa diubah**. Kalau kamu coba:

```python
s = "Python"
s[0] = "J"  # ❌ TypeError: 'str' object does not support item assignment
```

Ini beda sama list (yang akan kita pelajari di Modul 3). Kalau mau "mengubah" string, kita harus **bikin string baru**.

```python
s = "Python"
s = "J" + s[1:]  # ✅ 'Jython' — bikin string baru
```

> 🏆 **Poin ngajar:** "String itu seperti buku cetak. Kamu gak bisa hapus satu huruf dari halaman. Kamu harus cetak ulang bukunya."

---

## 🧪 Latihan Modul 2

### Latihan 1: Pembalik Nama

```python
# Minta nama depan dan nama belakang
# Output: "Nama terbalik: [nama_belakang] [nama_depan]"
# Contoh: "Budi Santoso" → "Santoso Budi"
```

### Latihan 2: Validasi Password

```python
# Minta password
# Cek: minimal 8 karakter, mengandung angka
# Output: "Password valid" atau "Password terlalu pendek" / "Harus ada angka"
```

### Latihan 3: Format Nilai

```python
# Input: nama siswa, nilai matematika, nilai ipa, nilai bahasa
# Output: laporan rapor format rapi
'''
====================================
LAPORAN NILAI SISWA
====================================
Nama          : Budi Santoso
Matematika    : 85.0
IPA           : 92.5
Bahasa        : 78.0
------------------------------------
Rata-rata     : 85.2
====================================
'''
```

### Latihan 4: Pembersih Teks

```python
# Input: "  PyThOn  ItU  sERu!  "
# Output: "Python Itu Seru!" — bersih, kapitalisasi rapi
# Hint: pake strip(), lower(), title()
```

---

## ✅ Checklist Paham

- [ ] Saya bisa jelasin konsep index 0 dan index negatif
- [ ] Saya bisa slicing string dengan `[start:stop:step]`
- [ ] Saya hafal `[::-1]` untuk membalik string
- [ ] Saya bisa pake `.upper()`, `.lower()`, `.strip()`, `.split()`, `.replace()`, `.join()`
- [ ] Saya paham string itu **immutable**
- [ ] Saya bisa format teks pake f-string
- [ ] Saya bisa cek keberadaan substring dengan `in`

**Kalau semua checklist tercentang → lanjut ke Modul 3.**
