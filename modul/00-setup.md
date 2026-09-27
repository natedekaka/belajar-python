# Modul 0: Setup Python — Pilih Jalur yang Sesuai

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjalankan Python di komputer atau browser
- Membedakan REPL mode vs file mode
- Menulis dan menjalankan script `.py`
- Mengerti kenapa kadang perlu install Python, dan kenapa kadang tidak

---

## 0. Pilih Jalurmu Dulu

Ada **3 cara** menjalankan Python. Tidak semua orang perlu install apa pun.
Pilih **satu** yang sesuai dengan perangkatmu, lalu lewati yang lain.

| Jalur | Untuk Siapa | Perlu Install? | Capai |
|-------|-----------|----------------|-------|
| **[A. Google Colab](#a-google-colab--paling-gampang)** | Semua orang, terutama yang belum pernah install | ❌ Tidak | 2 menit |
| **[B. Install di Komputer](#b-install-di-komputer)** | Yang mau belajar pakai laptop sendiri / komputer sekolah | ✅ Ya | 15–30 menit |
| **[C. VS Code](#c-vs-code--opsional)** | Yang sudah nyaman dengan editor | ✅ Ya | 10 menit |

> 💡 **Aturan paling penting modul ini:** kalau **[A] Colab** sudah jalan di perangkatmu,
> **langsung ke Modul 1**. Semua materi di repo ini bisa ditulis dan dijalankan di Colab.
> Install Python itu opsional, bukan wajib.

---

## A. Google Colab — Paling Gampang

Colab = **Google Colaboratory**. Python yang jalan di browser. Tidak install apa-apa.

### 1️⃣ Buka Colab

Buka di browser (Chrome/Edge/Firefox):

```
https://colab.research.google.com
```

Atau cari "Google Colab" di pencarian. Pilih **File → New → Notebook**.

### 2️⃣ Klik kotak kode, ketik, jalankan

Akan muncul kotak kosong dengan tanda `+`. Klik, lalu ketik:

```python
print("Halo, dunia!")
```

Jalankan dengan **Ctrl + Enter** (atau klik tombol ▶ di kiri kotak).

Muncul di bawahnya:
```
Halo, dunia!
```

Berhasil. Kamu sudah bisa ngoding.

### 3️⃣ Kenapa output muncul di bawah?

Di Colab, **kode** dan **hasilnya** tampil di tempat yang sama — dipisahkan kotak.
Kotak atas = kode yang kamu ketik. Kotak bawah = output dari program.

```
┌─────────────────────────────────┐
│ print("Halo, dunia!")           │  ← kode yang kamu tulis
└─────────────────────────────────┘
┌─────────────────────────────────┐
│ Hello, dunia!                   │  ← output dari program
└─────────────────────────────────┘
```

### 4️⃣ Menjalankan banyak baris sekaligus

Klik **Shift + Enter** kalau mau pindah ke baris berikutnya tanpa menjalankan.
Buat blok di bawah, lalu tekan **Ctrl + Enter**:

```python
nama = "Budi"
umur = 17
print(f"Halo {nama}, kamu {umur} tahun.")
```

> ⚠️ Urutan penting di Colab. Kalau kamu menulis `print(umur)` **sebelum**
> baris `umur = 17`, akan muncul error `NameError`.
> Jalankan dari atas ke bawah, seperti membaca halaman.

### 5️⃣ Cara reset kalau salah

Klik **Runtime → Restart session** di menu atas. Semua variabel kembali ke awal.
Ini setara dengan tombol "reset" — berguna kalau kamu bereksperimen dan semuanya jadi kacau.

> 💡 Tips: kerja di Colab berarti file-mu otomatis tersimpan di Google Drive,
> jadi tidak perlu khawatir kehilangan file. Tapi **untuk tugas yang mau dikumpulkan,
> tetap pakai file `.py`** — guru perlu melihat file-nya, bukan tautan Colab.

---

## B. Install di Komputer

Kalau kamu mau Python jalan **tanpa internet**, atau tugasmu butuh file `.py` di laptop sendiri.

> 📌 **Versi Python yang dibutuhkan: 3.10 atau lebih baru.**
> Materi di repo ini memakai `match/case` (Modul 5) dan anotasi `dict[str, ...]`
> (Modul 13) yang butuh 3.10+. Kalau versimu lebih tua, tulis di kertas dan
> tanyakan ke guru — **jangan** install sendiri, biar tidak bentrok di lab.

### Cek Dulu — Mungkin Sudah Terpasang!

#### Windows

Buka **Command Prompt** (tekan `Win`, ketik `cmd`, Enter):

```
python --version
```

Kalau muncul `Python 3.10.12` atau lebih tinggi — **sudah ada, lewati bagian ini**.

#### macOS / Linux

Buka **Terminal** (macOS: tekan `Cmd + Space`, ketik `Terminal`):

```
python3 --version
```

Kalau muncul `Python 3.10` atau lebih tinggi — **sudah ada, lewati bagian ini**.

> ⚠️ Kalau muncul `Python 2.x` — itu versi lama, **jangan dipakai**.
> Lanjut ke panduan install di bawah.

---

### B1. Install di Windows

**Langkah 1 — Unduh installer**

Buka: `https://www.python.org/downloads/`
Klik tombol besar **"Download Python 3.x.x"**.

**Langkah 2 — Jalankan installer**

> 🔴 **INI YANG SERING TERLEWAT.**
> Di halaman awal installer, **CENTANG checkbox "Add python.exe to PATH"** dulu
> **sebelum** klik Install. Kalau tidak, Python tidak bisa dipanggil dari CMD.

Akan muncul kotak **"Add python.exe to PATH"**. Kotak paling bawah biasanya sudah
tercentang otomatis — **jangan dilepas centangnya**.

Klik **Install Now**, tunggu sampai selesai.

**Langkah 3 — Uji**

Tutup lalu buka lagi **Command Prompt** (penting — jendela lama masih pakai PATH lama), lalu:

```
python --version
```

Harus muncul `Python 3.x.x`. Kalau muncul error, ulangi Langkah 2 dengan centang PATH.

---

### B2. Install di macOS

macOS **tidak** sudah membawa Python 3. Gagal paling umum: `python3` tidak ditemukan.

**Cara paling mudah — Homebrew:**

Buka **Terminal**, salin baris ini ke Google kalau tidak yakin:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Tunggu sampai selesai, lalu jalankan perintah yang ditampilkan di layar (biasanya menambah Homebrew ke PATH).

Lalu install Python:

```bash
brew install python
```

Uji:
```bash
python3 --version
```

---

### B3. Install di Linux

Python 3 hampir selalu sudah terpasang di Linux. Cek dulu:

```bash
python3 --version
```

Kalau belum ada, install sesuai distro:

**Ubuntu / Debian / Linux Mint:**
```bash
sudo apt update
sudo apt install python3 python3-venv
```

**Fedora:**
```bash
sudo dnf install python3
```

**Arch:**
```bash
sudo pacman -S python
```

---

### B4. Dua Perintah, Dua Arti

Linux/macOS sering punya dua perintah berbeda. Ini bukan error:

| Perintah | Yang Dipakai |
|----------|---------------------|
| `python` | Versi 2 (kadang) atau sudah di-set ke 3 |
| `python3` | **Selalu** Python 3 |

Di tutorial mana pun yang kamu googling, kalau perintahnya `python`, coba dulu `python3`.

---

## C. VS Code — Opsional

Editor yang enak buat nulis kode. **Tidak wajib** — Notepad juga bisa.

### 1. Install VS Code

Buka `https://code.visualstudio.com/` → download → install seperti aplikasi biasa.

### 2. Install Ekstensi Python

Buka VS Code → klik ikon **Extensions** di sidebar kiri (atau `Ctrl + Shift + X`)
→ cari **"Python"** (oleh Microsoft) → klik **Install**.

### 3. Cek Python

Buka terminal baru di VS Code (menu **Terminal → New Terminal**) dan ketik:

```
python --version
```

Harus muncul nomor versinya.

> 💡 Dua hal yang memudahkan:
> - Tekan **Ctrl + `** (backtick) untuk buka/m tutup terminal langsung dari editor
> - Tekan **F5** untuk jalankan program Python tanpa buka terminal manual

---

## 1. Dua Cara Jalanin Python

### 1. REPL Mode (Interactive)

REPL = **R**ead **E**val **P**rint **L**oop. Kamu kasih perintah, langsung dijawab.
Di Colab, ini setara dengan mengetik di kotak kode lalu Ctrl+Enter.

#### Di komputer (terminal/CMD)

```bash
python
```

Akan muncul:
```
Python 3.x.x (main, ...)
[GCC ...] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

`>>>` adalah **prompt** — Python siap menerima perintah.

Coba:
```python
>>> 2 + 3
5

>>> "Halo" * 3
'HaloHaloHalo'

>>> print("Selamat datang di Python!")
Selamat datang di Python!

>>> exit()   # ← Keluar dari REPL
```

> 💡 REPL cocok buat: coba-coba rumus, test kode kecil, ngajar demonstrasi.

### 2. File Mode (Script)

Tulis kode di file `.py`, baru jalankan. **Ini cara utama bikin program sungguhan.**

#### Di komputer

Buat file `halo.py`, isi satu baris:
```python
print("Halo dari file")
```

Lalu jalankan:
```bash
python halo.py
```

Output:
```
Halo dari file
```

#### Di Colab

Klik `+` untuk kotak baru, tulis kodenya, tekan **Ctrl + Enter**.
Supaya jadi file, klik **File → Save as** → beri nama `halo.py`.

> 💡 Perbedaan penting: di REPL, mengetik `nama = "Budi"` lalu keluar = hilang.
> Di file, kodenya tersimpan dan bisa dijalankan ulang kapan saja.
> Karena itu program yang mau dipakai serius **selalu** ditulis di file.

---

## 2. Virtual Environment (Venv)

Kadang perlu. Bagian ini menjelaskan kapan kamu membutuhkannya, dan kapan tidak.

**venv** = folder khusus tempat package Python-mu disimpan, terpisah dari sistem.
Tujuannya: biar install satu paket tidak merusak Python lain di komputer yang sama.

```bash
# 1. Bikin venv (cukup sekali, di folder projekmu)
python -m venv .venv

# 2. Aktifkan (setiap kali mau pakai folder ini)
# Windows (CMD):
.venv\Scripts\activate
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# 3. Cek — prompt terminal akan dapat tambahan (.venv)
python --version

# 4. Nonaktifkan
deactivate
```

> 💡 **Praktikkan:** Setiap membuka terminal baru di folder ini, aktifkan dulu.
> Kalau lihat `(.venv)` di awal prompt, berarti sudah aktif.
>
> ⚠️ Kalau belum aktif, `pip install` akan menginstall ke Python sistem.
> Itu bisa merusak program lain di komputermu — dan biasanya butuh hak admin untuk memperbaikinya.

### Kapan perlu venv?

| Situasi | Perlu venv? |
|-----------|-------------|
| Belajar di Colab | ❌ Tidak — Colab sudah punya virtual environment sendiri |
| Belajar dasar, belum pakai `pip` | ❌ Belum perlu |
| Install package (modul 10) | ✅ Ya |
| Proyek yang punya `requirements.txt` | ✅ Ya |

---

## 3. Shebang & Menjalankan Langsung

**Shebang** = baris pertama file yang memberi tahu komputer program mana yang dipakai.
Hanya perlu di Linux/macOS.

Baris pertama file `sapa.py`:
```python
#!/usr/bin/env python3

nama = input("Siapa nama kamu? ")
print(f"Halo {nama}! Selamat belajar Python!")
```

Lalu ubah jadi bisa dijalankan langsung:
```bash
chmod +x sapa.py
./sapa.py
```

> 💡 Di Windows, `./sapa.py` tidak diperlukan. Cukup `python sapa.py`.

---

## 4. PATH — Di Mana Python Mencari?

Kalau muncul error `command not found` atau `module not found`, kemungkinan
programnya ada tapi sistem tidak tahu di mana letaknya. Ini yang namanya **PATH**.

Cek:
```bash
which python    # Di mana python berada? (Linux/macOS)
where python    # Di mana python berada? (Windows)
echo $PATH      # Daftar folder yang dicari sistem
```

PATH itu daftar folder tempat sistem mencari program. Kalau programmu ada
di luar semua folder itu, sistem tidak akan menemukannya — makanya harus
memanggilnya dengan path lengkap.

> ⚠️ Error paling umum terkait PATH: di Windows, lupa mencentang
> "Add python.exe to PATH" saat install (Bagian B1). Gejalanya: `python` tidak
> dikenali, padahal Python sudah terpasang.

---

## 🧪 Latihan Modul 0

1. Buka [Google Colab](https://colab.research.google.com) atau terminal-mu, lalu hitung
   `((5 + 3) * 2 - 8) / 4` di REPL. Keluar `2.0`?
2. Buat file `coba.py` berisi `print("Belajar Python itu menyenangkan!")`, lalu jalankan.
3. **Sengaja** salah ketik di REPL — misalnya `print("Halo"` tanpa tutup kurung.
   Baca error yang muncul, lalu perbaiki. Ini latihan **membaca error** — penting!
4. Di Colab: ubah variabel `umur` jadi `18`, jalankan ulang, lalu klik
   **Runtime → Restart session** dan pastikan angka kembali ke semula.
5. (Kalau sudah install) Buat folder, aktifkan venv di dalamnya, cek `which python`,
   lalu `deactivate` dan cek lagi. Lihat bedanya.

---

## ✅ Checklist Paham

- [ ] Saya sudah pilih **satu** jalur setup yang sesuai untuk perangkat saya
- [ ] Saya bisa jalankan Python (minimal lewat Colab)
- [ ] Saya bisa bedain REPL vs file mode
- [ ] Saya bisa buat dan jalankan file `.py`
- [ ] Saya paham kenapa file tersimpan tapi REPL tidak
- [ ] Saya tahu kapan venv diperlukan (dan kapan tidak)
- [ ] Saya paham PATH secara konsep

**Kalau semua checklist tercentang → lanjut ke Modul 1.**

---

> 👨‍🏫 **Catatan untuk guru:** akses internet di sekolah sering terbatas,
> dan tidak semua komputer lab bisa di-install Python. Sebelum JP pertama, cek dulu
> kondisi lab — atau siap-siap pakai **[A] Colab** sebagai jalur cadangan.
