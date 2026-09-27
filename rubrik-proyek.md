# 📊 Rubrik Penilaian Proyek Akhir — Informatika Kelas XI (Fase F)

**Komponen:** Proyek Akhir PLB (Praktik Lintas Bidang)  
**Bobot:** 35% dari nilai akhir  
**Kelompok:** 3–4 orang  
**Durasi:** 10 JP (4 sprint + integrasi + demo + refleksi)

---

## 🎯 Tujuan Penilaian

Mengukur kemampuan siswa:
1. **Teknis:** Mengimplementasikan program modular besar, database, testing, CI/CD
2. **PLB:** Kolaborasi tim inklusif, *software engineering lifecycle* end-to-end
3. **Komunikasi:** Dokumentasi, presentasi, *code review*, refleksi
4. **Etika & Karakter:** Integritas akademik, *responsible coding*, *peer support*

---

## 📋 Rubrik Detail (Total 100 Poin)

### A. Kualitas Teknis & Kode (40 poin)

| Sub-Kriteria | Indikator | Skor (0–10) |
|--------------|-----------|-------------|
| **A1. Fungsionalitas & Kelengkapan** | Semua *user stories* Must & Should berjalan tanpa bug kritis; fitur Could sebagai bonus | |
| **A2. Arsitektur & Modularitas** | Pemisahan *concerns* (models, repository, services, cli, utils); low coupling, high cohesion; pakai type hints & docstring | |
| **A3. Database & Query** | ER → DDL benar (PK, FK, index, constraint); parameterized query; transaksi ACID; query efisien (JOIN, agregat, subquery) | |
| **A4. Testing & Kualitas** | `pytest` branch coverage ≥ 80%; test *unit* + *integration*; `mypy strict` pass; `ruff` clean; CI green | |
| **Total A** | | **___ / 40** |

### B. Proses PLB & Kolaborasi (25 poin)

| Sub-Kriteria | Indikator | Skor (0–5) |
|--------------|-----------|------------|
| **B1. Perencanaan & Sprint** | *Sprint planning* jelas; *backlog* terprioritaskan; *Definition of Done* disepakati; *burndown* / progress tracking | |
| **B2. Git Workflow** | *Feature branch* per fitur; *commit message* konvensional (Conventional Commits); PR review minimal 1 reviewer; *merge* via PR (bukan push langsung ke main) | |
| **B3. Kolaborasi Tim** | *Standup* rutin; *pair programming* / *mob programming* minimal 2×; *conflict resolution* konstruktif; *peer support* (bantu teman stuck) | |
| **B4. Dokumentasi Proses** | `CHANGELOG.md` per rilis; *meeting notes* singkat per sprint; *retrospective* akhir sprint (start/stop/continue) | |
| **B5. Etika & Integritas** | Kode original (bukan copy-paste tanpa paham); *AI-assisted* dicatat & diverifikasi; *license* & *credit* library; tidak *hardcode* secret | |
| **Total B** | | **___ / 25** |

### C. Produk & User Experience (15 poin)

| Sub-Kriteria | Indikator | Skor (0–5) |
|--------------|-----------|------------|
| **C1. CLI UX** | Menu intuitif; validasi input ramah; error message jelas; output tabel warna (`rich`/`tabulate`); *help* kontekstual | |
| **C2. Instalasi & Portabilitas** | `README.md` lengkap (prasyarat, install, run, test, troubleshoot); `requirements.txt` pin version; jalan di Linux/Win/macOS tanpa config manual | |
| **C3. Dokumentasi Pengguna** | *User guide* singkat (PDF/Markdown): *screenshot* menu, alur kerja, FAQ; *developer guide* (arsitektur, kontribusi, testing) | |
| **Total C** | | **___ / 15** |

### D. Presentasi & Komunikasi (10 poin)

| Sub-Kriteria | Indikator | Skor (0–5) |
|--------------|-----------|------------|
| **D1. Presentasi Demo (10 menit)** | Alur cerita jelas (masalah → solusi → demo live → tantangan → lesson learned); slide visual minimalis; demo *live* lancar (siapkan *fallback* video) | |
| **D2. Q&A (5 menit)** | Jawab teknis & non-teknis percaya diri; jujur soal keterbatasan; terima masukan terbuka | |
| **Total D** | | **___ / 10** |

### E. Refleksi Individu & Portofolio (10 poin)

| Sub-Kriteria | Indikator | Skor (0–5) |
|--------------|-----------|------------|
| **E1. Refleksi Tertulis (200–300 kata)** | *What went well*, *what didn't*, *what I learned*, *what I'd do differently*; bukti *growth mindset*; contoh spesifik (bukan generik) | |
| **E2. Portofolio GitHub** | Repo *public* (atau *private* dengan akses guru); *release* v1.0.0; *topics* tag; *description* jelas; *README* badge (CI, coverage, license); *commit history* rapi | |
| **Total E** | | **___ / 10** |

