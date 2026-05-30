# Modul 12: OOP Dasar (Object-Oriented Programming)

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjelaskan **Class** dan **Object** ke murid dengan analogi
- Membuat class sendiri dengan atribut dan method
- Memahami `__init__` (constructor) dan `self`
- Menggunakan **inheritance** sederhana
- Memahami **encapsulation** dasar

---

## 1. Analogi: Class itu Cetakan, Object itu Kue

Ini cara paling mudah ngajar OOP ke murid:

> **Class** = cetakan kue. **Object** = kue yang sudah jadi.

```
      Cetakan (Class)                Kue (Object)
   ┌──────────────────┐          ┌──────────────────┐
   │ Bentuk: Bintang   │          │ ★ Bintang ke-1   │
   │ Warna: (isi nanti)│   →     │ Warna: Merah      │
   │ Rasa: (isi nanti) │          │ Rasa: Coklat      │
   └──────────────────┘          ├──────────────────┤
                                  │ ★ Bintang ke-2   │
                                  │ Warna: Biru       │
                                  │ Rasa: Vanilla     │
                                  └──────────────────┘
```

- **Class** = blueprint / cetakan — mendefinisikan **atribut** (data) dan **method** (fungsi)
- **Object** = instance dari class — wujud nyata dengan data spesifik

## 2. Class Sederhana

```python
# Definisi class
class Siswa:
    """Class untuk merepresentasikan siswa"""
    pass  # Isi dulu kosong

# Membuat object dari class
s1 = Siswa()
s2 = Siswa()

print(type(s1))  # <class '__main__.Siswa'>
print(s1)        # <__main__.Siswa object at 0x...>
```

> 💡 `pass` digunakan saat class belum punya isi (placeholder).

## 3. Menambah Atribut

Atribut = **data** yang dimiliki object.

```python
class Siswa:
    pass

# Membuat object
s1 = Siswa()
s2 = Siswa()

# Menambah atribut secara manual (kurang praktis)
s1.nama = "Budi Santoso"
s1.kelas = "XII IPA 1"
s1.nilai = 85

s2.nama = "Ani Wijaya"
s2.kelas = "XII IPA 1"
s2.nilai = 92

print(f"{s1.nama} - {s1.kelas} - {s1.nilai}")
print(f"{s2.nama} - {s2.kelas} - {s2.nilai}")
```

Cara diatas **kurang praktis** — kita harus ngetik manual setiap kali. Solusi: `__init__`

## 4. __init__ — Constructor (Paling Penting!)

`__init__` adalah method spesial yang otomatis dipanggil saat object dibuat. Digunakan untuk **mengisi data awal**.

```python
class Siswa:
    def __init__(self, nama, kelas, nilai):
        """Constructor: dipanggil otomatis saat bikin object"""
        self.nama = nama    # self.nama = atribut
        self.kelas = kelas  # parameter 'nama' = input
        self.nilai = nilai
    
    def perkenalan(self):
        """Method: fungsi yang dimiliki object"""
        return f"Halo, saya {self.nama} dari {self.kelas}"

# Membuat object — __init__ dipanggil otomatis
s1 = Siswa("Budi Santoso", "XII IPA 1", 85)
s2 = Siswa("Ani Wijaya", "XII IPA 1", 92)

# Akses atribut
print(s1.nama)     # Budi Santoso
print(s2.nilai)    # 92

# Panggil method
print(s1.perkenalan())  # Halo, saya Budi Santoso dari XII IPA 1
```

### Penjelasan `self`

- `self` adalah **referensi ke object itu sendiri**
- Wajib sebagai parameter **pertama** di setiap method
- Kamu tidak perlu mengirim `self` saat memanggil — Python otomatis

```python
# Di dalam class, 'self' merujuk ke object yang sedang diproses
s1 = Siswa("Budi", "XII IPA 1", 85)
# Saat __init__ jalan, self = s1
# Jadi: self.nama = "Budi" → s1.nama = "Budi"
```

> 🏆 **Poin ngajar:** `self` itu seperti kata "saya" — setiap object bicara tentang dirinya sendiri.

## 5. Method — Fungsi di Dalam Class

Method adalah fungsi yang **dimiliki oleh object**.

