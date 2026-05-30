# 👨‍🏫 Panduan Mengajar — Tips Per Modul

Strategi, analogi, jebakan murid, dan aktivitas kelas untuk setiap modul.

---

## Modul 0: Setup

**Analogi:** "Python itu seperti koki. REPL seperti dia masak langsung di depan kita. File .py seperti resep yang bisa dijalanin kapan saja."

**Jebakan Murid:**
- Bingung beda terminal vs Python REPL — tandai prompt `$` vs `>>>`
- Lupa aktivasi venv — biasakan `source .../venv/bin/activate`

**Aktivitas Kelas (10 menit):**
1. Minta semua buka terminal
2. Ketik `python` → muncul `>>>`
3. Ketik `print("Nama saya ...")` — tiap murid tulis nama sendiri
4. `exit()` untuk keluar

**Estimasi:** 1 JP (45 menit) — lebih banyak praktek

---

## Modul 1: Variabel & Tipe Data

**Analogi:** "Variabel itu seperti loker sekolah. Setiap loker punya label (nama variabel) dan isi (nilai). Ada loker untuk buku (string), ada untuk uang (integer)."

**Jebakan Murid:**
- ❌ Paling umum: `5 = x` (terbalik) — ingatkan: "Yang diubah itu yang kiri, `x = 5`"
- ❌ `type(x)` dikira fungsi cetak — tunjukkan beda `print()` vs `type()`
- ❌ Bingung `int` vs `float` — "Kenapa 5/2 hasilnya 2.5 bukan 2?"

**Aktivitas Kelas (15 menit):**
1. Suruh tebak output sebelum di-run
2. Game: "Tebak Tipe" — tunjukkan nilai, suruh tebak `int/float/str/bool`

```python
# Tebak output sebelum jalanin
print(type("5"))
print(type(5))
print(type(5.0))
print(10 / 3)
print(10 // 3)
```

**Estimasi:** 2 JP — teori 1 JP, praktek 1 JP

---

## Modul 2: String

**Analogi:** "String itu seperti pita pengukur. Ada nomor di setiap sentimeternya. Index 0 itu sentimeter pertama. Slicing [2:5] itu ambil dari cm ke-2 sampai ke-4."

**Jebakan Murid:**
- ❌ Index mulai 0 — "Kenapa `"Budi"[0]` itu 'B' bukan index 1?"
- ❌ `s[0:5]` tidak termasuk index 5 — "Kenapa 'Python'[0:5] cuma 'Pytho'?"
- ❌ Lupa string **immutable** — coba `s[0] = "J"` dapat error

**Aktivitas Kelas (15 menit):**
1. Tebak index: tulis "INFORMATIKA" di papan, tunjuk murid, tanya index huruf tertentu
2. Lomba: siapa paling cepat balik nama pake `[::-1]`
3. FizzBuzz pake string: cetak "Fizz" untuk angka genap, "Buzz" untuk ganjil

```python
# Game tebak output
kata = "PYTHON"
print(kata[0])    # ?
print(kata[-1])   # ?
print(kata[1:4])  # ?
print(kata[::-1]) # ?
```

**Estimasi:** 2 JP

---

## Modul 3: List & Tuple

**Analogi:** "List itu seperti tas ransel — bisa dimasukin barang, bisa dikeluarin, bisa diubah isinya. Tuple itu seperti bingkisan yang sudah dibungkus — isinya tetap, tidak bisa diganti."

**Jebakan Murid:**
- ❌ Index 0 lagi — "Kenapa `[1,2,3][0]` itu 1?"
- ❌ `append()` lupa kurung — tulis `list.append` tanpa `()` — itu ngirim method, bukan manggil
- ❌ Nested list bingung aksesnya — `matriks[0][1]`

**Aktivitas Kelas:**
1. Praktik: bikin list teman sekelas, loop cetak semua
2. Game: tebak output `[1,2,3,4,5][::-1]` (balik list)
3. "List Operation Race" — siapa paling cepat: tambah, hapus, urutkan

