# Modul 4: Dictionary & Set

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Membuat dan menggunakan **dictionary** (key-value)
- Memilih kapan pakai list vs dictionary
- Menggunakan method-method dictionary
- Memahami **set** untuk data unik
- Membuat **nested dictionary** (data kompleks)

---

## 1. Apa Itu Dictionary?

Dictionary = kumpulan **pasangan key-value**. Seperti buku telepon: cari nama (key) → dapat nomor (value).

```python
# Sintaks: {key1: value1, key2: value2, ...}
siswa = {
    "nama": "Budi Santoso",
    "kelas": "XII IPA 1",
    "usia": 17,
    "lulus": False
}

# Mengakses value
print(siswa["nama"])      # Budi Santoso
print(siswa["kelas"])     # XII IPA 1
# print(siswa["alamat"])  ❌ KeyError! Key tidak ada

# Mengakses dengan .get() — aman (tidak error kalau key tdk ada)
print(siswa.get("nama"))     # Budi Santoso
print(siswa.get("alamat"))   # None (tidak error)
print(siswa.get("alamat", "Tidak ada"))  # "Tidak ada" — default value
```

> 💡 **Key harus unik.** Kalau kamu pakai key yang sama dua kali, value terakhir yang dipakai.

### Kenapa Pake Dictionary?

| Situasi | Pakai |
|---------|-------|
| Data punya label/nama | Dictionary |
| Data cuma urutan | List |
| Contoh: data siswa | `{"nama": "Budi", "nilai": 85}` |
| Contoh: daftar nilai | `[85, 92, 78]` |

## 2. Method-Method Dictionary

```python
siswa = {"nama": "Budi", "kelas": "XII IPA 1", "usia": 17}

# Menambah/mengubah
siswa["alamat"] = "Jakarta"       # Tambah key baru
siswa["usia"] = 18                # Ubah key yang sudah ada
siswa.update({"nilai": 88, "kelas": "XII IPA 2"})  # Update multiple keys

print(siswa)
# {'nama': 'Budi', 'kelas': 'XII IPA 2', 'usia': 18, 'alamat': 'Jakarta', 'nilai': 88}

# Menghapus
del siswa["alamat"]               # Hapus key tertentu
nilai = siswa.pop("nilai")        # Hapus & return value
siswa.clear()                     # Hapus semua

# Melihat isi
siswa = {"nama": "Budi", "kelas": "XII IPA 1", "usia": 17}

print(siswa.keys())     # dict_keys(['nama', 'kelas', 'usia'])
print(siswa.values())   # dict_values(['Budi', 'XII IPA 1', 17])
print(siswa.items())    # dict_items([('nama', 'Budi'), ...])

# Cek keberadaan key
print("nama" in siswa)      # True
print("alamat" in siswa)    # False
```

### Method Penting

| Method | Fungsi |
|--------|--------|
| `.get(key, default)` | Ambil value, kalau gak ada return default |
| `.keys()` | Daftar semua key |
| `.values()` | Daftar semua value |
| `.items()` | Daftar pasangan (key, value) |
| `.update(dict2)` | Gabung dictionary lain |
| `.pop(key)` | Hapus dan return value |

## 3. Looping Dictionary

```python
siswa = {"nama": "Budi", "kelas": "XII IPA 1", "usia": 17}

# Loop key saja
for key in siswa:
    print(key)       # nama, kelas, usia

# Loop value saja
for value in siswa.values():
    print(value)     # Budi, XII IPA 1, 17

# Loop key dan value 🔥
for key, value in siswa.items():
    print(f"{key}: {value}")
```

> 💡 **`items()`** adalah cara paling Pythonic untuk loop dictionary. Biasakan.

## 4. Nested Dictionary — Dictionary di Dalam Dictionary

Ini sangat berguna untuk data kompleks seperti data siswa:

```python
# Satu dictionary besar berisi data kelas
kelas = {
    "siswa1": {
        "nama": "Budi Santoso",
        "nilai": {"mtk": 85, "ipa": 90, "inggris": 78},
        "aktif": True
    },
    "siswa2": {
        "nama": "Ani Wijaya",
        "nilai": {"mtk": 92, "ipa": 88, "inggris": 95},
        "aktif": True
    },
    "siswa3": {
        "nama": "Citra Dewi",
        "nilai": {"mtk": 76, "ipa": 80, "inggris": 82},
        "aktif": False
    }
}

# Cara akses
print(kelas["siswa1"]["nama"])                # Budi Santoso
print(kelas["siswa2"]["nilai"]["mtk"])        # 92
print(kelas["siswa3"]["aktif"])               # False

# Loop semua siswa
for id_siswa, data in kelas.items():
    if data["aktif"]:
        rata = sum(data["nilai"].values()) / len(data["nilai"])
        print(f"{data['nama']}: rata-rata {rata:.1f}")
```

