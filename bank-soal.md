# 📝 Bank Soal Python — 100+ Soal Lengkap dengan Kunci Jawaban

## Format Soal

| Kode | Tipe | Bobot |
|------|------|-------|
| PG | Pilihan Ganda | 1 poin |
| C | Coding | 3-5 poin |
| E | Essay | 2-3 poin |

---

## Modul 1: Variabel & Tipe Data (15 Soal)

### PG-01
Manakah penulisan variabel yang **benar** di Python?
a) `2data = 5`  
b) `data-siswa = 5`  
c) `data_siswa = 5` ✅  
d) `data siswa = 5`

### PG-02
Tipe data dari `3.14` adalah...
a) `int`  
b) `float` ✅  
c) `str`  
d) `bool`

### PG-03
Apa output dari `print(type("123"))`?
a) `<class 'int'>`  
b) `<class 'float'>`  
c) `<class 'str'>` ✅  
d) `<class 'bool'>`

### PG-04
Apa output dari `print(10 // 3)`?
a) `3.33`  
b) `3` ✅  
c) `3.0`  
d) `4`

### PG-05
Apa output dari `print(10 % 3)`?
a) `3`  
b) `1` ✅  
c) `0`  
d) `3.33`

### PG-06
Operator yang digunakan untuk **pangkat** di Python adalah...
a) `^`  
b) `**` ✅  
c) `pow`  
d) `^^`

### PG-07
Apa output dari `print(5 + 3 * 2)`?
a) `16`  
b) `11` ✅  
c) `13`  
d) `10`

### C-01 (Bobot: 3)
Buat program yang menerima **nama** dan **tahun lahir**, lalu menampilkan:
```
Halo [nama], umur kamu [umur] tahun.
```
*Hint: tahun sekarang 2026*

**Kunci:**
```python
nama = input("Masukkan nama: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))
umur = 2026 - tahun_lahir
print(f"Halo {nama}, umur kamu {umur} tahun.")
```

### C-02 (Bobot: 3)
Buat program yang menerima dua angka, lalu menampilkan: jumlah, selisih, kali, bagi, sisa bagi.

**Kunci:**
```python
a = int(input("Angka 1: "))
b = int(input("Angka 2: "))
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} x {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
```

### E-01 (Bobot: 2)
Jelaskan perbedaan antara `int` dan `float`! Berikan contoh masing-masing.

**Kunci:** `int` untuk bilangan bulat (tanpa koma) seperti `5`, `-10`, `1000`. `float` untuk bilangan desimal seperti `3.14`, `-0.5`, `2.0`. Perbedaan utama: `int` tidak punya bagian desimal, `float` punya.

---

## Modul 2: String (12 Soal)

### PG-08
Apa output dari `"PYTHON"[2]`?
a) `'P'`  
b) `'Y'`  
c) `'T'` ✅  
d) `'H'`

### PG-09
Apa output dari `"PYTHON"[::-1]`?
a) `'PYTHON'`  
b) `'NOHTYP'` ✅  
c) `'NOTYPH'`  
d) `'Python'`

### PG-10
Method untuk menghapus spasi di kiri dan kanan string adalah...
a) `.cut()`  
b) `.remove()`  
c) `.strip()` ✅  
d) `.trim()`

### PG-11
Apa output dari `"belajar python".title()`?
a) `'Belajar Python'` ✅  
b) `'BELAJAR PYTHON'`  
c) `'belajar python'`  
d) `'Belajar python'`

### PG-12
Apa output dari `"satu-dua-tiga".split("-")`?
a) `['satu', 'dua', 'tiga']` ✅  
b) `'satu duetiga'`  
c) `['satu-dua-tiga']`  
d) `'satu', 'dua', 'tiga'`

### PG-13
String di Python bersifat... (pilih yang benar)
a) Mutable (bisa diubah)  
b) Immutable ✅  
c) Bisa diubah dengan assignment index  
d) Tidak bisa diakses per karakter

### C-03 (Bobot: 4)
Buat program yang menerima sebuah kalimat, lalu menampilkan:
1. Jumlah karakter
2. Kalimat dalam huruf besar semua
3. Kalimat dalam huruf kecil semua
4. Kalimat yang dibalik