**Estimasi:** 2 JP

---

## Modul 4: Dictionary & Set

**Analogi:** "Dictionary itu seperti kamus — cari kata (key) dapat artinya (value). Atau seperti lemari arsip — setiap laci (key) berisi map (value)."

**Jebakan Murid:**
- ❌ Akses key yang tidak ada — `dict["x"]` error, harus pakai `.get()`
- ❌ Bingung `{}` untuk dict vs set — `{"a": 1}` adalah dict, `{"a"}` adalah set
- ❗ Kritis: nested dict akses `data["siswa1"]["nilai"]["mtk"]`

**Aktivitas Kelas:**
1. Bikin dictionary data diri sendiri
2. Bikin buku telepon teman sekelas (nama: no hp)
3. Loop dengan `.items()` — "Ini cara Pythonic, hafalkan!"

**Estimasi:** 2 JP

---

## Modul 5: Percabangan

**Analogi:** "Percabangan itu seperti pohon keputusan. Kalau hujan, bawa payung. Kalau tidak, tidak usah. Sederhana."

**Jebakan Murid:**
- ❌ **Paling kritis:** `=` vs `==` — berulang kali salah. Ingatkan: "Tanda sama dengan SATU untuk assignment, DUA untuk perbandingan"
- ❌ Urutan kondisi salah — kasih contoh nilai 85 dapet C karena urutan terbalik
- ❌ Lupa `:` setelah `if`, `elif`, `else`

**Aktivitas Kelas:**
1. Gambar flowchart di papan untuk kasus "Cek Kelulusan"
2. Minta murid bikin flowchart dulu sebelum nulis kode
3. Praktek: program penentu grade nilai

**Estimasi:** 2 JP — 1 JP teori + flowchart, 1 JP coding

---

## Modul 6: Perulangan

**Analogi:** "For loop itu seperti guru manggil murid satu per satu dari daftar hadir. While loop itu seperti 'ulang terus sampai ada yang bilang stop'."

**Jebakan Murid:**
- ❌ **Paling kritis:** Infinite loop — lupa mengupdate variabel di `while`
- ❌ `range(5)` cuma sampai 4, bukan 5
- ❌ `break` vs `continue` tertukar

**Safety:** Ajarkan `Ctrl+C` untuk memberhentikan infinite loop — ini HARUS di hari pertama loop.

**Aktivitas Kelas:**
1. Tabel perkalian pake nested loop — cetak rapi
2. Game tebak angka (while + break)
3. FizzBuzz — klasik, wajib

**Peringatan Keras:** "Bikin infinite loop itu bagian dari belajar. Kalau kejadian, tekan Ctrl+C. Jangan panik, jangan tutup terminal."

**Estimasi:** 2 JP

---

## Modul 7: Function

**Analogi:** "Function itu seperti mesin fotokopi. Kamu masukin kertas (input/parameter), pencet tombol, keluar hasil (return value). Atau seperti resep masak — tulis sekali, bisa dipraktekkin berkali-kali."

**Jebakan Murid:**
- ❌ Lupa `return` — fungsi return `None` tanpa sadar
- ❌ Lupa kurung pas manggil — `func` vs `func()` — beda! `func` itu objek fungsi, `func()` itu hasilnya
- ❌ Scope: bikin variabel di dalam fungsi, coba panggil di luar
- ❌ Parameter vs Argumen — dua istilah ini sering tertukar

**Aktivitas Kelas:**
1. Bikin fungsi `luas_persegi`, `luas_lingkaran` — langsung dipraktekkin
2. Bikin fungsi yang return beberapa nilai → unpack hasilnya
3. Analisis: "Kode mana yang lebih baik — dengan fungsi atau tanpa?"

**Estimasi:** 2 JP

---

## Modul 8: Error & Exception

