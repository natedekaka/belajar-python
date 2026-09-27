# 📦 Template Proyek Akhir — Aplikasi CLI Manajemen Sekolah

**Kelompok:** ________________________   **Anggota:** ___________________________________________________  
**Kelas:** ______   **Semester:** ______   **Tahun:** ______

---

## 1. Ringkasan Proyek (Maks 150 Kata)

> Tuliskan: **Apa** yang dibangun, **untuk siapa**, **masalah apa** yang diselesaikan, **fitur utama** apa saja.

____________________________________________________________________________________
____________________________________________________________________________________
____________________________________________________________________________________
____________________________________________________________________________________

---

## 2. Analisis Kebutuhan (User Stories)

| ID | Sebagai | Saya Ingin | Agar | Prioritas (Must/Should/Could) |
|----|---------|------------|------|-------------------------------|
| US-01 | Guru BK | input nilai siswa per mapel | rapor otomatis tercipta | Must |
| US-02 | Wali Kelas | lihat statistik kelas | monitoring performa cepat | Must |
| US-03 | Siswa | lihat nilai & rapor sendiri | transparansi & motivasi | Should |
| US-04 | Admin | backup & restore data CSV/JSON | keamanan data | Could |
| US-05 | Guru | ranking siswa per semester | identifikasi siswa berprestasi / butuh bimbingan | Should |

> Tambah baris sesuai kebutuhan (minimal 5 user stories).

---

## 3. Desain Sistem

### 3.1 ER Diagram (Gambar / Teks)
```
[Siswa] 1 ───< [Nilai] >─── 1 [MataPelajaran]
   │                          │
   1                          1
   │                          │
[Kelas]                      [Semester]
```
> Tempel foto diagram draw.io / mermaid / PlantUML di sini.

### 3.2 Arsitektur Kode (Modul)

```
proyek-akhir/
├── main.py              # Entry point — menu utama
├── models.py            # Class: Siswa, Kelas, MataPelajaran, Nilai
├── repository.py        # Data access (SQLite) — CRUD + query kompleks
├── services.py          # Business logic: hitung rata2, grade, ranking, statistik
├── cli.py               # UI: menu, input validation, pretty print (rich/tabulate)
├── utils.py             # Helper: format, export CSV/JSON, validasi
├── config.py            # Konfigurasi: DB_PATH, GRADE_SCALE, EXPORT_DIR
├── tests/
│   ├── test_models.py
│   ├── test_repository.py
│   ├── test_services.py
│   └── conftest.py      # pytest fixtures
├── requirements.txt     # dependencies (rich, tabulate, pytest, etc.)
├── README.md            # Cara install & jalankan
├── LICENSE              # MIT / Apache-2.0
└── .github/workflows/ci.yml  # CI pipeline
```

---

## 4. Rincian Fitur & Checklist Implementasi

| Fitur | Deskripsi Singkat | Checklist (☑) |
|-------|-------------------|---------------|
| **Manajemen Siswa** | Tambah, lihat, cari (NIS/nama), hapus, pindah kelas | ☐ |
| **Manajemen Kelas** | CRUD kelas, wali kelas, daftar siswa per kelas | ☐ |
| **Manajemen Mapel** | CRUD mapel, SKS, guru pengampu | ☐ |
| **Input Nilai** | Per siswa per mapel per semester, validasi 0–100 | ☐ |
| **Hitung Otomatis** | Rata-rata, grade (A–E), ranking kelas | ☐ |
| **Cetak Rapor** | Per siswa (detail per mapel + rata2 + grade + ranking) | ☐ |
| **Statistik Kelas** | Rata2 per mapel, min/max, distribusi grade, siswa butuh bimbingan | ☐ |
| **Simpan/Buka** | SQLite (default), Export/Import CSV & JSON | ☐ |
| **Autentikasi** | Login guru (bcrypt hash), session sederhana | ☐ |
| **Logging** | Audit trail: siapa apa kapan (login, input nilai, hapus) | ☐ |
| **Testing** | pytest ≥ 80% branch coverage (models, repo, services) | ☐ |
| **CI/CD** | GitHub Actions: lint (ruff) → type-check (mypy) → test → coverage gate | ☐ |
| **Dokumentasi** | README (install, run, test), docstring Google style, CHANGELOG.md | ☐ |

---

