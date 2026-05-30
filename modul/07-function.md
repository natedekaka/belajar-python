# Modul 7: Function (Fungsi)

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Membuat dan memanggil fungsi sendiri
- Menjelaskan **parameter**, **argumen**, dan **return value**
- Membedakan parameter vs argumen
- Memahami **scope** (lokal vs global)
- Menggunakan default parameter, *args, **kwargs

---

## 1. Kenapa Perlu Fungsi?

Fungsi adalah **blok kode yang bisa dipakai ulang**. Bayangkan kamu punya kode untuk hitung rata-rata:

```python
# Tanpa fungsi — harus nulis ulang setiap kali
nilai1 = [85, 90, 78]
rata1 = sum(nilai1) / len(nilai1)
print(f"Rata-rata: {rata1}")

nilai2 = [92, 88, 95]
rata2 = sum(nilai2) / len(nilai2)
print(f"Rata-rata: {rata2}")

# Dengan fungsi — tulis sekali, pake berkali-kali
def hitung_rata(daftar_nilai):
    return sum(daftar_nilai) / len(daftar_nilai)

print(f"Rata-rata: {hitung_rata(nilai1)}")
print(f"Rata-rata: {hitung_rata(nilai2)}")
```

Manfaat fungsi:
- **Reusable** — tulis sekali, pake kapan saja
- **Modular** — kode terorganisir, gampang dicari bug-nya
- **Readable** — nama fungsi menjelaskan apa yang dilakukan
- **Testable** — bisa diuji sendiri-sendiri

## 2. Struktur Fungsi

```python
# def nama_fungsi(parameter1, parameter2, ...):
#     """Dokumentasi (optional)"""
#     ... kode ...
#     return hasil (optional)

def sapa(nama):
    """Menyapa seseorang dengan namanya"""
    pesan = f"Halo {nama}! Selamat belajar Python!"
    return pesan

# Panggil fungsi
output = sapa("Budi")
print(output)  # Halo Budi! Selamat belajar Python!
```

### Komponen Fungsi:

| Bagian | Penjelasan | Contoh |
|--------|------------|--------|
| `def` | Keyword untuk mendefinisikan fungsi | `def hitung():` |
| Nama | Nama fungsi (snake_case) | `hitung_rata` |
| Parameter | Input fungsi (opsional) | `(daftar_nilai)` |
| `return` | Output fungsi (opsional) | `return hasil` |
| Docstring | Dokumentasi (opsional) | `"""Hitung rata-rata"""` |

> 💡 Fungsi bisa tanpa parameter dan tanpa return:

```python
def garis():
    print("=" * 30)

garis()  # ==============================
garis()  # Bisa dipanggil berkali-kali
```

## 3. Parameter vs Argumen

**Parameter** = variabel yang didefinisikan di fungsi.  
**Argumen** = nilai yang dikirim saat memanggil fungsi.

```python
def kali(a, b):      # a dan b adalah PARAMETER
    return a * b

hasil = kali(5, 3)   # 5 dan 3 adalah ARGUMEN
print(hasil)          # 15
```

> 🏆 **Poin ngajar:** "Parameter itu seperti wadah kosong yang kita siapkan di fungsi. Argumen itu isinya yang kita kirim waktu manggil."

### Jenis Argumen

**1. Positional Arguments (berdasarkan urutan)**

```python
def data_siswa(nama, kelas, nilai):
    print(f"{nama} - {kelas} - {nilai}")

data_siswa("Budi", "XII IPA 1", 85)
# Urutan penting: Budi → nama, XII IPA 1 → kelas, 85 → nilai
```

**2. Keyword Arguments (sebut nama parameter)**

```python
data_siswa(nama="Ani", nilai=92, kelas="XII IPA 1")
# Urutan tidak penting kalau pakai keyword
```

**3. Campuran (positional dulu, baru keyword)**

```python
data_siswa("Citra", kelas="XII IPA 1", nilai=78)
# ✅ Boleh — positional dulu
# data_siswa(nama="Dedi", "XII IPA 1", 88)
# ❌ Error — positional setelah keyword
```