**⚠️ Ini modul PALING PENTING untuk guru.** Murid harus diajar baca error SEJAK AWAL.

**Analogi:** "Error itu seperti lampu indikator di mobil. Kalau nyala, jangan panik — baca dulu tulisannya. Dia kasih tahu apa yang rusak."

**Jebakan Murid:**
- ❌ Panik liat error merah — biasakan: "Error itu informasi, bukan hukuman"
- ❌ Langsung tanya guru tanpa baca pesan error
- ❌ Salah tangkap error jenis salah — `except ValueError:` tapi errornya `TypeError:`

**Aktivitas Kelas (WAJIB):**
1. Sesi "Error Challenge": kasih kode yang error, minta murid baca pesan errornyadan perbaiki
2. Tebak jenis error: kasih kode, tanya "error apa yang akan muncul?"
3. Latihan try/except: kalkulator yang tahan banting

**Kata Kunci:** "Programmer hebat bukan yang tidak pernah error, tapi yang bisa baca dan perbaiki error."

**Estimasi:** 2 JP — ini investasi. Murid yang bisa baca error akan jauh lebih mandiri.

---

## Modul 9: File I/O

**Analogi:** "File itu seperti buku catatan. Mode 'r' itu baca, 'w' itu nulis baru (buku baru), 'a' itu nulis di halaman terakhir."

**Jebakan Murid:**
- ❌ Lupa `with` statement — buka file, lupa tutup
- ❌ Mode `"w"` menimpa file — kaget data hilang
- ❌ Path salah — "FileNotFoundError, padahal filenya ada"
- ❌ `readlines()` masih ada `\n` — harus di-`.strip()`

**Aktivitas Kelas:**
1. Bikin file catatan harian — simpan, baca, tambah
2. Baca file CSV nilai — ini yang paling real-world
3. Bikin program yang menyimpan data (bookmark) ke JSON

**Estimasi:** 3 JP — 2 JP teori, 1 JP projek CSV nilai

---

## Modul 10: Module & pip

**Analogi:** "Module itu seperti meminjam buku dari perpustakaan. `import math` = ambil buku matematika dari rak. `pip install requests` = beli buku baru ke toko buku."

**Jebakan Murid:**
- ❌ Lupa install dulu — `import requests` dapat `ModuleNotFoundError`
- ❌ Install di global, bukan di venv
- ❌ Bikin file `math.py` sendiri lalu bingung kenapa `import math` error
- ❌ `if __name__` sering dilupakan — kode test jalan pas di-import

**Aktivitas Kelas:**
1. Bikin module `alat_sekolah.py` berisi fungsi-fungsi, lalu import di `main.py`
2. Coba install `requests`, ambil data dari API publik (contoh: jadwal libur)
3. Praktek: `pip freeze > requirements.txt`

**Estimasi:** 2 JP

---

## Modul 11: List Comprehension

**Analogi:** "List comprehension itu seperti pabrik — masukin bahan mentah (list awal), proses dengan mesin (ekspresi), keluar produk jadi (list baru). Semua dalam satu baris."

**Jebakan Murid:**
- ❌ LC dipaksakan untuk logika kompleks — bikin kode susah dibaca
- ❌ Kurung siku kelebihan/kekurangan — typo bracket
- ❌ Lambda bikin bingung — "kok pake `lambda`?" padahal bisa pakai fungsi biasa

**Aktivitas Kelas:**
1. Sebelum-LC vs Sesudah-LC — tunjukkan perbandingan
2. Lomba: siapa paling cepat nulis LC untuk kasus tertentu
3. "LC atau loop?" — tebak mana yang lebih tepat

**Estimasi:** 1-2 JP

---

## Modul 12: OOP

**⚠️ Ini modul paling abstrak untuk pemula.** Jangan buru-buru.

**Analogi (WAJIB):**
- Class = cetakan kue
- Object = kue-nya
- `__init__` = proses memanggang
- `self` = "saya" (setiap object bicara tentang dirinya)
- Inheritance = "anak mewarisi sifat orang tua"

