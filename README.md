# 🐍 Belajar Python — Untuk Guru Informatika

**Live Site:** [https://natedekaka.github.io/belajar-python/](https://natedekaka.github.io/belajar-python/)

**Penulis:** Sisyphus  
**Target:** Guru Informatika — Omarchy Linux  
**Tujuan:** Paham Python dari nol sampai bisa ngajar dan bikin tools sendiri

---

## Cara Belajar

1. **Pelajari modul urut** — setiap modul dibangun di atas modul sebelumnya
2. **Tulis kode, jangan copy-paste** — ketik manual setiap contoh
3. **Kerjakan latihan** — baru lanjut kalau latihan selesai
4. **Baca error** — error itu guru terbaik
5. **Coba-coba di REPL** — ketik `python` di terminal, eksperimen bebas

## Struktur Modul

| # | Modul | Deskripsi |
|---|-------|-----------|
| 0 | **Setup** | 3 jalur: Google Colab (paling gampang), install di komputer, VS Code |
| 1 | **Variabel & Tipe Data** | int, float, str, bool — fondasi paling dasar |
| 2 | **String** | Manipulasi teks — slicing, formatting, method |
| 3 | **List & Tuple** | Kumpulan data — index, loop, method |
| 4 | **Dictionary & Set** | Pasangan key-value, data unik |
| 5 | **Percabangan** | if/elif/else, logika AND/OR/NOT |
| 6 | **Perulangan** | for loop, while loop, range() |
| 7 | **Function** | def, parameter, return, scope |
| 8 | **Error & Exception** | try/except — jangan takut error |
| 9 | **File I/O** | Baca & tulis file, CSV |
| 10 | **Module & pip** | import, bikin module sendiri, install package |
| 11 | **List Comprehension** | Cara Pythonic bikin list |
| 12 | **OOP Dasar** | Class, object, inheritance |
| 13 | **Proyek Akhir** | Aplikasi CLI Nilai Siswa + Quiz Interaktif |
| 14 | **Struktur Data Lanjutan** | collections, dataclasses, typing, heapq, itertools |
| 15 | **Kompleksitas Algoritma** | Big-O, sorting, hashing, analisis strategi & justifikasi efisiensi |
| 16 | **Basis Data (SQLite)** | SQL, ER diagram, normalisasi, transaksi, indexing |
| 17 | **Testing & Dokumentasi** | pytest, coverage, mypy, ruff, docstring, CI/CD |
| 18 | **Jaringan & Model OSI** | 7 layer OSI, topologi, TCP/UDP, socket programming |
| 19 | **Keamanan Digital** | CIA Triad, STRIDE, OWASP Top 10, bcrypt, JWT, TLS, Zero Trust |
| 20 | **Dampak Sosial TIK** | Studi kasus, argumentasi kritis (CER), debat, AI ethics |

---

> 📌 **Catatan Kurikulum:** Modul 0–13 = fondasi Python (Fase E bridging). Modul 14–20 = **pelengkap Fase F** (Kelas XI–XII Kurikulum Merdeka). Total 21 modul → 72 JP (2 JP × 36 minggu).

## Legend

```python
# 👈 Ini komentar — penjelasan
>>>  # 👈 Ini output di REPL / terminal
💡  # 👈 Tips penting
⚠️  # 👈 Peringatan / jebakan umum
🧪  # 👈 Latihan
🏆  # 👈 Target pemahaman (buat ngajar)
```

## Sebelum Mulai

Cara paling cepat dan paling gampang: **[Google Colab](https://colab.research.google.com)**.
Buka di browser, klik `+`, ketik `print("Halo dunia!")`, tekan **Ctrl + Enter**. Selesai — tanpa install apa pun.

Kalau mau pakai Python di komputermu sendiri, cek dulu versinya:

```bash
python --version     # Windows
python3 --version    # macOS / Linux
```

Yang dibutuhkan: **Python 3.10 atau lebih baru**.

Kalau sudah siap — lanjut ke **Modul 0: Setup**.

---

## 📄 Berkas Pendukung Guru

| Berkas | Untuk siapa | Isi |
|--------|------------|------|
| `PETA-KURIKULUM.md` | Guru | Peta CP Fase F, modul→elemen, 72 JP, profil Pelajar Pancasila |
| `RPS.md` | Guru | Rencana Pelaksanaan Pembelajaran 72 JP + ATP + KKTP + asesmen |
| `lembar-kerja-siswa.md` | **Siswa** | Lembar kerja siap cetak A4 per modul + rubrik mini |
| `template-proyek.md` | Siswa | Template proyek akhir semi-kosong + rubrik penilaian PLB |
| `rubrik-proyek.md` | Guru | Rubrik detail penilaian proyek (PLB, teknis, presentasi, portofolio) |
| `tips-mengajar.md` | Guru | Strategi, analogi, jebakan murid, aktivitas kelas, estimasi JP |
| `bank-soal.md` | Guru | 77 soal + kunci jawaban + kunci cepat |
| `bank-soal-siswa.md` | **Siswa** | 77 soal tanpa kunci — aman untuk dibagikan |
| `cheat-sheet.md` | Siswa | Ringkasan syntax 1 halaman, siap cetak |
| `error-dictionary.md` | Siswa | Cara baca 15+ error Python yang sering muncul |
| `mini-projek.md` | Guru | 6 proyek latihan dengan panduan |
| `scripts/` | Guru | Absensi, rekap nilai, jadwal, backup, rename tugas |

> ⚠️ **Perhatikan:** `bank-soal.md` berisi kunci jawaban. Jangan dibagikan apa adanya —
> pakai `bank-soal-siswa.md` untuk siswa.
