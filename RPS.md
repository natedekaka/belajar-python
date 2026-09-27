# RPS — Rencana Pelaksanaan Pembelajaran Informatika Kelas XI

**Mata Pelajaran:** Informatika  
**Fase:** F (Kelas XI–XII)  
**Semester:** Ganjil & Genap (Kelas XI)  
**Alokasi Waktu:** 72 JP (2 JP × 36 minggu)  
**Kurikulum:** Kurikulum Merdeka — Kepmen 033/H/KR/2022  
**Sumber CP:** Capaian Pembelajaran Informatika Fase F

---

## 1. Identitas Sekolah & Mata Pelajaran

| Item | Detail |
|------|--------|
| Nama Sekolah | [NAMA SEKOLAH] |
| Jenjang | SMA / MA |
| Kelas | XI |
| Mata Pelajaran | Informatika |
| Semester | Ganjil & Genap |
| Tahun Pelajaran | [TAHUN] |
| Guru | [NAMA GURU] |
| Alokasi Waktu | 72 JP (2 JP × 36 minggu) |

---

## 2. Capaian Pembelajaran (CP) Fase F — Ringkasan

| Elemen | Kode | Capaian (Ringkas) |
|--------|------|-------------------|
| Berpikir Komputasional | BK | Analisis strategi algoritmik alternatif, justifikasi efisiensi, pilih solusi optimal dengan struktur data kompleks |
| Teknologi Informasi & Komunikasi | TIK | (Integrasi di elemen lain) |
| Sistem Komputer | SK | Prototipe SW interaksi SBC/controller/kit elektronika |
| Jaringan Komputer & Internet | JKI | Konsep lanjutan: topologi, OSI Layer, keamanan siber, kontrol akses, konfigurasi jaringan |
| Analisis Data | AD | (Muatan diserap ke AP — library big data) |
| Algoritma & Pemrograman | AP | Program modular besar, struktur data abstrak + library standar (AI, big data), translasi bahasa |
| Dampak Sosial Informatika | DSI | Kajian kritis kasus sosial TIK terkini, argumentasi berbasis bukti |
| Praktik Lintas Bidang | PLB | Proyek tim inklusif end-to-end: analisis → desain → implementasi → testing → dokumentasi → presentasi |

---

## 3. Profil Pelajar Pancasila — Integrasi per Unit

| Dimensi | Unit yang Menguatkan | Indikator Observasi |
|---------|---------------------|---------------------|
| Bernalar Kritis | 6, 9, 10 | Jelaskan trade-off algoritma, kritik kebijakan keamanan, evaluasi solusi teman |
| Kreatif | 5, 10 | Rancang struktur data sendiri, desain arsitektur proyek |
| Mandiri | 4, 5, 7, 8 | Debug mandiri, refactoring, self-review sebelum PR |
| Berkebinekaan Global | 9, 10 | Kolaborasi tim heterogen, dokumentasi bilingual (ID/EN) |
| Bergotong Royong | 10 (PLB) | Pair programming, code review tim, retrospective |
| Beriman & Bertakwa | — | Ruang refleksi di journal proyek (opsional) |

---

## 4. Alokasi JP per Unit (72 JP Total)

| Unit | Modul | Judul | Elemen CP | JP |
|------|-------|-------|-----------|----|
| 1 | 0,1,2 | Fondasi: Setup, Variabel, String | AP (dasar) | 8 |
| 2 | 3,4,11 | Struktur Data Dasar: List/Tuple/Dict/Set, List Comp | AP, BK | 10 |
| 3 | 5,6 | Kontrol Alur: Percabangan, Perulangan | BK | 6 |
| 4 | 7,8,10 | Function, Error, Module/pip | AP | 8 |
| 5 | 12,14 | OOP Dasar + Struktur Data Lanjutan | AP, BK | 10 |
| 6 | 15 | Kompleksitas Algoritma & Analisis Strategi | BK, AP | 8 |
| 7 | 16 | Basis Data (SQL & SQLite) | AP, AD | 6 |
| 8 | 17 | Testing, Dokumentasi & Kualitas Kode | AP | 4 |
| 9 | 18,19,20 | Jaringan/OSI, Keamanan, Dampak Sosial | JKI, DSI | 10 |
| 10 | 13 | Proyek Akhir PLB (Kelompok) | PLB, AP, BK, DSI, SK | 10 |
| **TOTAL** | | | | **72** |