**Kunci:**
```python
kalimat = input("Masukkan kalimat: ")
print(f"Jumlah karakter: {len(kalimat)}")
print(f"Huruf besar: {kalimat.upper()}")
print(f"Huruf kecil: {kalimat.lower()}")
print(f"Dibalik: {kalimat[::-1]}")
```

### E-02 (Bobot: 2)
Apa yang dimaksud dengan **string slicing**? Berikan contoh `[start:stop:step]` dengan penjelasan.

**Kunci:** Slicing adalah cara mengambil sebagian string. Format: `string[start:stop:step]`. `start` = index mulai, `stop` = index akhir (tidak termasuk), `step` = langkah. Contoh: `"Python"[0:4]` → `"Pyth"` (index 0,1,2,3). `"Python"[::2]` → `"Pto"` (setiap 2 langkah).

---

## Modul 3: List & Tuple (12 Soal)

### PG-14
Manakah yang **benar** tentang list di Python?
a) List dimulai dari index 1  
b) List tidak bisa diubah setelah dibuat  
c) List bisa berisi berbagai tipe data ✅  
d) List menggunakan kurung biasa `()`

### PG-15
Apa output dari `[1, 2, 3, 4, 5][-1]`?
a) `1`  
b) `5` ✅  
c) `4`  
d) Error

### PG-16
Method untuk menambahkan item ke **akhir** list adalah...
a) `.add()`  
b) `.insert()`  
c) `.append()` ✅  
d) `.push()`

### PG-17
Apa output dari kode berikut?
```python
a = [1, 2, 3]
b = a
b[0] = 99
print(a[0])
```
a) `1`  
b) `99` ✅  
c) `[1, 2, 3]`  
d) Error

### PG-18
Perbedaan utama antara **list** dan **tuple** adalah...
a) List lebih cepat dari tuple  
b) Tuple bisa diubah, list tidak  
c) List bisa diubah, tuple tidak ✅  
d) Tuple menggunakan kurung siku

### PG-19
Apa output dari `len([1, [2, 3], 4])`?
a) `3` ✅  
b) `4`  
c) `2`  
d) Error

### C-04 (Bobot: 4)
Buat program yang:
1. Menerima 5 angka dari user (masukkan ke list)
2. Menampilkan: nilai tertinggi, terendah, rata-rata, jumlah

**Kunci:**
```python
angka = []
for i in range(5):
    n = int(input(f"Angka ke-{i+1}: "))
    angka.append(n)

print(f"Tertinggi: {max(angka)}")
print(f"Terendah: {min(angka)}")
print(f"Rata-rata: {sum(angka)/len(angka)}")
print(f"Jumlah: {sum(angka)}")
```

---

## Modul 4: Dictionary & Set (10 Soal)

### PG-20
Cara mengakses value dengan key `"nama"` dari dictionary `d = {"nama": "Budi", "umur": 17}` adalah...
a) `d["nama"]` ✅  
b) `d.0`  
c) `d[0]`  
d) `d("nama")`

### PG-21
Apa keuntungan menggunakan `.get()` dibanding `d[key]`?
a) `.get()` lebih cepat  
b) `.get()` tidak error jika key tidak ada ✅  
c) `.get()` hanya untuk string  
d) Tidak ada perbedaan

### PG-22
Apa output dari?
```python
d = {"a": 1, "b": 2}
print("c" in d)
```
a) `True`  
b) `False` ✅  
c) `None`  
d) Error

### PG-23
Method untuk mengambil **semua pasangan key-value** dari dictionary adalah...
a) `.keys()`  
b) `.values()`  
c) `.items()` ✅  
d) `.pairs()`

### PG-24
Set di Python digunakan untuk...
a) Menyimpan data berurutan  
b) Menyimpan data unik (tanpa duplikat) ✅  
c) Menyimpan data dengan key-value  
d) Menyimpan data yang bisa diubah

### C-05 (Bobot: 4)
Buat program **buku telepon** sederhana yang bisa menambah kontak (nama: nomor) dan menampilkan semua kontak.

