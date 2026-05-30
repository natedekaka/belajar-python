# 🐍 Python Cheat Sheet — Cetak 1 Halaman (Bolak-Balik)

## 📌 Tipe Data & Variabel

| Tipe | Contoh | Keterangan |
|------|--------|------------|
| `int` | `x = 5` | Bilangan bulat |
| `float` | `y = 3.14` | Bilangan desimal |
| `str` | `nama = "Budi"` | Teks |
| `bool` | `aktif = True` | True / False |

```python
# Cek tipe
type(x)          # <class 'int'>

# Casting
int("5")         # String → int
str(5)           # int → string
float("3.14")    # String → float

# Input (selalu return string)
umur = int(input("Umur: "))
```

## 📌 String

```python
s = "Python Programming"
s[0]           # 'P' — index 0
s[-1]          # 'n' — dari belakang
s[0:6]         # 'Python' — slicing
s[::-1]        # 'gnimmargorP nohtyP' — balik!

s.lower()      # 'python programming'
s.upper()      # 'PYTHON PROGRAMMING'
s.strip()      # Hapus spasi pinggir
s.split()      # ['Python', 'Programming']
"-".join(["a","b"])  # 'a-b'
s.replace("P", "J")  # 'Jython'
len(s)         # 18
"Python" in s  # True

f"Halo {nama}, umur {umur}"  # f-string 🔥
```

## 📌 List & Tuple

```python
# List — bisa diubah
listku = [1, 2, 3]
listku.append(4)       # [1,2,3,4]
listku.insert(0, 0)    # [0,1,2,3,4]
listku.remove(2)       # Hapus angka 2
x = listku.pop()       # Ambil & hapus akhir
listku.sort()          # Urutkan
len(listku)            # Panjang
listku[::-1]           # Balik

# Tuple — tidak bisa diubah
tup = (1, 2, 3)
a, b, c = tup          # Unpack
```

## 📌 Dictionary

```python
d = {"nama": "Budi", "nilai": 85}
d["nama"]              # 'Budi'
d.get("alamat", "-")   # '-' (aman)
d["umur"] = 17         # Tambah/ubah
del d["umur"]          # Hapus
"nama" in d            # True
d.keys()               # Semua key
d.values()             # Semua value
d.items()              # Pasangan (key, value)

for k, v in d.items():
    print(f"{k}: {v}")
```

## 📌 If/Else

```python
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
else:
    grade = "C"

# Ternary
status = "Lulus" if nilai >= 75 else "Tidak"

# Operator logika
and, or, not

# Cek truthy/falsy
if nama:     # True kalau tidak kosong
if listku:   # True kalau tidak kosong
```

## 📌 Loop

```python
# For
for i in range(5):         # 0,1,2,3,4
for i in range(2, 6):      # 2,3,4,5
for i in range(0, 10, 2):  # 0,2,4,6,8

for item in listku:
for i, item in enumerate(listku):  # dapet index
for k, v in d.items():

# While
while kondisi:
    # hati-hati infinite loop!

break      # Hentikan loop
continue   # Lompat ke iterasi berikut
```

## 📌 Function

```python
def nama_fungsi(param1, param2="default"):
    """Docstring"""
    return hasil

def func(*args, **kwargs):
    # *args = tuple
    # **kwargs = dict

# Lambda
kali = lambda x: x * 2
```

## 📌 Error Handling

```python
try:
    hasil = 10 / angka
except ValueError:
    print("Bukan angka!")
except ZeroDivisionError:
    print("Pembagian nol!")
else:
    print("Sukses!")
finally:
    print("Selesai")
```

## 📌 File I/O

```python
# Baca
with open("file.txt", "r") as f:
    isi = f.read()           # Semua
    baris = f.readlines()    # List baris
    for line in f:           # Per baris

# Tulis
with open("file.txt", "w") as f:  # Timpa
    f.write("teks\n")
with open("file.txt", "a") as f:  # Tambah

# CSV
import csv
with open("data.csv", "r") as f:
    for row in csv.reader(f):
        ...

# JSON
import json
with open("data.json", "r") as f:
    data = json.load(f)
```

## 📌 List Comprehension

```python
[expr for item in iterable]
[expr for item in iterable if kondisi]
[expr if kondisi else expr2 for item in iterable]

[x**2 for x in range(10)]          # [0,1,4,9,...]
[x for x in range(20) if x%2==0]   # Genap
```

## 📌 OOP

```python
class Siswa:
    sekolah = "SMA 1"  # Class variable
    
    def __init__(self, nama, nilai):
        self.nama = nama       # Instance variable
        self.nilai = nilai
    
    def lulus(self):
        return self.nilai >= 75
    
    def __str__(self):
        return f"{self.nama}: {self.nilai}"

# Inheritance
class SiswaBaru(Siswa):
    def __init__(self, nama, nilai, kelas):
        super().__init__(nama, nilai)
        self.kelas = kelas
```

## 📌 Module & pip

```python
import math
from random import randint, choice
import requests as req

# if __name__ == "__main__":
#     test code here
```

```bash
pip install nama_package
pip install -r requirements.txt
pip list
```

---

> 💡 Print ini bolak-balik, laminating, tempel di meja!