## 5. Rencana Sprint (4 Sprint × 2 JP = 8 JP + Buffer)

| Sprint | Minggu | Fokus | Deliverable | PIC |
|--------|--------|-------|-------------|-----|
| **Sprint 1** | 1–2 | Setup repo, ER → DDL, `models.py`, `repository.py` (CRUD dasar) | Repo GitHub + DB schema + CRUD test pass | |
| **Sprint 2** | 3–4 | `services.py` (logic bisnis), `cli.py` menu utama, input validasi | CLI jalan: CRUD siswa/kelas/mapel + input nilai | |
| **Sprint 3** | 5–6 | Rapor, statistik, export/import, auth bcrypt, logging | Fitur lengkap + test coverage ≥ 80% | |
| **Sprint 4** | 7–8 | Polish UI (rich/tabulate), CI pipeline, README, demo prep | Repo production-ready + slide presentasi | |
| **Buffer** | 9–10 | Bug fixing, integrasi, demo day, refleksi | Demo day + portofolio GitHub | |

> **Daily Standup (5 menit tiap JP):** Apa kemarin? Apa hari ini? Blocker apa?

---

## 6. Teknologi & Library

| Kategori | Pilihan | Alasan |
|----------|---------|--------|
| Bahasa | Python 3.10+ | Type hints modern, match-case, performance |
| Database | SQLite (`sqlite3` stdlib) | Zero-config, file-based, ACID, cukup untuk skala sekolah |
| CLI UI | `rich` + `tabulate` | Warna, tabel cantik, progress bar, prompt |
| Testing | `pytest` + `pytest-cov` + `pytest-mock` | Industri standar, fixture powerful |
| Lint/Format | `ruff` | Super cepat, all-in-one (lint + format + isort + pyupgrade) |
| Type Check | `mypy` (strict) | Tangkap bug sebelum jalan |
| CI | GitHub Actions | Gratis, terintegrasi GitHub, matrix testing |
| Versioning | SemVer + `CHANGELOG.md` | Profesional, jelas breaking changes |

---

## 7. Risiko & Mitigasi

| Risiko | Probabilitas | Dampak | Mitigasi |
|--------|--------------|--------|----------|
| Anggota tidak kontribusi merata | Tinggi | Sedang | *Peer evaluation* mingguan, *individual commit* wajib min 2/sprint |
| Scope creep (tambah fitur di tengah) | Tinggi | Sedang | *Product backlog* diprioritaskan, *scope freeze* Sprint 3 |
| Merge conflict berat | Sedang | Tinggi | *Feature branch* per fitur, PR review wajib, `rebase` rutin |
| DB corrupt / data hilang | Rendah | Sangat Tinggi | Backup otomatis harian (script), `git` history, export CSV berkala |
| Library tidak kompatibel | Rendah | Sedang | Pin version di `requirements.txt`, test di CI matrix Python 3.10–3.12 |

---

## 8. Kriteria Selesai (*Definition of Done*)

- [ ] Semua *user stories* **Must** & **Should** terimplementasi & tested
- [ ] `pytest --cov --cov-branch --cov-fail-under=80` **PASS**
- [ ] `mypy .` **PASS** (strict mode)
- [ ] `ruff check . && ruff format --check .` **PASS**
- [ ] GitHub Actions CI **green** di branch `main`
- [ ] `README.md` lengkap: install, run, test, kontribusi, lisensi
- [ ] `CHANGELOG.md` terupdate (v1.0.0)
- [ ] Demo day: presentasi 10 menit + Q&A 5 menit, repo public/private akses guru
- [ ] Refleksi individu dikumpulkan (Google Form / kertas)

---

## 9. Catatan Tambahan / Ide Ekstra (Opsional)

- [ ] **GUI versi** (Tkinter / PyQt / Flet) — *bonus*
- [ ] **Web API** (FastAPI) + frontend sederhana — *bonus*
- [ ] **Dockerize** (`Dockerfile`, `docker-compose.yml`) — *bonus*
- [ ] **Notifikasi** (email/Telegram bot) untuk nilai < KKM — *bonus*
- [ ] **Dashboard** (Streamlit / Plotly Dash) untuk visualisasi statistik — *bonus*

---

*Template ini bebas dimodifikasi sesuai kebutuhan kelompok.  
Tujuannya: **struktur jelas**, **beban adil**, **kode berkualitas**, **portofolio bangga**.*