**Kunci:**
```python
kontak = {}
while True:
    print("\n1. Tambah kontak")
    print("2. Lihat semua")
    print("3. Keluar")
    pilih = input("Pilihan: ")
    
    if pilih == "1":
        nama = input("Nama: ")
        nomor = input("Nomor: ")
        kontak[nama] = nomor
        print("Tersimpan!")
    elif pilih == "2":
        for nama, nomor in kontak.items():
            print(f"{nama}: {nomor}")
    elif pilih == "3":
        break
```

---

## Modul 5: Percabangan (12 Soal)

### PG-25
Apa output dari:
```python
x = 10
if x > 5:
    print("A")
else:
    print("B")
```
a) `A` ✅  
b) `B`  
c) Error  
d) Tidak ada output

### PG-26
Apa perbedaan `=` dan `==` di Python?
a) Sama saja  
b) `=` untuk assignment, `==` untuk perbandingan ✅  
c) `=` untuk perbandingan, `==` untuk assignment  
d) Keduanya bisa dipakai bergantian

### PG-27
Manakah yang akan menghasilkan `True`?
a) `True and False`  
b) `False or False`  
c) `not False` ✅  
d) `True and False or False`

### PG-28
Apa output dari kode berikut?
```python
nilai = 85
if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
else:
    grade = "D"
print(grade)
```
a) `A`  
b) `B` ✅  
c) `C`  
d) `D`

### PG-29
Nilai di Python yang dianggap **False** (falsy) adalah... (kecuali)
a) `0`  
b) `""` (string kosong)  
c) `"False"` ✅  
d) `None`

### PG-30
Apa output dari `print("A") if 5 > 3 else print("B")`?
a) `A` ✅  
b) `B`  
c) `True`  
d) Error

### C-06 (Bobot: 4)
Buat program yang menerima **3 nilai ujian** (MTK, IPA, ING). Syarat lulus: rata-rata >= 75 DAN tidak ada nilai di bawah 60. Tampilkan "Lulus" atau "Tidak lulus" beserta alasan.

**Kunci:**
```python
mtk = float(input("Nilai Matematika: "))
ipa = float(input("Nilai IPA: "))
ing = float(input("Nilai Inggris: "))
rata = (mtk + ipa + ing) / 3

if rata < 75:
    print(f"Tidak lulus. Rata-rata {rata:.1f} < 75")
elif mtk < 60 or ipa < 60 or ing < 60:
    print("Tidak lulus. Ada nilai di bawah 60")
else:
    print(f"Lulus! Rata-rata {rata:.1f}")
```

---

## Modul 6: Perulangan (12 Soal)

### PG-31
Apa output dari:
```python
for i in range(3):
    print(i, end=" ")
```
a) `1 2 3`  
b) `0 1 2` ✅  
c) `0 1 2 3`  
d) `1 2`

### PG-32
`for i in range(2, 8, 3)` akan menghasilkan urutan...
a) `2, 5, 8`  
b) `2, 5` ✅  
c) `2, 3, 4, 5, 6, 7`  
d) `2, 4, 6`

### PG-33
Apa fungsi `break` dalam perulangan?
a) Melanjutkan ke iterasi berikutnya  
b) Menghentikan perulangan sepenuhnya ✅  
c) Mengulang dari awal  
d) Melewatkan 1 iterasi

### PG-34
Apa output dari:
```python
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
```
a) `0 1 2` ✅  
b) `0 1 2 3`  
c) `0 1 2 4`  
d) `0 1 2 3 4`

### PG-35
Apa output dari:
```python
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
```
a) `0 1 2 4` ✅  
b) `0 1 2 3`  
c) `0 1 2 4 5`  
d) `0 1 2`

### PG-36
Manakah yang **paling tepat** menggunakan `while` loop?
a) Mencetak semua item dalam list  
b) Mencetak angka 1-10  
c) Meminta input sampai user menjawab benar ✅  
d) Menghitung jumlah karakter string

### C-07 (Bobot: 5)
Buat program **FizzBuzz** untuk angka 1-100:
- Kelipatan 3 → "Fizz"
- Kelipatan 5 → "Buzz"
- Kelipatan 3 dan 5 → "FizzBuzz"
- Selainnya → angka

