# Modul 5: Percabangan (Conditional)

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Membuat logika `if/elif/else` untuk berbagai situasi
- Menjelaskan **flowchart** percabangan ke murid
- Menggunakan operator perbandingan dan logika
- Membuat nested conditionals
- Menggunakan ternary untuk kondisi sederhana

---

## 1. Operator Perbandingan

Percabangan selalu melibatkan **perbandingan**. Ini operatornya:

| Operator | Arti | Contoh | Hasil |
|----------|------|--------|-------|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama | `5 <= 3` | `False` |

```python
nilai = 85
print(nilai > 75)    # True
print(nilai == 100)  # False
print(nilai != 50)   # True
```

> ⚠️ **Ini error paling umum murid:** `=` vs `==`
> - `=` adalah **assignment** (isi nilai): `x = 5`
> - `==` adalah **perbandingan**: `x == 5`
> - Salah tulis `if x = 5:` → error SyntaxError!

## 2. If/Else — Struktur Dasar

```python
nilai = 85

if nilai >= 75:
    print("Lulus! 🎉")
else:
    print("Tidak lulus. 😢")
```

### Bagaimana Cara Kerjanya?

```
          ┌─────────┐
          │  nilai  │
          │ >= 75?  │
          └────┬────┘
               │
        ┌──────┴──────┐
       Ya             Tidak
        │              │
   ┌────┴────┐    ┌───┴───┐
   │ "Lulus" │    │"Tidak"│
   └─────────┘    └───────┘
```

> 🏆 **Buat ngajar:** Selalu gambar flowchart dulu sebelum nulis kode. Murid akan lebih paham alur logikanya.

### If/Elif/Else — Banyak Kondisi

```python
nilai = 85

if nilai >= 90:
    grade = "A"
elif nilai >= 80:
    grade = "B"
elif nilai >= 70:
    grade = "C"
elif nilai >= 60:
    grade = "D"
else:
    grade = "E"

print(f"Nilai: {nilai}, Grade: {grade}")  # Nilai: 85, Grade: B
```

### Bagaimana Python Mengeksekusi?

Python cek **dari atas ke bawah**. Kondisi pertama yang `True` akan dijalankan, sisanya dilewati.

```python
# ⚠️ Urutan penting! Kalau ditukar, hasilnya beda:
nilai = 85

# SALAH
if nilai >= 70:      # Ini True (85>=70)
    grade = "C"      # ⚠️ Berhenti di sini!
elif nilai >= 80:    # Tidak pernah dicek
    grade = "B"
elif nilai >= 90:
    grade = "A"
# Hasil: C — padahal seharusnya B!
```

> 💡 **Aturan:** Urutkan dari kondisi **paling spesifik** ke **paling umum**.

## 3. Operator Logika (Boolean)

Kita bisa gabung beberapa kondisi dengan `and`, `or`, `not`:

### AND — Keduanya harus True

```python
usia = 17
lulus = True

if usia >= 16 and lulus:
    print("Bisa ikut ujian praktek")
else:
    print("Belum bisa ikut")
```

### OR — Salah satu True

```python
hari = "Sabtu"

if hari == "Sabtu" or hari == "Minggu":
    print("Libur! 🎉")
else:
    print("Masuk sekolah")
```

### NOT — Membalik

```python
cuaca_hujan = False

if not cuaca_hujan:
    print("Boleh olahraga di luar")
```

### Kombinasi

```python
nilai = 85
absen = 90
izin = False

if nilai >= 75 and absen >= 80 and not izin:
    print("Lulus sempurna")
elif nilai >= 75 and absen >= 80:
    print("Lulus")
elif nilai >= 75:
    print("Lulus bersyarat — perbaiki absen")
else:
    print("Tidak lulus")
```

### Tabel Kebenaran (Truth Table)

Ini penting buat ngajar:

| A | B | A and B | A or B | not A |
|---|---|---------|--------|-------|
| T | T | T | T | F |
| T | F | F | T | F |
| F | T | F | T | T |
| F | F | F | F | T |

## 4. Truthy dan Falsy — Konsep Penting

Di Python, setiap nilai bisa dianggap `True` atau `False` dalam konteks boolean:

```python
# Nilai yang dianggap False (Falsy):
bool(0)         # False
bool(0.0)       # False
bool("")        # False — string kosong
bool([])        # False — list kosong
bool({})        # False — dict kosong
bool(None)      # False

# Semua yang lain = Truthy (dianggap True)
bool(1)         # True
bool(-1)        # True
bool("Python")  # True
bool([0])       # True — list isi 0, tapi list-nya tidak kosong
```