## 4. Default Parameter

Parameter bisa punya **nilai default**. Kalau argumen tidak diberikan, nilai default dipakai.

```python
def sapa(nama="Teman"):
    print(f"Halo {nama}!")

sapa("Budi")     # Halo Budi!
sapa()           # Halo Teman! — pakai default
```

```python
def info_siswa(nama, kelas="XII IPA 1", status="aktif"):
    print(f"{nama} - {kelas} - {status}")

info_siswa("Budi")                    # Budi - XII IPA 1 - aktif
info_siswa("Ani", "XI IPA 2")        # Ani - XI IPA 2 - aktif
info_siswa("Citra", status="tidak")  # Citra - XII IPA 1 - tidak
```

> ⚠️ **Aturan:** Parameter dengan default harus **setelah** parameter tanpa default. Ini error: `def func(a=1, b):` ❌

## 5. Return Value

Fungsi bisa **mengembalikan** nilai dengan `return`.

```python
def tambah(a, b):
    return a + b

hasil = tambah(5, 3)   # hasil = 8
print(hasil * 2)        # 16 — return value bisa dipakai lagi
```

### Multiple Return (Sebagai Tuple)

```python
def hitung(a, b):
    tambah = a + b
    kurang = a - b
    kali = a * b
    bagi = a / b
    return tambah, kurang, kali, bagi  # Return tuple

hasil = hitung(10, 3)
print(hasil)        # (13, 7, 30, 3.33...)

# Unpack langsung
tambah, kurang, kali, bagi = hitung(10, 3)
print(tambah)   # 13
```

### Fungsi Tanpa Return → None

```python
def cetak_pesan(pesan):
    print(pesan)

hasil = cetak_pesan("Halo")
print(hasil)  # None — fungsi tidak punya return
```

> 💡 Setiap fungsi Python **selalu** mengembalikan sesuatu. Kalau tidak ada `return`, return-nya `None`.

## 6. Scope — Dimana Variabel Bisa Diakses

Scope = **lingkungan** dimana variabel bisa diakses.

### Variabel Lokal

Variabel yang didefinisikan **di dalam fungsi**:

```python
def hitung_nilai():
    bonus = 10       # Lokal — hanya ada di dalam fungsi
    nilai = 85 + bonus
    return nilai

print(hitung_nilai())  # 95
# print(bonus)          ❌ NameError! bonus tidak dikenal di luar fungsi
```

### Variabel Global

Variabel yang didefinisikan **di luar fungsi**:

```python
kelas = "XII IPA 1"  # Global — bisa diakses di mana saja

def tampilkan_kelas():
    print(f"Kelas: {kelas}")  # ✅ Bisa akses variabel global

tampilkan_kelas()  # Kelas: XII IPA 1

def ubah_kelas():
    kelas = "XII IPA 2"  # ⚠️ Ini BUKAN mengubah global!
    # Ini malah bikin variabel LOKAL baru bernama kelas
    print(f"Di dalam: {kelas}")

ubah_kelas()      # Di dalam: XII IPA 2
print(kelas)      # XII IPA 1 — global tidak berubah!
```

### Global Keyword

Kalau kamu **harus** mengubah variabel global di dalam fungsi:

```python
kelas = "XII IPA 1"

def ubah_kelas():
    global kelas     # Bilang: "saya mau pake variabel global ini"
    kelas = "XII IPA 2"

ubah_kelas()
print(kelas)   # XII IPA 2
```

> ⚠️ **Hindari `global`** sebisa mungkin. Fungsi yang baik menerima input lewat parameter, bukan lewat variabel global.

## 7. *args dan **kwargs (Advanced)

Kadang kita tidak tahu berapa banyak argumen yang akan diberikan.

### *args — Banyak Positional Arguments

```python
def jumlahkan(*args):
    """Jumlahkan semua angka yang diberikan"""
    print(args)  # Tuple: (1, 2, 3, 4, 5)
    return sum(args)

print(jumlahkan(1, 2, 3, 4, 5))    # 15
print(jumlahkan(10, 20))            # 30
```

