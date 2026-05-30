# ❌ Error Dictionary Python — Bahasa Indonesia

## Cara Baca Error

```
  Jenis Error         Pesan Error
  ────────            ──────────────────
Traceback (most recent call last):
  File "main.py", line 5, in <module>        ← File & baris
    print(10 / 0)                             ← Kode yang salah
ZeroDivisionError: division by zero           ← Jenis: penyebab
```

---

## 🔴 SyntaxError — Salah Tulis

Kode tidak mengikuti aturan bahasa Python.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `invalid syntax` | Ada kesalahan penulisan | Cek baris yang disebut — biasanya lupa `:` di `if`, `for`, `def`, atau kurung tidak sepasang |
| `EOL while scanning string literal` | String tidak ditutup | Cek kutip string — lupa `"` atau `'` |
| `unexpected indent` | Indentasi tidak terduga | Pastikan semua blok kode indentasinya rata (sama) |
| `expected an indented block` | Harus ada indentasi setelah `:` | Tekan tab/spasi setelah baris yang diakhiri `:` |

```
❌ if x > 5            ✅ if x > 5:
print(x)                    print(x)

❌ print("Halo         ✅ print("Halo")
```

---

## 🔴 NameError — Nama Tidak Dikenal

Variabel atau fungsi belum didefinisikan.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `name 'x' is not defined` | Variabel `x` belum dibuat | Cek: apakah sudah `x = ...` sebelumnya? Periksa ejaan! |

```
❌ print(umur)  # umur belum diisi
✅ umur = 17
   print(umur)

❌ print(nilai_siswa)  # salah eja
✅ print(nilai_siswa)  # atau perbaiki nama variabelnya
```

> 💡 **Penyebab umum:** typo nama variabel, lupa assign, variabel cuma ada di dalam if yang tidak jalan.

---

## 🔴 TypeError — Tipe Data Tidak Cocok

Operasi antara dua tipe data yang berbeda.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `can only concatenate str (not "int") to str` | String digabung dengan angka | `str(angka)` dulu |
| `unsupported operand type(s) for +: 'int' and 'str'` | Angka dijumlah dengan string | `int(angka_str)` atau `str(angka)` |
| `'int' object is not iterable` | Angka di-loop padahal harus list | Loop harus untuk list/tuple/string, bukan angka |
| `list indices must be integers or slices, not str` | Index list pakai string | List pake angka, dictionary pake string |

```
❌ "Umur: " + 17
✅ "Umur: " + str(17)
✅ f"Umur: {17}"

❌ for i in 5:
✅ for i in range(5):
```

---

## 🔴 ValueError — Nilai Tidak Sesuai

Nilai yang diberikan tidak bisa diproses.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `invalid literal for int() with base 10: 'abc'` | `int("abc")` — 'abc' bukan angka | Pastikan input benar-benar angka sebelum di-`int()` |
| `could not convert string to float: 'lima'` | `float("lima")` — "lima" bukan float | Pakai angka, bukan terbilang |
| `math domain error` | Operasi matematika tidak valid | Cek: `sqrt(-1)`, `log(0)` — nilainya harus valid |

```
❌ int(input("Masukkan angka: "))  # user ketik "lima"
✅ # Pakai try/except:
   try:
       angka = int(input("Masukkan angka: "))
   except ValueError:
       print("Itu bukan angka!")
```

---

## 🔴 IndexError — Index di Luar Jangkauan

Mengakses index yang tidak ada di list/string.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `list index out of range` | Index melebihi panjang list | Cek `len(listku)` — index maksimal `len-1` |

```
❌ siswa = ["Budi", "Ani"]
   print(siswa[5])     # cuma ada index 0 dan 1!

✅ if len(siswa) > 5:
       print(siswa[5])
```

> 💡 **Ingat:** Index mulai dari **0**. List dengan 3 item: index 0, 1, 2 — bukan 1, 2, 3.

---

## 🔴 KeyError — Key Tidak Ada di Dictionary

