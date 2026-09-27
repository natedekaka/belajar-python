# 📚 Peta Kurikulum Informatika SMA Kelas XI — Fase F

**Sumber resmi:**  
KEPUTUSAN KEPALA BADAN STANDAR, KURIKULUM, DAN ASESMEN PENDIDIKAN  
KEMENTERIAN PENDIDIKAN, KEBUDAYAAN, RISET, DAN TEKNOLOGI  
NOMOR 033/H/KR/2022 — Capaian Pembelajaran Kurikulum Merdeka

> ⚠️ **Koreksi penting:**  
> - **Fase E = Kelas X**  
> - **Fase F = Kelas XI dan XII SMA/MA/SMK/MAK**  
> Paket ini untuk **kelas XI** → rujuk **Fase F** (bukan Fase E).

---

## 1. Capaian Pembelajaran (CP) Fase F — Per Elemen

| Elemen | Kode | Capaian Pembelajaran (ringkasan resmi) |
|--------|------|----------------------------------------|
| Berpikir Komputasional | BK | Menganalisis **beberapa strategi algoritmik** secara kritis → banyak alternatif solusi, justifikasi efisiensi/kelebihan/keterbatasan, **memilih & menerapkan solusi terbaik** dengan merancang struktur data yang lebih kompleks & abstrak. |
| Teknologi Informasi & Komunikasi | TIK | — *(tidak ada CP khusus di tabel per elemen; TIK jadi alat di elemen lain)* |
| Sistem Komputer | SK | Menghasilkan **prototipe perangkat lunak** yang berinteraksi dengan *single board computer*/controller/kit elektronika; mengomunikasikan produk & proses pengembangan. |
| Jaringan Komputer & Internet | JKI | Memahami **konsep lanjutan**: topologi, aspek teknis jaringan, **OSI Layer**, komponen jaringan, mekanisme pertukaran data, **cyber security**, tata kelola kontrol akses data, faktor & konfigurasi keamanan jaringan. |
| Analisis Data | AD | — *(tidak ada CP khusus di tabel per elemen; muatan AD masuk ke AP — library big data)* |
| Algoritma & Pemrograman | AP | Mengembangkan **program modular berukuran besar**; memahami, memelihara, menyempurnakan struktur program (statik & dinamis); **algoritma standar & strategi efisiensinya**; merancang & mengimplementasikan **struktur data abstrak kompleks** dengan *library* standar (termasuk *library* AI & pengolahan data bervolume besar); **menerjemahkan program antar bahasa** (kaidah translasi). |
| Dampak Sosial Informatika | DSI | Mengkaji, menganalisis, memberikan **argumentasi & rasional kritis** pada kasus-kasus sosial terkini terkait produk TIK & sistem komputasi. |
| Praktik Lintas Bidang | PLB | Bergotong royong dalam **tim inklusif** untuk projek pengembangan sistem komputasi: analisis & identifikasi persoalan → merancang → mengimplementasi → menguji → menyempurnakan → mengomunikasikan produk/proses/manfaat (lisan & tertulis). |

> **Catatan:** Tabel per elemen resmi menandai TIK = “—” dan AD = “—”. Naratif umum (paragraf D) menyebut “library untuk pengolahan data bervolume besar” → muatan AD diserap ke elemen AP.

---

## 2. Kesenjangan Jujur: Materi Repo Saat Ini vs CP Fase F

| Area CP Fase F | Status di Repo (Modul 0–13) | Tindakan |
|----------------|----------------------------|----------|
| Analisis strategi algoritmik alternatif + justifikasi efisiensi (BK) | **Tidak ada** — hanya dasar loop & function | Tambah Modul 15 |
| Struktur data abstrak kompleks + library standar (AP) | List/dict/set dasar saja; tidak ada `collections`, `dataclasses`, `typing`, `heapq`, `itertools` | Tambah Modul 14 |
| Program modular besar + pemeliharaan kode statik/dinamis (AP) | Hanya Modul 13 (proyek CLI sederhana) | Perluas Modul 13 + Modul 17 |
| OSI Layer, topologi, mekanisme pertukaran data, cyber security (JKI) | **Tidak ada** | Tambah Modul 18–19 |
| Argumentasi kritis dampak sosial TIK (DSI) | **Tidak ada** | Tambah Modul 20 |
| Prototipe SBC/kit elektronika (SK) | **Tidak ada** | Opsional — tambah lab Arduino/RPi di proyek |
| Proyek PLB tim inklusif end-to-end (PLB) | Modul 13 individual | Restruktur proyek jadi **kelompok + dokumentasi lengkap** |