> 🏆 Ini pola yang akan kamu pakai terus — data siswa nested dictionary. Kuasai.

## 5. Set — Kumpulan Data Unik

Set mirip list, tapi:
- **Tidak berurutan** (no index)
- **Semua elemen unik** (tidak ada duplikat)
- **Mutable** (bisa ditambah/dihapus)

```python
# Set dibuat dengan kurung kurawal {} TANPA key-value
warna = {"merah", "biru", "hijau", "merah", "biru"}
print(warna)  # {'hijau', 'merah', 'biru'} — duplikat hilang!

# Atau dari list
angka = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unik = set(angka)
print(unik)   # {1, 2, 3, 4, 5}

# Set tidak punya index
# print(warna[0])  ❌ TypeError!

# Operasi Set (ini yang bikin set berguna)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union: {1, 2, 3, 4, 5, 6} — gabung
print(a & b)   # Intersection: {3, 4} — irisan
print(a - b)   # Difference: {1, 2} — di a tapi tidak di b
print(a ^ b)   # Symmetric diff: {1, 2, 5, 6} — tidak di kedua-duanya
```

### Kapan Pakai Set?

```python
# Menghapus duplikat dari list
nama_siswa = ["Budi", "Ani", "Budi", "Citra", "Ani", "Dedi"]
unik = list(set(nama_siswa))
print(unik)  # ['Citra', 'Dedi', 'Budi', 'Ani']

# Cek anggota (ini CEPAT banget)
print("Budi" in unik)   # True — O(1), lebih cepat dari list
```

---

## 🧪 Latihan Modul 4

### Latihan 1: Data Siswa

```python
# 1. Buat dictionary untuk 3 siswa dengan key: nama, kelas, nilai (int)
# 2. Tampilkan nama dan nilai masing-masing
# 3. Hitung rata-rata nilai semua siswa
```

### Latihan 2: Buku Telepon

```python
# Program buku telepon sederhana:
# - Simpan kontak (nama: nomor telepon)
# - User bisa:
#   • tambah kontak
#   • cari kontak (input nama → tampil nomor)
#   • hapus kontak
#   • lihat semua kontak
#   • keluar
```

### Latihan 3: Analisis Nilai dengan Nested Dict

```python
kelas = {
    "Budi": {"mtk": 85, "ipa": 90, "inggris": 78},
    "Ani": {"mtk": 92, "ipa": 88, "inggris": 95},
    "Citra": {"mtk": 76, "ipa": 80, "inggris": 82}
}

# Cetak:
# Nama | MTK | IPA | ING | Rata-rata
# --------------------------------------
# Budi |  85 |  90 |  78 |     84.3
# Ani  |  92 |  88 |  95 |     91.7
# Citra|  76 |  80 |  82 |     79.3
# --------------------------------------
# Rata-rata kelas per mapel: MTK=..., IPA=..., ING=...
```

### Latihan 4: Set — Hobi Siswa

```python
# Dua kelompok siswa dengan hobinya:
kelas_a = {"membaca", "olahraga", "melukis", "musik", "menari"}
kelas_b = {"musik", "memasak", "olahraga", "fotografi", "menari"}

# Tentukan:
# - Hobi yang dimiliki kedua kelas
# - Hobi yang hanya dimiliki kelas A
# - Hobi yang hanya dimiliki kelas B
# - Semua hobi unik dari kedua kelas
```

---

## ✅ Checklist Paham

- [ ] Saya bisa bikin dictionary dan akses value-nya
- [ ] Saya paham beda `dict["key"]` vs `dict.get("key")`
- [ ] Saya bisa loop dictionary dengan `.items()`
- [ ] Saya bisa bikin nested dictionary
- [ ] Saya paham kapan pake list vs dictionary
- [ ] Saya bisa bikin set dan paham kegunaannya (unik, operasi himpunan)

**Kalau semua checklist tercentang → lanjut ke Modul 5.**
