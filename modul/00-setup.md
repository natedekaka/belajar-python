# Modul 0: Setup Lingkungan Python di Omarchy Linux

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjalankan Python di terminal
- Membedakan REPL mode vs file mode
- Menulis dan menjalankan script `.py`
- Mengerti PATH dan virtual environment

---

## 1. Cek Python

Omarchy Linux (Arch) udah include Python secara default.

```bash
python --version
```

Kalau muncul `Python 3.x.x` — berarti siap.

> 💡 Di Arch Linux, `python` mengarah ke Python 3 (bukan 2). Aman.

## 2. Dua Cara Jalanin Python

### A. REPL Mode (Interactive)

REPL = **R**ead **E**val **P**rint **L**oop. Kita kasih perintah langsung, langsung dijawab.

```bash
python
```

Ketik itu di terminal. Maka akan muncul:

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

>>> exit()   # 👈 Keluar dari REPL
```

> 💡 REPL cocok buat: coba-coba rumus, test kode kecil, ngajar demonstrasi.

### B. File Mode (Script)

Tulis kode di file `.py`, lalu jalankan.

```bash
echo 'print("Halo dari file")' > halo.py
python halo.py
```

Output:
```
Halo dari file
```

Ini cara **utama** bikin program sungguhan.

## 3. Editor buat Nulis Kode

Di Omarchy Linux, kamu punya beberapa pilihan:

| Editor | Cara Buka | Cocok Buat |
|--------|-----------|------------|
| **VS Code** | `code .` | Full fitur, recommand buat belajar |
| **Neovim** | `nvim file.py` | Ringan, cepat |
| **Alacritty + Nano** | `nano file.py` | Darurat, edit cepat |

> 💡 Saran: pake **VS Code** biar ada syntax highlighting, auto-complete, dan terminal built-in.

Install VS Code kalau belum:
```bash
omarchy install dev  # atau
yay -S visual-studio-code-bin
```

## 4. Menjalankan Script Python

```bash
# Cara 1: Langsung
python namafile.py

# Cara 2: Bikin executable (advanced)
chmod +x namafile.py
./namafile.py
```

Untuk cara 2, tambahkan baris ini di baris **paling atas** file:
```python
#!/usr/bin/env python3
```

## 5. Virtual Environment (Venv)

Ini penting — biar project Python kita **tidak campur aduk** sama system Python.

```bash
# Bikin venv (cukup sekali)
python -m venv ~/belajar-python/.venv

# Aktifkan (lakukan setiap kali mau belajar)
source ~/belajar-python/.venv/bin/activate

# Cek: prompt terminal berubah jadi (.venv)
# Sekarang pip install akan aman di dalam venv

# Nonaktifkanls
deactivate
```

> 💡 Praktekkan: Setiap buka terminal baru → `source ~/belajar-python/.venv/bin/activate`
> 
> ⚠️ Kalau belum diaktifkan, `pip install` akan menginstall ke system Python. Hindari kalau gak perlu.

## 6. Shebang & Executable (Advanced — Tapi Berguna)

Di Omarchy, kita sering bikin script CLI. Ini cara praktisnya:

Buat file `greet.py`

```python
#!/usr/bin/env python3

nama = input("Siapa nama kamu? ")
print(f"Halo {nama}! Selamat belajar Python!")
```

Lalu:

```bash
chmod +x greet.py
./greet.py
```

Dengan shebang (`#!/usr/bin/env python3`), file bisa dijalankan langsung tanpa `python` di depan.

## 7. PATH — Dimana Python Mencari?

Kadang kita liat error `command not found` atau `module not found`. Ini karena **PATH**.

Cek:

```bash
which python   # Dimana python berada?
echo $PATH     # Daftar folder yang dicari sistem
```

PATH itu daftar folder (dipisah `:`) tempat sistem mencari program. Kalau file kita gak ada di salah satu folder itu, kita harus panggil pake path lengkap.

---

## 🧪 Latihan Modul 0

1. Buka terminal, ketik `python`, lalu hitung `((5 + 3) * 2 - 8) / 4`. Keluar?
2. Buat file `coba.py` berisi `print("Belajar Python itu menyenangkan!")`, jalankan.
3. Coba salah ketik di REPL — misal `print("Halo"` tanpa tutup kurung. Baca errornya.
4. Buat venv di folder `~/belajar-python/`, aktifkan, lalu `which python` — liat bedanya PATH.
5. Buat file `sapa.py` dengan shebang, `chmod +x`, dan jalankan dengan `./sapa.py`.

## ✅ Checklist Paham

- [x] Saya bisa bedain REPL vs file mode
- [x] Saya bisa buat dan jalanin file `.py`
- [x] Saya tau cara aktivasi virtual environment
- [x] Saya tau fungsi shebang `#!/usr/bin/env python3`
- [x] Saya paham PATH secara konsep

**Kalau semua checklist tercentang → lanjut ke Modul 1.**