```python
class Siswa:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai
        self.aktif = True  # Default semua aktif
    
    def perkenalan(self):
        return f"{self.nama} dari {self.kelas}"
    
    def info_nilai(self):
        return f"Nilai {self.nama}: {self.nilai}"
    
    def lulus(self):
        return self.nilai >= 75
    
    def nonaktifkan(self):
        self.aktif = False
        return f"{self.nama} telah dinonaktifkan"
    
    def __str__(self):
        """Method spesial: representasi string object"""
        return f"Siswa({self.nama}, {self.kelas}, {self.nilai})"

# Test
s = Siswa("Budi", "XII IPA 1", 85)
print(s.perkenalan())       # Budi dari XII IPA 1
print(s.info_nilai())       # Nilai Budi: 85
print(s.lulus())            # True
print(s)                    # Siswa(Budi, XII IPA 1, 85)
print(s.nonaktifkan())      # Budi telah dinonaktifkan
print(s.aktif)              # False
```

### Method Spesial (Magic Methods)

| Method | Kegunaan |
|--------|----------|
| `__init__(self, ...)` | Constructor — inisialisasi object |
| `__str__(self)` | Representasi string (dipanggil oleh `print()`) |
| `__len__(self)` | Dipanggil oleh `len(object)` |
| `__repr__(self)` | Representasi untuk debugging |

```python
class Buku:
    def __init__(self, judul, penulis, halaman):
        self.judul = judul
        self.penulis = penulis
        self.halaman = halaman
    
    def __str__(self):
        return f"'{self.judul}' oleh {self.penulis}"
    
    def __len__(self):
        return self.halaman

b = Buku("Python untuk Guru", "Sisyphus", 200)
print(b)    # 'Python untuk Guru' oleh Sisyphus
print(len(b))  # 200
```

## 6. Class Variable vs Instance Variable

### Instance Variable — milik masing-masing object

```python
class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama      # Instance variable — berbeda tiap object
        self.nilai = nilai

s1 = Siswa("Budi", 85)
s2 = Siswa("Ani", 92)
print(s1.nama)  # Budi
print(s2.nama)  # Ani — beda!
```

### Class Variable — milik semua object (sama)

```python
class Siswa:
    # Class variable — SAMA untuk semua object
    sekolah = "SMA Negeri 1"
    tahun_ajaran = "2025/2026"
    
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai
    
    def info(self):
        return f"{self.nama} - {self.sekolah} - {self.nilai}"

s1 = Siswa("Budi", 85)
s2 = Siswa("Ani", 92)

print(s1.info())  # Budi - SMA Negeri 1 - 85
print(s2.info())  # Ani - SMA Negeri 1 - 92

# Ubah class variable
Siswa.sekolah = "SMA Negeri 2"
print(s1.info())  # Budi - SMA Negeri 2 - 85 — berubah semua!
```

## 7. Inheritance (Pewarisan)

Inheritance = **class anak mewarisi atribut & method dari class induk**.

```python
# Class induk (parent)
class AnggotaSekolah:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def perkenalan(self):
        return f"Halo, saya {self.nama}, umur {self.umur}"
    
    def __str__(self):
        return f"{self.nama} ({self.umur})"

# Class anak (child) — mewarisi AnggotaSekolah
class Siswa(AnggotaSekolah):
    def __init__(self, nama, umur, kelas, nilai):
        super().__init__(nama, umur)  # Panggil constructor parent
        self.kelas = kelas
        self.nilai = nilai
    
    def lulus(self):
        return self.nilai >= 75
    
    # Override method perkenalan
    def perkenalan(self):
        return f"Halo, saya {self.nama}, siswa kelas {self.kelas}"

# Class anak lain
class Guru(AnggotaSekolah):
    def __init__(self, nama, umur, mapel):
        super().__init__(nama, umur)
        self.mapel = mapel
    
    def mengajar(self):
        return f"{self.nama} mengajar {self.mapel}"

# Test
s = Siswa("Budi", 17, "XII IPA 1", 85)
g = Guru("Pak Ahmad", 35, "Matematika")

print(s.perkenalan())        # Halo, saya Budi, siswa kelas XII IPA 1
print(g.perkenalan())        # Halo, saya Pak Ahmad, umur 35 (dari parent)
print(g.mengajar())          # Pak Ahmad mengajar Matematika
print(s.lulus())             # True
print(isinstance(s, Siswa))  # True
print(isinstance(s, AnggotaSekolah))  # True — karena warisan!
```

### Kenapa Inheritance?

```python
# Tanpa inheritance — duplikasi kode
class Siswa:
    def __init__(self, nama, umur, kelas):
        self.nama = nama
        self.umur = umur
        self.kelas = kelas

class Guru:
    def __init__(self, nama, umur, mapel):
        self.nama = nama
        self.umur = umur
        self.mapel = mapel
    # ↑ Duplikasi! nama dan umur di kedua class

# Dengan inheritance — kode lebih kering
class AnggotaSekolah:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

class Siswa(AnggotaSekolah):
    def __init__(self, nama, umur, kelas):
        super().__init__(nama, umur)
        self.kelas = kelas

class Guru(AnggotaSekolah):
    def __init__(self, nama, umur, mapel):
        super().__init__(nama, umur)
        self.mapel = mapel
```