> **Catatan Proyek (Unit 10):** 10 JP = 4 sprint (minggu 29–32) + 2 minggu integrasi & testing + 2 minggu presentasi/demo day + 2 minggu refleksi & penilaian. Proyek dikerjakan berkelompok sepanjang Unit 5–9 (embedded), JP di atas untuk milestone formal.

---

## 5. ATP — Alur Tujuan Pembelajaran per Pertemuan (Contoh Semester Ganjil)

| Minggu | JP | Modul | Tujuan Pembelajaran (TP) | Bentuk Asesmen |
|--------|----|-------|--------------------------|----------------|
| 1 | 2 | 0 | Siapkan lingkungan (Colab / local), jalankan `print("Halo")`, kenal REPL | Observasi + cek instalasi |
| 2 | 2 | 1 | Deklarasi variabel, tipe `int/float/str/bool`, `type()`, konversi tipe | Latihan Modul 1 |
| 3 | 2 | 1 | Operator aritmatika, precedence, input/output, f-string | Kuis singkat |
| 4 | 2 | 2 | String slicing, method (`split`, `join`, `replace`, `strip`), formatting | Latihan Modul 2 |
| 5 | 2 | 3 | List: index, slice, `append/extend/pop`, loop `for x in list` | Latihan Modul 3 |
| 6 | 2 | 3 | Tuple: immutable, unpacking, `enumerate`, `zip` | Kuis Modul 3 |
| 7 | 2 | 4 | Dictionary: CRUD, `get`, `setdefault`, loop `items()`, Set operasi | Latihan Modul 4 |
| 8 | 2 | 4 | Dictionary comprehension, set operation, nested dict | Kuis Modul 4 |
| 9 | 2 | 11 | List comprehension: filter, transform, nested, walrus operator | Latihan Modul 11 |
| 10 | 2 | 5 | `if/elif/else`, boolean logic, truthy/falsy, ternary operator | Latihan Modul 5 |
| 11 | 2 | 5 | Nested conditional, *guard clause*, *short-circuit* evaluation | Kuis Modul 5 |
| 12 | 2 | 6 | `for` loop, `range()`, `while`, `break/continue`, `else` clause | Latihan Modul 6 |
| 13 | 2 | 6 | Nested loop, pattern printing, loop invariants | Kuis Modul 6 |
| 14 | 2 | 7 | `def`, parameter (pos/kw/default), `return`, scope (LEGB), `lambda` | Latihan Modul 7 |
| 15 | 2 | 7 | `*args`, `**kwargs`, docstring, type hints, recursion dasar | Kuis Modul 7 |
| 16 | 2 | 8 | `try/except/else/finally`, exception hierarchy, `raise`, custom exception | Latihan Modul 8 |
| 17 | 2 | 10 | `import`, `from ... import`, stdlib (`random`, `datetime`, `pathlib`), `pip`, virtual env | Latihan Modul 10 |
| 18 | 2 | 12 | Class, `__init__`, `self`, method, attribute, `__str__`, `__repr__` | Latihan Modul 12 |
| 19 | 2 | 12 | Inheritance, `super()`, method overriding, class variable vs instance | Latihan Modul 12 |
| 20 | 2 | 14 | `collections` (`deque`, `Counter`, `defaultdict`), `namedtuple` | Latihan Modul 14 |
| 21 | 2 | 14 | `dataclasses`, `field`, `frozen=True`, `typing` (`TypeVar`, `Generic`, `Protocol`, `TypedDict`) | Latihan Modul 14 |
| 22 | 2 | 14 | `heapq` (priority queue), `itertools` (product, permutations, accumulate) | Kuis Modul 14 |
| 23 | 2 | 15 | Big-O, best/avg/worst, hirarki kompleksitas, analisis loop & rekursi | Latihan Modul 15 |
| 24 | 2 | 15 | Sorting: Timsort, Quicksort, Mergesort, Heapsort — bandingkan & justifikasi | Latihan Modul 15 |
| 25 | 2 | 15 | Hashing & dict internals, collision, `heapq` aplikasi, benchmark `timeit`/`cProfile` | Kuis Modul 15 |
| 26 | 2 | 16 | ER diagram → DDL, PK/FK, `PRAGMA foreign_keys=ON`, `sqlite3` CRUD | Latihan Modul 16 |
| 27 | 2 | 16 | JOIN (INNER/LEFT), GROUP BY + agregat, subquery, transaksi `BEGIN/COMMIT/ROLLBACK` | Latihan Modul 16 |
| 28 | 2 | 16 | Indexing (`EXPLAIN QUERY PLAN`), migrasi skema, upsert `ON CONFLICT` | Kuis Modul 16 |
| 29 | 2 | 17 | `pytest` (fixture, parametrize, mock), `unittest`, coverage (line & branch) | Latihan Modul 17 |
| 30 | 2 | 17 | `mypy` strict, `ruff` lint+format, docstring Google style, SemVer, `pre-commit` | Latihan Modul 17 |
| 31 | 2 | 18 | 7 layer OSI, PDU, protokol per layer, topologi, addressing (MAC/IP/Port) | Latihan Modul 18 |
| 32 | 2 | 18 | Encapsulation, TCP 3-way handshake, state diagram, socket TCP/UDP Python | Latihan Modul 18 |
| 33 | 2 | 19 | CIA Triad, STRIDE, OWASP Top 10, `bcrypt`, JWT, MFA, RBAC vs ABAC | Latihan Modul 19 |
| 34 | 2 | 19 | TLS/HTTPS, Let's Encrypt, firewall/UFW, VLAN/DMZ, Zero Trust, `fail2ban` | Kuis Modul 19 |
| 35 | 2 | 20 | PERSIA+Etika, 6 studi kasus (COMPAS, Deepfake, CA, Digital Divide, GenAI, Gig) | Latihan Modul 20 |
| 36 | 2 | 20 | CER writing, Position Paper, debat terstruktur, *responsible innovation* (AREA) | Kuis Modul 20 |