**Kunci:**
```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

## Modul 7: Function (10 Soal)

### PG-37
Manakah penulisan fungsi yang benar?
a) `fungsi my_func():`  
b) `def my_func():` ✅  
c) `function my_func():`  
d) `func my_func():`

### PG-38
Apa output dari:
```python
def kali(a, b):
    return a * b
print(kali(3, 4))
```
a) `12` ✅  
b) `7`  
c) `34`  
d) Error

### PG-39
Apa yang terjadi jika fungsi tidak memiliki `return`?
a) Error  
b) Mengembalikan `None` ✅  
c) Mengembalikan `0`  
d) Tidak mengembalikan apa-apa

### PG-40
Manakah pernyataan yang **benar** tentang variabel lokal?
a) Bisa diakses di luar fungsi  
b) Hanya bisa diakses di dalam fungsi tempat ia didefinisikan ✅  
c) Selalu bisa diakses di semua fungsi  
d) Tidak bisa punya nama yang sama dengan variabel global

### PG-41
Apa output dari:
```python
def hitung(*args):
    return sum(args)
print(hitung(1, 2, 3, 4, 5))
```
a) `15` ✅  
b) `[1, 2, 3, 4, 5]`  
c) Error  
d) `10`

### C-08 (Bobot: 4)
Buat fungsi `luas_lingkaran(jari_jari)` yang mengembalikan luas lingkaran (π=3.14). Panggil dengan jari-jari 7 dan tampilkan hasilnya.

**Kunci:**
```python
def luas_lingkaran(r):
    return 3.14 * r * r

print(f"Luas lingkaran r=7: {luas_lingkaran(7)}")
```

---

## Modul 8: Error & Exception (8 Soal)

### PG-42
Apa jenis error jika kita membagi angka dengan nol?
a) `ValueError`  
b) `IndexError`  
c) `ZeroDivisionError` ✅  
d) `TypeError`

### PG-43
Apa output dari:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Error nih!")
```
a) Error program berhenti  
b) `Error nih!` ✅  
c) `inf`  
d) Tidak ada output

### PG-44
Blok `finally` pada try/except akan dijalankan ketika...
a) Hanya ketika tidak ada error  
b) Hanya ketika ada error  
c) Selalu, baik error maupun tidak ✅  
d) Tidak pernah dijalankan

### PG-45
Kita sengaja membuat error dengan perintah...
a) `error()`  
b) `raise` ✅  
c) `throw`  
d) `exception()`

### C-09 (Bobot: 3)
Buat fungsi `bagi(a, b)` yang menggunakan `try/except` untuk menangani:
- `ZeroDivisionError` → cetak "Tidak bisa membagi nol!"
- Input bukan angka → cetak "Input harus angka!"

**Kunci:**
```python
def bagi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Tidak bisa membagi nol!"
    except TypeError:
        return "Input harus angka!"

print(bagi(10, 2))   # 5.0
print(bagi(10, 0))   # Tidak bisa membagi nol!
print(bagi(10, "a")) # Input harus angka!
```

---

## Modul 9: File I/O (8 Soal)

### PG-46
Mode `"w"` saat membuka file berarti...
a) Membaca file  
b) Menulis file (menimpa) ✅  
c) Menulis file (menambah di akhir)  
d) Membaca dan menulis

### PG-47
Mode `"a"` saat membuka file berarti...
a) Membaca file  
b) Menulis file (menimpa)  
c) Append — menambah di akhir file ✅  
d) Membaca dan menulis

### PG-48
`with open("file.txt", "r") as f:` — Keuntungan menggunakan `with` adalah...
a) File otomatis ditutup setelah blok selesai ✅  
b) File tidak perlu dibuat  
c) File bisa dibaca lebih cepat  
d) Tidak perlu import apa-apa

### C-10 (Bobot: 4)
Buat program yang:
1. Menerima input nama file dari user
2. Menerima input teks
3. Menyimpan teks ke file (append)
4. Membaca dan menampilkan semua isi file

**Kunci:**
```python
nama_file = input("Nama file: ")
teks = input("Teks yang akan disimpan: ")

with open(nama_file, "a") as f:
    f.write(teks + "\n")

print("\nIsi file:")
with open(nama_file, "r") as f:
    print(f.read())
```

