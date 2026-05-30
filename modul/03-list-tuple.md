# Modul 3: List & Tuple

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Membuat, mengakses, dan memanipulasi **list**
- Membedakan list vs tuple
- Menjelaskan **mutable vs immutable** ke murid
- Menggunakan method-method list (`append`, `insert`, `remove`, dll)
- Loop dasar untuk mengolah list

---

## 1. Apa Itu List?

List adalah **kumpulan data berurutan** yang bisa diubah (mutable). Ini salah satu struktur data paling penting di Python.

```python
# List dibuat dengan kurung siku []
siswa = ["Budi", "Ani", "Citra", "Dedi"]
angka = [1, 2, 3, 4, 5]
campur = ["Budi", 17, True, 88.5]
kosong = []

print(siswa)     # ['Budi', 'Ani', 'Citra', 'Dedi']
print(type(siswa))  # <class 'list'>
```

### Sama Seperti String: Index & Slicing

List juga punya index, sama persis seperti string:

```python
siswa = ["Budi", "Ani", "Citra", "Dedi"]

print(siswa[0])      # Budi
print(siswa[-1])     # Dedi
print(siswa[1:3])    # ['Ani', 'Citra']
print(siswa[::-1])   # ['Dedi', 'Citra', 'Ani', 'Budi']
```

> 💡 Apapun yang kamu pelajari tentang slicing string, **berlaku sama** untuk list.

### Beda dengan String: List Bisa Diubah!

```python
siswa = ["Budi", "Ani", "Citra"]
siswa[1] = "Anita"      # ✅ BISA diubah
print(siswa)            # ['Budi', 'Anita', 'Citra']

# Bandingkan dengan string:
s = "ABC"
# s[1] = "X"  ❌ TypeError!
```

## 2. Method-Method List

```python
siswa = ["Budi", "Ani", "Citra"]

# Menambah
siswa.append("Dedi")          # ['Budi', 'Ani', 'Citra', 'Dedi'] — tambah di akhir
siswa.insert(1, "Eva")        # ['Budi', 'Eva', 'Ani', 'Citra', 'Dedi'] — di index 1

# Menghapus
siswa.remove("Ani")           # Hapus "Ani" (yang pertama ditemukan)
siswa.pop()                   # Hapus & return yang terakhir
siswa.pop(1)                  # Hapus & return index 1
del siswa[0]                  # Hapus index 0
siswa.clear()                 # Hapus semua

# Mencari
siswa = ["Budi", "Ani", "Citra", "Budi"]
print(siswa.index("Citra"))   # 2 — index dari "Citra"
print(siswa.count("Budi"))    # 2 — "Budi" muncul 2x
print("Ani" in siswa)         # True

# Mengurutkan
angka = [3, 1, 4, 1, 5]
angka.sort()                  # [1, 1, 3, 4, 5] — urut naik
angka.sort(reverse=True)      # [5, 4, 3, 1, 1] — urut turun
angka.reverse()               # Balik urutan

# Lainnya
print(len(siswa))             # 4 — jumlah elemen
```

### Method yang Paling Sering Dipakai

| Method | Fungsi | Contoh |
|--------|--------|--------|
| `append(x)` | Tambah x di akhir | `list.append(5)` |
| `insert(i, x)` | Tambah x di index i | `list.insert(0, "a")` |
| `remove(x)` | Hapus x pertama | `list.remove("a")` |
| `pop(i)` | Ambil & hapus index i | `x = list.pop()` |
| `sort()` | Urutkan ascending | `list.sort()` |
| `index(x)` | Cari index x | `i = list.index("a")` |

## 3. List Bisa Berisi List (Nested List)

```python
# Matriks 2D
nilai = [
    ["Budi", 85, 90, 78],
    ["Ani", 92, 88, 95],
    ["Citra", 76, 80, 82]
]

print(nilai[0])          # ['Budi', 85, 90, 78] — baris pertama
print(nilai[0][1])       # 85 — Budi, nilai pertama
print(nilai[2][3])       # 82 — Citra, nilai terakhir

# Loop untuk nested list
for siswa in nilai:
    print(f"{siswa[0]}: {siswa[1:]}")
```

Ini berguna banget buat data nilai siswa — kita akan pakai di proyek akhir.

## 4. Tuple — List yang Tidak Bisa Diubah