**Kesimpulan:** Modul 0–13 = **fondasi Fase E / bridging**. Untuk memenuhi Fase F, **wajib menambah 7 modul pelengkap** (14–20) dan mengupgrade proyek akhir.

---

## 3. Peta Modul → Elemen CP → Alokasi 72 JP (2 JP × 36 minggu)

| Unit | Modul | Judul | Elemen CP Utama | JP |
|------|-------|-------|-----------------|----|
| 1 | 0 | Setup: Colab / Install / VS Code | — (prasyarat) | 2 |
| 1 | 1 | Variabel & Tipe Data | AP (dasar) | 3 |
| 1 | 2 | String | AP (dasar) | 3 |
| **Subtotal Unit 1** | | | | **8** |
| 2 | 3 | List & Tuple | AP, BK (struktur data dasar) | 4 |
| 2 | 4 | Dictionary & Set | AP, BK | 3 |
| 2 | 11 | List Comprehension | AP (ekspresi Pythonic) | 3 |
| **Subtotal Unit 2** | | | | **10** |
| 3 | 5 | Percabangan | BK (logika) | 3 |
| 3 | 6 | Perulangan | BK (iterasi) | 3 |
| **Subtotal Unit 3** | | | | **6** |
| 4 | 7 | Function | AP (modularitas) | 4 |
| 4 | 8 | Error & Exception | AP (ketahanan) | 2 |
| 4 | 10 | Module & pip | AP (organisasi kode) | 2 |
| **Subtotal Unit 4** | | | | **8** |
| 5 | 12 | OOP Dasar | AP (class, inheritance, enkapsulasi) | 4 |
| 5 | **14 (baru)** | **Struktur Data Lanjutan & Library Standar** | **AP, BK** (collections, dataclasses, typing, heapq, itertools, abstract data structures) | **6** |
| **Subtotal Unit 5** | | | | **10** |
| 6 | **15 (baru)** | **Kompleksitas Algoritma & Analisis Strategi** | **BK, AP** (big-O, sorting/searching comparison, hashing, justifikasi efisiensi, trade-off) | **8** |
| **Subtotal Unit 6** | | | | **8** |
| 7 | **16 (baru)** | **Basis Data (SQL & SQLite)** | **AP, AD** (skema, ER, query, indexing, transaksi) | **6** |
| **Subtotal Unit 7** | | | | **6** |
| 8 | **17 (baru)** | **Testing, Dokumentasi & Kualitas Kode** | **AP** (static vs dynamic analysis, unittest/pytest, docstring, type hints, CI) | **4** |
| **Subtotal Unit 8** | | | | **4** |
| 9 | **18 (baru)** | **Jaringan & Model OSI** | **JKI** (topologi, OSI 7 layer, komponen, mekanisme pertukaran data) | **3** |
| 9 | **19 (baru)** | **Keamanan Digital & Siber** | **JKI, DSI** (cyber security, kontrol akses, konfigurasi keamanan, etika digital) | **3** |
| 9 | **20 (baru)** | **Dampak Sosial TIK — Studi Kasus & Argumentasi Kritis** | **DSI** (analisis kasus terkini, debat tertulis, position paper) | **4** |
| **Subtotal Unit 9** | | | | **10** |
| 10 | 13 | **Proyek Akhir PLB (Kelompok)** | **PLB, AP, BK, DSI, SK** (end-to-end: analisis → desain → implementasi → testing → presentasi + portofolio) | **10** |
| **Subtotal Unit 10** | | | | **10** |
| **TOTAL** | | | | **72** |

> **Catatan Proyek (Unit 10):** 10 JP = 4 sprint (minggu 29–32) + 2 minggu integrasi & testing + 2 minggu presentasi/demo day + 2 minggu refleksi & penilaian. Proyek **dikerjakan berkelompok** sepanjang Unit 5–9 (embedded), JP di atas untuk *milestone* formal.

---

## 4. Profil Pelajar Pancasila — Integrasi per Unit