**Semester Genap (Minggu 19–36 di atas) — Lanjut Proyek:**

| Minggu | JP | Modul | Tujuan Pembelajaran | Bentuk Asesmen |
|--------|----|-------|---------------------|----------------|
| 19–22 | 8 | 13 (Proyek) | Sprint 1–4: Analisis kebutuhan → Desain ER & UI → Implementasi core (models, utils) → Integrasi DB & CLI | Sprint review (mingguan) |
| 23–24 | 4 | 13 | Integrasi penuh, testing (pytest), bug fixing, dokumentasi (README, docstring) | Code review tim |
| 25–26 | 4 | 13 | Demo day: presentasi 10 menit + Q&A 5 menit per kelompok | Presentasi + rubrik |
| 27–28 | 4 | 13 | Refleksi individu (journal), penilaian portofolio (GitHub repo), perbaikan akhir | Portofolio + refleksi |

---

## 6. KKTP — Kriteria Ketuntasan Pembelajaran (Contoh per Modul)

| Modul | KKTP (Minimal) |
|-------|----------------|
| 0–2 | Bisa install Python, jalankan REPL, tulis program input/output variabel & string |
| 3–4 | Bisa manipulasi list/tuple/dict/set untuk persoalan data sederhana |
| 5–6 | Bisa tulis percabangan & perulangan bersarang untuk pola & logika |
| 7–8 | Bisa bikin function reusable, handle error, pakai module stdlib |
| 10–11 | Bisa list comprehension & module/pip untuk kode Pythonic |
| 12 | Bisa desain class dengan inheritance & encapsulation |
| 14 | Bisa pilih & pakai `deque`/`Counter`/`defaultdict`/`dataclass`/`heapq`/`itertools` tepat |
| 15 | Bisa hitung Big-O, bandingkan sorting, justify pilihan algoritma tabel CER |
| 16 | Bisa desain ER → DDL, tulis query JOIN/agregat/subquery, pakai transaksi & parameterized query |
| 17 | Bisa tulis test pytest (fixture/parametrize/mock), coverage ≥80%, mypy strict pass, ruff clean |
| 18 | Bisa jelaskan OSI 7 layer, TCP vs UDP, tulis socket client/server sederhana |
| 19 | Bisa terapkan STRIDE, hash password bcrypt, JWT auth, jelaskan OWASP Top 10 mitigasi |
| 20 | Bisa tulis Position Paper CER, debat terstruktur, analisis kasus PERSIA+Etika |
| 13 | Bisa kerjakan proyek kelompok end-to-end: Git workflow, CI, demo, portofolio GitHub |