---

## 📝 Total Nilai Akhir

| Komponen | Maks | Diperoleh |
|----------|------|-----------|
| A. Kualitas Teknis & Kode | 40 | ___ |
| B. Proses PLB & Kolaborasi | 25 | ___ |
| C. Produk & User Experience | 15 | ___ |
| D. Presentasi & Komunikasi | 10 | ___ |
| E. Refleksi & Portofolio | 10 | ___ |
| **TOTAL** | **100** | **___** |

**Konversi ke Nilai Raport (0–100):** `Total` (sudah skala 100)

---

## ✅ Checklist *Must-Have* (Jika Tidak Terpenuhi → Otomatis Batas Nilai)

| Item | Wajib? | Catatan |
|------|--------|---------|
| Repo GitHub dengan minimal 20 commit tersebar 4 sprint | Ya | Tidak = max 70 |
| `pytest` coverage ≥ 80% branch | Ya | Tidak = max 75 |
| `mypy strict` pass | Ya | Tidak = max 80 |
| `ruff` clean (lint + format) | Ya | Tidak = max 80 |
| CI GitHub Actions green di `main` | Ya | Tidak = max 80 |
| `README.md` + `LICENSE` + `CHANGELOG.md` | Ya | Tidak = max 85 |
| Semua anggota punya minimal 5 commit *meaningful* | Ya | Tidak = nilai individu -10 |
| Presentasi demo day dihadiri semua anggota | Ya | Tidak = nilai individu -15 |
| Refleksi individu dikumpulkan tepat waktu | Ya | Tidak = nilai individu -10 |

---

## 🏷️ Deskripsi Predikat (Referensi)

| Skor | Predikat | Deskripsi |
|------|----------|-----------|
| 90–100 | **A (Sangat Baik)** | Produk *production-ready*, tim *high-performing*, dokumentasi teliti, presentasi meyakinkan |
| 80–89 | **B (Baik)** | Produk berfungsi baik, minor bug non-kritis, kolaborasi baik, dokumentasi cukup |
| 70–79 | **C (Cukup)** | Fitur inti jalan, tapi ada *technical debt* signifikan / kolaborasi kurang merata / dokumen minim |
| 60–69 | **D (Kurang)** | Fitur *Must* tidak lengkap / bug kritis / coverage rendah / tidak ada CI / presentasi tidak siap |
| < 60 | **E (Gagal)** | Proyek tidak berfungsi / tidak dikumpulkan / plagiarisme / tidak ada kontribusi individu |

> **Catatan:** Nilai **individu** = `Nilai Kelompok` ± `Adjustment Individu` (berdasarkan commit log, *peer evaluation*, refleksi, kehadiran *standup*). Guru berhak menyesuaikan ±15 poin per individu.

---

## 📝 *Peer Evaluation* Formulir (Diisi Setiap Anggota untuk Anggota Lain)

**Nama Penilai:** ________________________   **Nama Dinilai:** ________________________  

| Aspek | Skala 1–5 (1=Sangat Kurang, 5=Sangat Baik) | Bukti / Contoh |
|-------|--------------------------------------------|----------------|
| Kontribusi kode (kuantitas & kualitas) | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Kehadiran & partisipasi *standup* | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| *Code review* & *feedback* konstruktif | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Bantuan ke teman (*pair programming*, debug) | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| Komunikasi & *conflict resolution* | ☐1 ☐2 ☐3 ☐4 ☐5 | |
| **Rata-rata** | **___ / 5** | |

**Komentar Tambahan (Opsional):**  
______________________________________________________________________________
______________________________________________________________________________

*Formulir ini rahasia — hanya guru yang melihat. Hasil rata-rata *peer evaluation* mempengaruhi *Adjustment Individu* (±10 poin).*

---

## 📅 Jadwal Penilaian

| Tahap | Minggu | Penilai | Output |
|-------|--------|---------|--------|
| Sprint Review 1–4 | Minggu 1–8 | Guru + Tim | *Checkpoint* verbal + cek repo |
| Code Review Akhir | Minggu 9 | Guru | Review PR final + rubrik A |
| Demo Day | Minggu 9–10 | Guru + Kelas | Presentasi + Q&A (rubrik D) |
| Refleksi & *Peer Eval* | Minggu 10 | Individu | Formulir + refleksi (rubrik E) |
| **Nilai Akhir Diumumkan** | Minggu 11 | Guru | Nilai individu + kelompok |

---

*Rubrik ini bersifat *living document* — boleh disesuaikan guru selama transparan ke siswa sebelum proyek dimulai.*