Tuple seperti **list versi read-only**. Immutable.

```python
# Tuple dibuat dengan kurung biasa ()
warna = ("merah", "kuning", "hijau")
koordinat = (10, 20)
sehari_hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat")
satu_item = ("isi",)  # ⚠️ KOMA wajib untuk tuple 1 item!

print(warna[0])     # merah — bisa diakses
print(warna[1:3])   # ('kuning', 'hijau') — bisa slicing
# warna[0] = "biru"  ❌ TypeError! Tuple tidak bisa diubah
```

### Kapan pakai List vs Tuple?

| List (Mutable) | Tuple (Immutable) |
|----------------|-------------------|
| Daftar siswa (berubah-ubah) | Hari dalam seminggu (tetap) |
| Nilai ujian (bisa diupdate) | Koordinat (tidak berubah) |
| Keranjang belanja | Konstanta warna lampu lalu lintas |
| Data sementara | Key dictionary (akan dipelajari) |

> 🏆 **Poin ngajar:** "Tuple itu seperti data yang ditandatangani kontrak — sudah fix, tidak bisa diubah. List itu seperti draf — masih bisa direvisi."

### Tuple Berguna untuk Multiple Return

```python
def hitung(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    return tambah, kurang, kali  # Return tuple secara implisit

hasil = hitung(10, 3)
print(hasil)         # (13, 7, 30)
print(type(hasil))   # <class 'tuple'>

# Bisa di-unpack langsung:
tambah, kurang, kali = hitung(10, 3)
print(tambah)  # 13
print(kurang)  # 7
```

Ini sangat Pythonic — kita akan sering lihat pola ini.

## 5. Loop Sederhana untuk List

```python
siswa = ["Budi", "Ani", "Citra"]

# Cara 1: Loop langsung elemen
for s in siswa:
    print(f"Halo {s}!")

# Cara 2: Loop dengan index (pake range)
for i in range(len(siswa)):
    print(f"Siswa ke-{i+1}: {siswa[i]}")

# Cara 3: enumerate — dapet index + elemen sekaligus 🔥
for i, s in enumerate(siswa):
    print(f"{i+1}. {s}")
```

> 💡 **`enumerate()`** adalah fungsi Python yang sering dipake. Hafalkan — ini bikin looping lebih elegan.

---

## 🧪 Latihan Modul 3

### Latihan 1: Daftar Belanja

```python
# Buat program daftar belanja interaktif:
# 1. User bisa menambah item
# 2. User bisa menghapus item
# 3. Tampilkan semua item dengan nomor
# Contoh:
#   > tambah susu
#   > tambah roti
#   > tambah telur
#   > lihat
#   1. susu
#   2. roti
#   3. telur
#   > hapus 2
#   > lihat
#   1. susu
#   2. telur
#   > selesai
```

### Latihan 2: Nilai Kelas

```python
# Daftar nilai siswa
nilai_siswa = [85, 92, 78, 90, 88, 76, 95, 82]

# Hitung dan cetak:
# - Nilai tertinggi
# - Nilai terendah
# - Rata-rata kelas
# - Jumlah siswa yang lulus (>=75)
# Hint: gunakan max(), min(), sum(), len()
```

### Latihan 3: Matriks Sederhana

```python
# Buat matriks 3x3 (angka 1-9):
# 1 2 3
# 4 5 6
# 7 8 9
#
# Cetak dengan format rapi.
# Akses dan cetak elemen di baris 2, kolom 3 (harus 6)
```

### Latihan 4: Unpack Tuple

```python
# Buat fungsi yang mengembalikan (nama, usia, kelas)
# Panggil dan unpack hasilnya ke variabel terpisah
```

---

## ✅ Checklist Paham

- [ ] Saya bisa bikin dan mengakses list
- [ ] Saya bisa pake `append()`, `insert()`, `remove()`, `pop()`, `sort()`
- [ ] Saya paham beda mutable vs immutable (list vs tuple)
- [ ] Saya bisa bikin tuple dan paham kapan pakainya
- [ ] Saya paham konsep nested list
- [ ] Saya bisa pake `enumerate()` untuk loop
- [ ] Saya bisa unpack tuple dari return fungsi

**Kalau semua checklist tercentang → lanjut ke Modul 4.**