Ini berguna untuk penulisan kode yang lebih singkat:

```python
nama = input("Masukkan nama: ")

# Daripada:
if nama != "":
    print(f"Halo {nama}")

# Lebih Pythonic:
if nama:  # True kalau string tidak kosong
    print(f"Halo {nama}")
```

> 💡 **Poin ngajar:** "Semua yang 'kosong' dianggap False: 0, string kosong, list kosong, None. Ini membuat kode lebih bersih."

## 5. Nested Conditionals (Bersarang)

Kondisi di dalam kondisi:

```python
usia = 17
lulus = True
nilai = 85

if usia >= 16:
    print("Syarat usia terpenuhi")
    
    if lulus:
        print("Syarat kelulusan terpenuhi")
        
        if nilai >= 80:
            print("Selamat! Dapat sertifikat dengan pujian")
        else:
            print("Dapat sertifikat")
    else:
        print("Tidak lulus — tidak dapat sertifikat")
else:
    print("Belum memenuhi syarat usia")
```

> ⚠️ **Hati-hati dengan nested yang terlalu dalam.** Kalau sudah 3 level nested, sebaiknya disederhanakan (nanti di modul function).

## 6. Ternary (One-liner Condition)

Untuk kondisi sederhana, Python punya **ternary operator**:

```python
# Format: hasil_jika_true if kondisi else hasil_jika_false

# Daripada:
nilai = 85
if nilai >= 75:
    status = "Lulus"
else:
    status = "Tidak lulus"

# Lebih ringkas:
status = "Lulus" if nilai >= 75 else "Tidak lulus"
print(status)  # Lulus
```

Cocok untuk assignment sederhana. Tapi jangan dipaksakan untuk kondisi kompleks.

## 7. Match/Case (Python 3.10+) — Alternatif Switch

Python versi baru punya `match/case` seperti switch di bahasa lain:

```python
# Cocok untuk banyak kondisi dengan nilai tertentu
hari = 3

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case _:  # Default
        print("Akhir pekan")
```

```python
# Match dengan kondisi
nilai = 85
match nilai:
    case n if n >= 90:
        grade = "A"
    case n if n >= 80:
        grade = "B"
    case n if n >= 70:
        grade = "C"
    case _:
        grade = "D"
print(grade)  # B
```

> 💡 `match/case` masih baru. Kalau Python kamu < 3.10, pakai `if/elif/else` biasa.

---

## 🧪 Latihan Modul 5

### Latihan 1: Penentu Grade Nilai

```python
# Input nilai siswa (0-100)
# Output grade:
# 90-100: A (Sangat Baik)
# 80-89: B (Baik)
# 70-79: C (Cukup)
# 60-69: D (Kurang)
# <60: E (Sangat Kurang)
# Hint: validasi input harus antara 0-100
```

### Latihan 2: Cek Kelulusan

```python
# Input: 3 nilai (mtk, ipa, inggris)
# Syarat lulus:
# - Rata-rata >= 75
# - Tidak ada nilai di bawah 60
# Output: "Lulus" atau "Tidak lulus" + alasan
```

### Latihan 3: Tahun Kabisat

```python
# Input tahun
# Aturan tahun kabisat:
# - Habis dibagi 400 → kabisat
# - Habis dibagi 100 tapi tidak 400 → bukan kabisat
# - Habis dibagi 4 dan tidak 100 → kabisat
# - Sisanya → bukan kabisat
# Output: "[tahun] adalah tahun kabisat" / "bukan tahun kabisat"
```

### Latihan 4: Aplikasi Parkir Sederhana

```python
# Input: jam masuk, jam keluar (format 0-24)
# Tarif:
# 1 jam pertama: Rp 5.000
# Jam berikutnya: Rp 3.000 per jam
# Maksimum tarif: Rp 30.000
# Hitung total bayar
```

---

## ✅ Checklist Paham

- [ ] Saya bisa bedain `=` (assignment) vs `==` (perbandingan)
- [ ] Saya bisa bikin percabangan `if/elif/else`
- [ ] Saya paham urutan eksekusi kondisi
- [ ] Saya bisa pakai `and`, `or`, `not`
- [ ] Saya paham konsep truthy/falsy
- [ ] Saya bisa bikin ternary `A if kondisi else B`
- [ ] Saya tau `match/case` (kalau Python 3.10+)

**Kalau semua checklist tercentang → lanjut ke Modul 6.**
