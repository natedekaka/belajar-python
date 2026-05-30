# Modul 8: Error & Exception Handling

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Membaca dan memahami **error message** Python
- Membedakan **syntax error** vs **exception**
- Menggunakan `try/except` untuk menangani error
- Membuat program yang **tidak crash** di situasi tak terduga
- Melempar error sendiri dengan `raise`

---

## 1. Error Itu Guru Terbaik

Error di Python **bukan musuh** — itu petunjuk. Setiap error memberitahu:
1. **Apa yang salah**
2. **Di baris berapa**
3. **Jenis errornya apa**

### Syntax Error — Salah Nulis

Error paling dasar: kode tidak sesuai aturan bahasa Python.

```python
# print("Halo"   ← lupa tutup kurung
# SyntaxError: '(' was never closed

# if x > 5     ← lupa titik dua
#     print(x)
# SyntaxError: expected ':'
```

> 💡 Syntax error akan dicegah oleh VS Code / editor sebelum dijalankan. Perhatikan garis merah!

### Exception — Error Saat Jalan

Program sudah benar secara syntax, tapi terjadi masalah saat dijalankan:

```python
# TypeError
print("Angka: " + 5)
# TypeError: can only concatenate str (not "int") to str

# ValueError
angka = int("abc")
# ValueError: invalid literal for int() with base 10: 'abc'

# ZeroDivisionError
print(10 / 0)
# ZeroDivisionError: division by zero

# IndexError
listku = [1, 2, 3]
print(listku[10])
# IndexError: list index out of range

# KeyError
dictku = {"nama": "Budi"}
print(dictku["alamat"])
# KeyError: 'alamat'

# FileNotFoundError
open("file_tidak_ada.txt")
# FileNotFoundError: [Errno 2] No such file or directory
```

## 2. Try/Except — Menangkap Error

Kita bisa **menangkap** error agar program tidak crash:

```python
# Tanpa try/except:
# angka = int(input("Masukkan angka: "))
# Kalau user ketik "abc" → program crash!

# Dengan try/except:
try:
    angka = int(input("Masukkan angka: "))
    print(f"Angka yang dimasukkan: {angka}")
except ValueError:
    print("Error: Itu bukan angka yang valid!")
```

Flowchart:
```
     ┌──────────────┐
     │  try block   │
     │  coba jalanin│
     └──────┬───────┘
            │
     ┌──────┴───────┐
     │  Error?      │
     └──┬───────┬───┘
     Tidak    Ya
        │       │
   Lanjut  ┌───┴──────────┐
   normal  │ except block │
           │ jalan        │
           └──────────────┘
```

### Menangkap Banyak Jenis Error

```python
try:
    angka1 = int(input("Angka 1: "))
    angka2 = int(input("Angka 2: "))
    hasil = angka1 / angka2
    print(f"Hasil: {hasil}")
except ValueError:
    print("Error: Input harus angka!")
except ZeroDivisionError:
    print("Error: Tidak bisa membagi dengan nol!")
```

### Menangkap Semua Error (Hati-hati!)

```python
try:
    # Kode yang mungkin error
    hasil = 10 / 0
except Exception as e:
    print(f"Terjadi error: {e}")
    # e berisi pesan error asli
```

> ⚠️ **Menangkap semua error** dengan `except Exception` itu praktik yang kurang baik. Tangkap error spesifik agar kamu tahu persis apa yang salah. Tapi untuk belajar, ini oke.

## 3. Else dan Finally

### Else — Jalan Kalau Tidak Ada Error

```python
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Error: Bukan angka!")
else:
    # Hanya jalan kalau try block sukses (tidak ada error)
    print(f"Angka valid: {angka}")
```

### Finally — SELALU Jalan

```python
try:
    file = open("data.txt", "r")
    isi = file.read()
    print(isi)
except FileNotFoundError:
    print("File tidak ditemukan!")
finally:
    # SELALU dijalankan, entah error atau tidak
    print("Blok finally: program selesai.")
```

> 💡 `finally` biasa dipakai untuk **bersih-bersih**: tutup file, tutup koneksi database, dll.

### Gabungan Lengkap

```python
try:
    # Coba kode yang berpotensi error
    angka = int(input("Angka: "))
    hasil = 10 / angka
except ValueError:
    print("Input harus angka!")
except ZeroDivisionError:
    print("Tidak boleh nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Selesai ✅")
```

## 4. Raise — Melempar Error Sendiri

Kadang kita mau **sengaja membuat error** kalau suatu kondisi terpenuhi.

```python
def cek_usia(usia):
    if usia < 0:
        raise ValueError("Usia tidak boleh negatif!")
    if usia > 150:
        raise ValueError("Usia tidak realistis!")
    print(f"Usia {usia} valid")

# Test
try:
    cek_usia(-5)
except ValueError as e:
    print(f"Error: {e}")
```