| Dimensi | Unit yang Menguatkan | Indikator Observasi |
|---------|---------------------|---------------------|
| Bernalar Kritis | 6, 9, 10 | Menjelaskan *trade-off* algoritma, mengkritisi kebijakan keamanan, menilai solusi teman |
| Kreatif | 5, 10 | Merancang struktur data sendiri, desain arsitektur proyek |
| Mandiri | 4, 5, 7, 8 | Debug mandiri, *refactoring*, *self-review* sebelum PR |
| Berkebinekaan Global | 9, 10 | Kolaborasi tim heterogen, dokumentasi bilingual (ID/EN) |
| Bergotong Royong | 10 (PLB) | *Pair programming*, *code review* tim, *retrospective* |
| Beriman & Bertakwa | — | Disediakan ruang refleksi di *journal* proyek (opsional) |

---

## 5. Rencana Modul Baru (14–20) — Ringkasan Cakupan

| Modul | File Target | Fokus Utama | Elemen CP |
|-------|-------------|-------------|-----------|
| 14 | `modul/14-struktur-data-lanjutan.md` | `collections` (`deque`, `Counter`, `defaultdict`), `dataclasses`, `typing` (`TypeVar`, `Generic`, `Protocol`), `heapq`, `itertools`, pola *immutable* vs *mutable* | AP, BK |
| 15 | `modul/15-kompleksitas-algoritma.md` | Notasi big-O, analisis *best/average/worst*, sorting (Timsort, quicksort, mergesort), searching, hashing, *trade-off* ruang-waktu, studi kasus *benchmark* | BK, AP |
| 16 | `modul/16-basis-data.md` | Relasional vs NoSQL, SQL DDL/DML, SQLite *hands-on*, ER diagram, normalisasi, indeks, transaksi, *parameterized query* (anti-SQLi) | AP, AD |
| 17 | `modul/17-testing-dokumentasi.md` | `unittest` / `pytest`, *fixtures*, *coverage*, *static analysis* (`mypy`, `ruff`), docstring (Google/NumPy), *type hints* lanjutan, *semantic versioning* | AP |
| 18 | `modul/18-jaringan-osi.md` | Topologi (star, mesh, bus, ring), OSI 7 layer (fungsi & protokol per lapisan), *encapsulation*, TCP vs UDP, *handshake*, *socket* demo Python | JKI |
| 19 | `modul/19-keamanan-digital.md` | CIA triad, *threat modeling*, autentikasi/otorisasi, *hashing* password (`bcrypt`), HTTPS/TLS, *firewall* konsep, *OWASP Top 10* ringkas, etika *white hat* | JKI, DSI |
| 20 | `modul/20-dampak-sosial.md` | Studi kasus: *algorithmic bias*, *deepfake*, privasi data, *digital divide*, AI etika; *position paper* 1 halaman + debat terstruktur | DSI |

---

## 6. Alokasi JP per Semester (Untuk Kalender Akademik)

| Semester | Unit | JP |
|----------|------|----|
| Ganjil (Kelas XI) | 1–5 | 8 + 10 + 6 + 8 + 10 = **42** |
| Genap (Kelas XI) | 6–10 | 8 + 6 + 4 + 10 + 10 = **30** |
| **Total** | | **72** |

> Semester ganjil lebih padat karena fondasi. Semester genap fokus aplikasi & proyek.

---

## 7. Langkah Selanjutnya (Checklist Implementasi)

- [ ] Tulis 7 modul baru (14–20) — setiap modul: *target pemahaman*, analogi, contoh kode, latihan, checklist, referensi CP
- [ ] Tambahkan **tabel CP ringkas** di awal setiap modul (lama & baru)
- [ ] Buat `RPS.md` (Rencana Pelaksanaananaan Pembelajaran) detail per pertemuan
- [ ] Buat `lembar-kerja-siswa.md` (siap cetak A4, ruang tulis, *rubric* mini)
- [ ] Upgrade `modul/13-proyek-akhir.md` → template kelompok + rubrik penilaian
- [ ] Update `build.py` (tambah order modul baru), `index.html`, `README.md`
- [ ] Jalankan `python3 build.py` → verifikasi link, CJK, HTML valid

---

*Dokumen ini merupakan *single source of truth* untuk perancangan RPS, modul, dan asesmen. Setiap perubahan CP merujuk ke Kepmen 033/H/KR/2022.*