## 8. Encapsulation Sederhana

Encapsulation = **menyembunyikan data** internal object. Di Python, dikasih tahu dengan **underscore**.

```python
class RekeningBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self._saldo = saldo_awal     # _ = "protected" (sebaiknya tidak langsung diakses)
        self.__pin = "1234"          # __ = "private" (name mangling)
    
    def cek_saldo(self):
        """Method publik — akses yang aman"""
        return f"Saldo {self.pemilik}: Rp{self._saldo:,}"
    
    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah
            return f"Setor Rp{jumlah:,} berhasil"
        return "Jumlah tidak valid"
    
    def tarik(self, jumlah, pin):
        if pin != self.__pin:
            return "PIN salah!"
        if jumlah > self._saldo:
            return "Saldo tidak mencukupi"
        self._saldo -= jumlah
        return f"Tarik Rp{jumlah:,} berhasil"

r = RekeningBank("Budi", 1000000)
print(r.cek_saldo())         # Saldo Budi: Rp1,000,000
print(r.setor(500000))       # Setor Rp500,000 berhasil
print(r.tarik(200000, "1234"))  # Tarik Rp200,000 berhasil
print(r.tarik(999999999, "0000"))  # PIN salah!

# Akses langsung — "bisa" tapi tidak disarankan
print(r._saldo)   # 1300000 — bisa, tapi tandanya internal
# print(r.__pin)  # ❌ AttributeError — name mangling!
```

> 💡 **Di Python:** Tidak ada `private` sejati. `_` dan `__` adalah **konvensi** (kesepakatan programmer) untuk bilang: "ini internal, jangan disentuh dari luar."

---

## 🧪 Latihan Modul 12

### Latihan 1: Class Buku Perpustakaan

```python
# Buat class Buku dengan:
# Atribut: judul, penulis, tahun, dipinjam (bool, default False)
# Method:
#   info() → return string informasi buku
#   pinjam() → set dipinjam=True, return "Buku dipinjam"
#   kembalikan() → set dipinjam=False, return "Buku dikembalikan"
# __str__ → representasi string

# Buat 3 object buku, pinjam 1 buku, tampilkan info semua
```

### Latihan 2: Class NilaiSiswa

```python
# Buat class NilaiSiswa dengan:
# Atribut: nama, mtk, ipa, ing, bahasa
# Method:
#   rata_rata() → return float
#   grade() → return A/B/C/D/E
#   lulus() → True/False (rata-rata >= 75)
#   laporan() → string laporan lengkap (format rapi)
#
# Buat 5 object, tampilkan laporan masing-masing
```

### Latihan 3: Inheritance — Hewan

```python
# Class induk: Hewan
#   __init__(self, nama, umur)
#   bersuara() → return "..."
#
# Class anak: Kucing (miaow), Anjing (guk guk), Bebek (kwek kwek)
#   override method bersuara()
#
# Buat list berisi berbagai hewan
# Loop dan panggil bersuara() masing-masing
# (Ini contoh POLYMORPHISM — beda class, method sama, hasil beda)
```

### Latihan 4: Sistem Sekolah Mini

```python
# Buat sistem kelas dengan:
# - class AnggotaSekolah (induk)
# - class Siswa (anak) — tambah: kelas, daftar_nilai
# - class Guru (anak) — tambah: mapel, ruangan
#
# Method di Siswa:
#   tambah_nilai(mapel, nilai)
#   rata_rata()
#   laporan()
#
# Method di Guru:
#   info_mengajar()
#
# Buat 3 siswa dan 2 guru, simpan di list, tampilkan semua info
```

---

## ✅ Checklist Paham

- [ ] Saya bisa jelasin beda Class vs Object dengan analogi
- [ ] Saya bisa bikin class dengan `__init__` dan method
- [ ] Saya paham `self` — merujuk ke object sendiri
- [ ] Saya bisa bikin inheritance (`class Anak(Ibu):`)
- [ ] Saya paham `super().__init__()` untuk panggil constructor parent
- [ ] Saya paham konsep class variable vs instance variable
- [ ] Saya paham encapsulation (`_` untuk protected)

**Kalau semua checklist tercentang → lanjut ke Modul 13 (Proyek Akhir).**