```python
# Contoh di aplikasi nilai
def beri_nilai(nilai):
    if not isinstance(nilai, (int, float)):
        raise TypeError("Nilai harus angka!")
    if nilai < 0 or nilai > 100:
        raise ValueError("Nilai harus antara 0-100!")
    
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

# Test
try:
    print(beri_nilai(85))    # B
    print(beri_nilai(-5))    # Error
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
```

> 🏆 **Poin ngajar:** "`raise` itu seperti kamu sengaja membunyikan alarm karena sesuatu tidak beres. Program lain yang panggil fungsi ini bisa menangkap alarm itu dengan `try/except`."

## 5. Custom Exception (Advanced)

Buat kelas error sendiri:

```python
class NilaiError(Exception):
    """Error khusus untuk nilai tidak valid"""
    pass

def validasi_nilai(nilai):
    if nilai < 0 or nilai > 100:
        raise NilaiError(f"Nilai {nilai} tidak valid (0-100)")
    return True

try:
    validasi_nilai(150)
except NilaiError as e:
    print(f"Validasi gagal: {e}")
```

> 💡 Ini sudah agak advanced. Cukup tahu dulu, nanti saat OOP akan lebih paham.

## 6. Common Errors & Cara Bacanya

| Error | Penyebab | Solusi |
|-------|----------|--------|
| `SyntaxError` | Salah penulisan | Cek kurung, titik dua, indentasi |
| `IndentationError` | Indentasi salah | Pastikan konsisten (spasi/tab) |
| `NameError` | Variabel belum didefinisikan | Cek nama variabel |
| `TypeError` | Operasi tipe data berbeda | Casting atau cek tipe |
| `ValueError` | Nilai tidak sesuai | Validasi input |
| `IndexError` | Index di luar jangkauan | Cek panjang list |
| `KeyError` | Key tidak ada di dict | Gunakan `.get()` |
| `ZeroDivisionError` | Pembagian nol | Cek pembagi sebelum operasi |
| `FileNotFoundError` | File tidak ditemukan | Cek path file |
| `AttributeError` | Object tidak punya method/atribut | Cek tipe object |

### Flowchart Debugging

```
Ada Error?
    │
    ├── Baca pesan error — cari tahu JENIS dan BARIS
    │
    ├── Cek baris yang disebut — apa yang salah?
    │   │
    │   ├── Typo? → perbaiki
    │   ├── Tipe data salah? → casting
    │   ├── Variabel tidak ada? → definisikan
    │   └── Index/key salah? → cek data
    │
    └── Coba lagi
```

---

## 🧪 Latihan Modul 8

### Latihan 1: Kalkulator Aman

```python
# Buat kalkulator yang:
# 1. Minta 2 angka dari user
# 2. Minta operator (+, -, *, /)
# 3. Tangani: ValueError, ZeroDivisionError
# 4. Loop sampai user ketik "exit"
```

### Latihan 2: Validasi Input Angka

```python
def minta_angka(pesan="Masukkan angka: "):
    """
    Minta input angka dari user.
    Loop terus sampai user memasukkan angka yang valid.
    Return: float
    """
    # TODO: implementasi dengan while True + try/except

# Test
umur = minta_angka("Masukkan umur: ")
print(f"Umur: {umur}")
```

### Latihan 3: Pembaca File Aman

```python
def baca_file(nama_file):
    """
    Baca isi file dan tampilkan.
    Tangani FileNotFoundError dengan pesan yang ramah.
    """
    try:
        with open(nama_file, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print(f"Maaf, file '{nama_file}' tidak ditemukan.")

# Test
baca_file("nilai_siswa.txt")
```

### Latihan 4: Fungsi dengan Raise

```python
def bagi(angka1, angka2):
    """
    - Raise TypeError kalau input bukan angka
    - Raise ZeroDivisionError kalau angka2 = 0
    - Return hasil bagi
    """
    # TODO: implementasi

# Test
try:
    print(bagi(10, 2))     # 5.0
    print(bagi(10, 0))     # Error
    print(bagi("a", 2))    # Error
except (TypeError, ZeroDivisionError) as e:
    print(f"Error: {e}")
```

---

## ✅ Checklist Paham

- [ ] Saya bisa baca dan paham pesan error Python
- [ ] Saya tau beda syntax error vs exception
- [ ] Saya bisa pake `try/except` untuk menangkap error
- [ ] Saya bisa nangkap error spesifik (ValueError, TypeError, dll)
- [ ] Saya paham `else` di try/except
- [ ] Saya paham `finally` — selalu jalan
- [ ] Saya bisa pake `raise` untuk buat error sendiri

**Kalau semua checklist tercentang → lanjut ke Modul 9.**