---

## Modul 10: Module & pip (6 Soal)

### PG-49
Perintah untuk menginstall package Python adalah...
a) `python install`  
b) `pip install` ✅  
c) `get install`  
d) `package install`

### PG-50
Fungsi `randint(1, 10)` berasal dari modul...
a) `math`  
b) `random` ✅  
c) `sys`  
d) `os`

### PG-51
`if __name__ == "__main__":` digunakan untuk...
a) Membuat program berjalan lebih cepat  
b) Mengecek apakah file dijalankan langsung atau di-import ✅  
c) Memberi nama pada program  
d) Mengambil argumen dari command line

### C-11 (Bobot: 3)
Buat module sederhana `operasi.py` berisi fungsi `tambah(a,b)` dan `kali(a,b)`. Lalu buat `main.py` yang mengimport dan menggunakannya.

**Kunci:**
```python
# operasi.py
def tambah(a, b):
    return a + b
def kali(a, b):
    return a * b

# main.py
import operasi
print(operasi.tambah(5, 3))  # 8
print(operasi.kali(5, 3))    # 15
```

---

## Modul 11: List Comprehension (6 Soal)

### PG-52
List comprehension `[x**2 for x in range(5)]` menghasilkan...
a) `[0, 1, 4, 9, 16]` ✅  
b) `[1, 4, 9, 16, 25]`  
c) `[0, 1, 2, 3, 4]`  
d) `[25, 16, 9, 4, 1]`

### PG-53
List comprehension untuk mengambil angka genap dari 0-20 adalah...
a) `[x for x in range(21) if x % 2 == 0]` ✅  
b) `[x for x in range(0, 20, 2)]`  
c) `[x for x in range(21) if x % 2]`  
d) a dan b benar

### PG-54
Lambda adalah...
a) Fungsi dengan nama panjang  
b) Fungsi anonim (tanpa nama) ✅  
c) Tipe data khusus  
d) Method untuk list

### C-12 (Bobot: 4)
Gunakan **list comprehension** untuk membuat list berisi kuadrat dari bilangan genap antara 1-20. Tampilkan hasilnya.

**Kunci:**
```python
hasil = [x**2 for x in range(1, 21) if x % 2 == 0]
print(hasil)
# [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
```

---

## Modul 12: OOP (8 Soal)

### PG-55
Apa itu **class** di Python?
a) Sebuah fungsi khusus  
b) Blueprint/cetakan untuk membuat object ✅  
c) Tipe data untuk angka  
d) Sebuah module

### PG-56
Method `__init__` dipanggil ketika...
a) Object dihapus  
b) Class didefinisikan  
c) Object dibuat ✅  
d) Method lain dipanggil

### PG-57
Parameter pertama di setiap method instance adalah...
a) `cls`  
b) `this`  
c) `self` ✅  
d) `object`

### PG-58
Apa output dari:
```python
class Siswa:
    sekolah = "SMA 1"
    def __init__(self, nama):
        self.nama = nama

s = Siswa("Budi")
print(s.sekolah)
```
a) `Budi`  
b) `SMA 1` ✅  
c) Error  
d) `sekolah`

### C-13 (Bobot: 5)
Buat class `Buku` dengan atribut: `judul`, `penulis`, `tahun`, `dipinjam` (default False). Method:
- `info()` → return string informasi buku
- `pinjam()` → ubah status, return "Buku dipinjam"
- `kembalikan()` → ubah status, return "Buku dikembalikan"

**Kunci:**
```python
class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.dipinjam = False
    
    def info(self):
        status = "Dipinjam" if self.dipinjam else "Tersedia"
        return f"{self.judul} - {self.penulis} ({self.tahun}) - {status}"
    
    def pinjam(self):
        self.dipinjam = True
        return "Buku dipinjam"
    
    def kembalikan(self):
        self.dipinjam = False
        return "Buku dikembalikan"

# Test
b = Buku("Python 101", "Budi", 2024)
print(b.info())
print(b.pinjam())
print(b.info())
```

---

## Soal Campuran (10 Soal)

### PG-59 (Campuran)
Manakah yang **bukan** tipe data bawaan Python?
a) `list`  
b) `dict`  
c) `array` ✅  
d) `tuple`