---

## 7. Asesmen — Bobot & Jenis

| Jenis Asesmen | Bobot | Deskripsi |
|---------------|-------|-----------|
| **Harian / Latihan Modul** | 20% | Checklist latihan per modul (terverifikasi guru) |
| **Kuis / Formatif** | 15% | Kuis singkat tiap 2–3 modul (Google Form / kertas) |
| **Tugas / Lembar Kerja** | 15% | Lembar kerja siswa per modul (dikumpulkan, dinilai rubrik mini) |
| **Proyek Akhir (PLB)** | 35% | Kelompok 3–4 orang: repo GitHub + demo + presentasi + portofolio individu |
| **Refleksi & Partisipasi** | 15% | Journal refleksi mingguan, partisipasi debat/diskusi, *peer review* |

**Skala Penilaian:** 0–100 → Konversi ke Predikat (A/B/C/D) per kebijakan sekolah.

---

## 8. Sumber Belajar & Referensi

1. **Modul 0–20** — Repository ini (`modul/00-setup.md` s.d `modul/20-dampak-sosial.md`)
2. **PETA-KURIKULUM.md** — Peta CP, modul, JP, profil Pelajar Pancasila
3. **Bank Soal** — `bank-soal.md` (guru), `bank-soal-siswa.md` (siswa)
4. **Cheat Sheet** — `cheat-sheet.md` (syntax reference 1 halaman)
4. **Error Dictionary** — `error-dictionary.md` (15+ error Python + solusi)
5. **Tips Mengajar** — `tips-mengajar.md` (strategi, analogi, jebakan per modul)
6. **Mini Projek** — `mini-projek.md` (13 projek bertingkat)
7. **Scripts** — `scripts/` (tools administrasi guru)
8. **Referensi Eksternal:**
   - Kepmen 033/H/KR/2022 (CP Informatika)
   - Buku "Informatika Fase F" Kemendikbudristek
   - Python Docs (https://docs.python.org/3/)
   - Real Python (https://realpython.com/)
   - OWASP Top 10 (https://owasp.org/www-project-top-ten/)
   - UNESCO AI Ethics (https://unesdoc.unesco.org/ark:/48223/pf0000377897)

---

## 9. Catatan Khusus Guru

- **Diferensiasi:** Siswa cepat → lanjut ke modul 14+ lebih awal / bantu *peer tutoring*. Siswa butuh bantuan → *pair programming* + latihan tambahan `scripts/` untuk drill.
- **Keamanan Lab:** Semua praktik keamanan (Modul 19) **hanya** di lingkungan VM / sandbox terisolasi (TryHackMe, Hack The Box, PicoCTF). **Tidak pernah** serang sistem nyata tanpa izin.
- **AI Generatif:** Diperbolehkan sebagai *learning companion* (jelaskan konsep, debug, *refactor*). **Wajib** siswa: (1) tulis *prompt* yang dipakai, (2) verifikasi output, (3) sitasi di kode (`# Generated with ChatGPT, verified by me`). Guru cek pemahaman via *live coding* / *oral exam*.
- **Portofolio:** Proyek akhir (Modul 13) **wajib** di-push ke GitHub public/private dengan: `README.md`, `requirements.txt`, `LICENSE`, GitHub Actions CI, *release* v1.0. Jadi bukti kompetensi untuk kuliah / magang.

---

*Dokumen ini merupakan *living document* — update tiap semester berdasarkan evaluasi & kebutuhan siswa.*