### **kwargs — Banyak Keyword Arguments

```python
def cetak_info(**kwargs):
    """Cetak informasi dari keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

cetak_info(nama="Budi", kelas="XII IPA 1", nilai=85)
# Output:
# nama: Budi
# kelas: XII IPA 1
# nilai: 85
```

### Gabungan Semua

```python
def fungsi_lengkap(a, b, *args, default="Halo", **kwargs):
    print(f"a={a}, b={b}")
    print(f"args={args}")
    print(f"default={default}")
    print(f"kwargs={kwargs}")

fungsi_lengkap(1, 2, 3, 4, 5, default="Yoo", nama="Budi")
# a=1, b=2
# args=(3, 4, 5)
# default=Yoo
# kwargs={'nama': 'Budi'}
```

> 💡 Urutan parameter: `positional, *args, default, **kwargs`

## 8. Type Hints (Petunjuk Tipe) — Python Modern

Python 3.5+ punya **type hints** — memberi tahu tipe data parameter dan return value. Ini tidak memaksa, tapi membantu.

```python
def hitung_rata(daftar: list) -> float:
    """Hitung rata-rata dari list angka"""
    return sum(daftar) / len(daftar)

def sapa(nama: str, usia: int) -> str:
    return f"Halo {nama}, usia {usia} tahun"

def aktifkan_siswa(siswa: dict) -> dict:
    siswa["aktif"] = True
    return siswa
```

> 💡 Type hints membantu kamu (dan murid) membaca fungsi dengan cepat: "Oh, fungsi ini menerima list dan mengembalikan float."

---

## 🧪 Latihan Modul 7

### Latihan 1: Fungsi Matematika

```python
# Buat fungsi-fungsi berikut:
# 1. luas_persegi(sisi) → luas persegi
# 2. luas_lingkaran(jari) → luas lingkaran (π=3.14)
# 3. volume_balok(p, l, t) → volume balok
# 4. konversi_suhu(celsius) → return (fahrenheit, kelvin, reamur)
```

### Latihan 2: Fungsi Validasi Nilai

```python
def validasi_nilai(nilai):
    """Return True kalau nilai valid (0-100), False kalau tidak"""
    # TODO: implementasi

def grade_nilai(nilai):
    """Return grade A/B/C/D/E berdasarkan nilai"""
    # TODO: implementasi
    pass

# Test
nilai = float(input("Masukkan nilai: "))
if validasi_nilai(nilai):
    print(f"Grade: {grade_nilai(nilai)}")
else:
    print("Nilai tidak valid!")
```

### Latihan 3: Fungsi dengan Default

```python
def buat_laporan(nama, nilai, kelas="XII IPA 1", tahun=2026):
    """Membuat string laporan siswa"""
    # TODO: return string laporan rapi

# Test
print(buat_laporan("Budi", 85))
print(buat_laporan("Ani", 92, kelas="XI IPA 2"))
print(buat_laporan("Citra", 78, tahun=2025))
```

### Latihan 4: Kalkulator dengan *args

```python
def kalkulator(operasi, *angka):
    """
    operasi: "tambah", "kurang", "kali", "rata"
    angka: daftar angka yang akan dioperasikan
    """
    # TODO: implementasi

# Test
print(kalkulator("tambah", 1, 2, 3))    # 6
print(kalkulator("kali", 2, 3, 4))      # 24
print(kalkulator("rata", 10, 20, 30))   # 20.0
```

---

## ✅ Checklist Paham

- [ ] Saya bisa bikin fungsi sendiri dengan `def`
- [ ] Saya paham beda parameter vs argumen
- [ ] Saya bisa pake positional dan keyword arguments
- [ ] Saya paham default parameter
- [ ] Saya paham `return` dan fungsi tanpa return return None
- [ ] Saya paham scope lokal vs global
- [ ] Saya tau `*args` dan `**kwargs`

**Kalau semua checklist tercentang → lanjut ke Modul 8.**