Mengakses key yang tidak ada di dictionary.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `KeyError: 'alamat'` | Key 'alamat' tidak ada | Cek: apakah key-nya sudah dimasukkan? |

```
❌ siswa = {"nama": "Budi"}
   print(siswa["alamat"])

✅ print(siswa.get("alamat", "Tidak ada"))
✅ # Atau cek dulu:
   if "alamat" in siswa:
       print(siswa["alamat"])
```

---

## 🔴 ZeroDivisionError — Pembagian Nol

Angka dibagi dengan nol.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `division by zero` | 10 / 0 atau 10 % 0 | Cek pembagi sebelum operasi |

```
❌ hasil = 10 / angka  # kalau angka = 0, error!
✅ if angka != 0:
       hasil = 10 / angka
   else:
       print("Tidak bisa membagi nol!")
```

---

## 🔴 FileNotFoundError — File Tidak Ada

Membuka file yang tidak ditemukan.

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `No such file or directory: 'data.txt'` | File tidak ada | Cek: apakah nama filenya benar? Apakah foldernya benar? |

```
❌ with open("nilai.txt") as f:  # file tidak ada
✅ import os
   if os.path.exists("nilai.txt"):
       with open("nilai.txt") as f:
           ...
```

---

## 🔴 IndentationError — Indentasi Salah

Python sangat strict soal indentasi (spasi di awal baris).

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `unexpected indent` | Ada spasi yang tidak seharusnya | Periksa baris yang dimaksud — hapus spasi berlebih |
| `unindent does not match any outer indentation level` | Jumlah spasi tidak konsisten | Pastikan semua baris dalam satu blok pakai jumlah spasi yang SAMA |

```
❌ if True:
   print("Halo")      # 3 spasi
     print("Dunia")   # 4 spasi — beda!

✅ if True:
       print("Halo")
       print("Dunia")
```

> 💡 **Aturan emas:** 1 blok = 4 spasi. Jangan campur tab dan spasi.

---

## 🔴 AttributeError — Object Tidak Punya Atribut/Method

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `'int' object has no attribute 'append'` | Angka tidak punya `.append()` | `.append()` hanya untuk list |
| `'list' object has no attribute 'items'` | List tidak punya `.items()` | `.items()` hanya untuk dict |
| `'str' object has no attribute 'append'` | String tidak punya `.append()` | String itu immutable |

```
❌ angka = 5
   angka.append(10)   # int tidak punya append!

✅ listku = [5]
   listku.append(10)
```

---

## 🔴 ImportError / ModuleNotFoundError — Module Tidak Ada

| Error | Arti | Perbaikan |
|-------|------|-----------|
| `No module named 'requests'` | Module belum diinstall | `pip install requests` |
| `cannot import name 'something'` | Nama yang diimport tidak ada | Cek apakah nama fungsi/class-nya benar |

---

## 📋 Tabel Cepat Semua Error

| Error | Arti Singkat | Paling Sering Karena |
|-------|-------------|---------------------|
| `SyntaxError` | Salah tulis | Lupa `:` atau kurung |
| `NameError` | Variabel belum ada | Typo atau lupa assign |
| `TypeError` | Tipe data beda | String + angka |
| `ValueError` | Nilai tidak valid | `int("abc")` |
| `IndexError` | Index kebesaran | List index di luar range |
| `KeyError` | Key tidak ada | Dict key salah |
| `ZeroDivisionError` | Pembagi = 0 | 10 / 0 |
| `FileNotFoundError` | File tidak ditemukan | Nama file salah |
| `IndentationError` | Spasi tidak rapi | Campur tab & spasi |
| `AttributeError` | Method tidak cocok | `.append()` di string |

---

## 🧠 Tips Debugging

```
1. BACA pesan error dari atas ke bawah
2. Cari: "File ... , line ..." — itu lokasi masalah
3. Cek baris yang disebut — apa yang salah di baris itu?
4. Kalau buntu, tambahkan print() sebelum baris error untuk cek nilai variabel
5. Google pesan error-nya (dalam Inggris) — pasti ada yang pernah ngalamin

"Error bukan kegagalan — itu petunjuk."
```