**Jebakan Murid (BANYAK):**
- ❌ `self` — paling membingungkan. "Apa itu self? Kenapa harus ada?"
- ❌ Lupa `self` di parameter method — `TypeError: takes 0 positional arguments but 1 was given`
- ❌ Lupa `()` pas buat object — `s = Siswa` vs `s = Siswa()`
- ❌ `__init__` dieja salah — `__init` atau `_init_` atau `__init__` (dua underscore tiap sisi)
- ❌ `super().__init__()` — lupa panggil constructor parent

**Aktivitas Kelas:**
1. Praktek: bikin class `Siswa`, `Buku`, `Hewan` — dari yang paling sederhana
2. Inheritance: `class Kucing(Hewan):` — override `bersuara()`
3. **JANGAN** langsung masuk polymorphism, abstraction — simpan untuk pertemuan lanjutan

**Kapan Mulai OOP:**
- Hanya setelah murid **benar-benar** nyaman dengan function, list, dict, loop
- Kalau masih struggling di function, jangan mulai OOP

**Estimasi:** 3 JP bertahap — 1 JP class sederhana, 1 JP method & `self`, 1 JP inheritance

---

## Modul 13: Proyek Akhir

Ini yang **membuktikan** murid sudah bisa bikin aplikasi nyata.

**Tips:**
1. Bagi proyek jadi 3 pertemuan:
   - Pertemuan 1: class Siswa, input data
   - Pertemuan 2: perhitungan, laporan
   - Pertemuan 3: file I/O (simpan/baca), penyempurnaan
2. Murid **tidak perlu** nulis kode full 300 baris sekaligus
3. Setiap pertemuan target: "hari ini output program harus jalan dan melakukan X"
4. Pair programming: 2 murid 1 komputer — salah satu ngetik, satu mikir

**Penilaian:**
- Apakah program jalan tanpa error? (40%)
- Apakah fitur inti berfungsi? (40%)
- Apakah kode rapi? (20%)

---

## 📅 Estimasi Total Jam Mengajar

| Modul | JP (45 menit) | Catatan |
|-------|---------------|---------|
| 0. Setup | 1 | Lebih banyak praktek |
| 1. Variabel | 2 | |
| 2. String | 2 | |
| 3. List & Tuple | 2 | |
| 4. Dictionary & Set | 2 | |
| 5. Percabangan | 2 | Flowchart penting |
| 6. Perulangan | 2 | Waspada infinite loop |
| 7. Function | 2 | |
| 8. Error Handling | 2 | ⭐ Prioritas tinggi |
| 9. File I/O | 3 | CSV untuk guru |
| 10. Module & pip | 2 | |
| 11. List Comp | 1-2 | |
| 12. OOP | 3 | Bertahap, jangan buru |
| 13. Proyek Akhir | 3 | 3 pertemuan |

**Total: 27-29 JP** (± 1 semester genap atau 1 tahun ajar jika 1 JP/minggu)

---

## ⚡ Ringkasan 10 Aturan Emas Ngajar Python

1. **Baca error dulu sebelum bertanya** — "Error apa yang muncul?"
2. **Ketik manual, jangan copy-paste** — otak merekam lebih baik
3. **REPL adalah sahabat** — coba-coba dulu di REPL sebelum bikin file
4. **Print debugging** — kalau bingung, `print()` isi variabel
5. **Start small** — jalanin dulu versi minimal, baru kembangkan
6. **Commit sering** — kalau rusak, tinggal balik ke versi sebelumnya
7. **Google with confidence** — programmer hebat googling tiap hari
8. **Kode baca kode** — baca kode punya teman, pelajari pola baru
9. **Ngajar = paham 2x lipat** — coba jelaskan ke teman sebangku
10. **Yang penting jalan, bukan sempurna** — perbaiki nanti