### PG-60 (Campuran)
Apa output dari?
```python
data = {"a": [1, 2], "b": [3, 4]}
print(data["a"][1])
```
a) `1`  
b) `2` ✅  
c) `[1, 2]`  
d) Error

### C-14 (Bobot: 5 — Campuran)
Buat program yang membaca file `nilai.txt` (format: `Nama|Nilai` per baris), lalu menampilkan:
- Daftar siswa dengan nilai dan status lulus/tidak
- Rata-rata kelas
- Jumlah siswa lulus

Contoh isi `nilai.txt`:
```
Budi|85
Ani|92
Citra|45
```

**Kunci:**
```python
siswa = []
with open("nilai.txt", "r") as f:
    for baris in f:
        nama, nilai = baris.strip().split("|")
        siswa.append({"nama": nama, "nilai": int(nilai)})

total = 0
lulus = 0
for s in siswa:
    status = "Lulus" if s["nilai"] >= 75 else "Tidak lulus"
    print(f"{s['nama']}: {s['nilai']} - {status}")
    total += s["nilai"]
    if s["nilai"] >= 75:
        lulus += 1

rata = total / len(siswa)
print(f"\nRata-rata kelas: {rata:.1f}")
print(f"Jumlah lulus: {lulus}/{len(siswa)}")
```

### E-03 (Bobot: 3 — Campuran)
Jelaskan perbedaan antara **list**, **tuple**, dan **dictionary** di Python. Kapan sebaiknya menggunakan masing-masing?

**Kunci:**
- **List** `[]`: Kumpulan data berurutan yang bisa diubah (mutable). Cocok untuk daftar yang berubah-ubah (daftar siswa, nilai).
- **Tuple** `()`: Kumpulan data berurutan yang tidak bisa diubah (immutable). Cocok untuk data tetap (hari dalam seminggu, koordinat).
- **Dictionary** `{}`: Kumpulan pasangan key-value. Cocok untuk data yang punya label/nama (data siswa dengan field nama, kelas, nilai).

---

## 📊 Kunci Jawaban Cepat

| No | Kunci | No | Kunci | No | Kunci | No | Kunci |
|----|-------|----|-------|----|-------|----|-------|
| 1 | C | 16 | C | 31 | B | 46 | B |
| 2 | B | 17 | B | 32 | B | 47 | C |
| 3 | C | 18 | C | 33 | B | 48 | A |
| 4 | B | 19 | A | 34 | A | 49 | B |
| 5 | B | 20 | A | 35 | A | 50 | B |
| 6 | B | 21 | B | 36 | C | 51 | B |
| 7 | B | 22 | B | 37 | B | 52 | A |
| 8 | C | 23 | C | 38 | A | 53 | D |
| 9 | B | 24 | B | 39 | B | 54 | B |
| 10 | C | 25 | A | 40 | B | 55 | B |
| 11 | A | 26 | B | 41 | A | 56 | C |
| 12 | A | 27 | C | 42 | C | 57 | C |
| 13 | B | 28 | B | 43 | B | 58 | B |
| 14 | C | 29 | C | 44 | C | 59 | C |
| 15 | B | 30 | A | 45 | B | 60 | B |

---

## 📝 Lembar Jawab Siswa (Copy & Print)

```
Nama: _____________________   Kelas: ___________   Tanggal: ___________

 1. ___    11. ___    21. ___    31. ___    41. ___    51. ___
 2. ___    12. ___    22. ___    32. ___    42. ___    52. ___
 3. ___    13. ___    23. ___    33. ___    43. ___    53. ___
 4. ___    14. ___    24. ___    34. ___    44. ___    54. ___
 5. ___    15. ___    25. ___    35. ___    45. ___    55. ___
 6. ___    16. ___    26. ___    36. ___    46. ___    56. ___
 7. ___    17. ___    27. ___    37. ___    47. ___    57. ___
 8. ___    18. ___    28. ___    38. ___    48. ___    58. ___
 9. ___    19. ___    29. ___    39. ___    49. ___    59. ___
10. ___    20. ___    30. ___    40. ___    50. ___    60. ___

Skor: ___ / 60
```
