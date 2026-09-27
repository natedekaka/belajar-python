# Modul 17: Testing, Dokumentasi & Kualitas Kode

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Algoritma & Pemrograman | AP | Memahami, memelihara, menyempurnakan struktur program (aspek statik & dinamis), kualitas kode, dokumentasi |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menulis **unit test** dengan `unittest` & `pytest` (fixtures, parametrize, mock)
- Mengukur **code coverage** & memahami *branch coverage* vs *line coverage*
- Memasang **static type checking** dengan `mypy` (strict mode)
- Memasang **linting & formatting** otomatis: `ruff` (lint + format), `black` (format)
- Menulis **docstring** standar (Google / NumPy) + *type hints* lengkap
- Memahami **Semantic Versioning** (SemVer) & *changelog*
- Menyiapkan **CI pipeline** minimal (GitHub Actions) yang jalankan: lint → type-check → test → coverage gate

---

## 1. Kenapa Testing & Kualitas Otomatis?

| Tanpa Otomatisasi | Dengan Otomatisasi |
|-------------------|-------------------|
| Test manual → lupa, malas, tidak konsisten | `pytest` jalan tiap commit → **regression tertangkap** |
| Bug deploy ke produksi → murid kecewa | CI gate → **merge diblokir kalau gagal** |
| Kode "spaghetti" → sulit dibaca tim | `ruff` + `black` → **style seragam** otomatis |
| Type bug runtime (`AttributeError`) | `mypy` → **tangkap sebelum jalan** |
| Dokumentasi ketinggalan update | Docstring + type hints = **dokumentasi hidup** |

> 💡 **Investasi awal 30 menit setup CI = hemat jam debugging nanti.**

---

## 2. `pytest` — Modern Testing Framework

```bash
pip install pytest pytest-cov pytest-mock
```

```python
# tests/test_utils.py
import pytest
from utils import hitung_rata_rata, grade_dari_nilai

# Fixture — data reusable
@pytest.fixture
def sample_nilai():
    return [80, 90, 75, 85, 95]

# Parametrize — banyak input, satu test
@pytest.mark.parametrize("nilai,expected_grade", [
    (95, "A"), (85, "B"), (75, "C"), (65, "D"), (55, "E"),
    (100, "A"), (0, "E"),
])
def test_grade_dari_nilai(nilai, expected_grade):
    assert grade_dari_nilai(nilai) == expected_grade

# Test exception
def test_hitung_rata_rata_kosong_raise():
    with pytest.raises(ValueError, match="tidak boleh kosong"):
        hitung_rata_rata([])

# Mock — isolate external dependency
def test_fetch_data_mock(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"data": [1,2,3]}
    mocker.patch("requests.get", return_value=mock_response)

    from utils import fetch_api
    result = fetch_api("https://api.example.com")
    assert result == [1,2,3]
```

**Jalankan:**
```bash
pytest                          # semua test
pytest -v                       # verbose
pytest -k "grade"               # filter nama
pytest --cov=utils --cov-report=term-missing  # coverage
pytest --cov-fail-under=80      # gate: minimal 80% coverage
```

---

## 3. `unittest` — Built-in (Tidak Perlu Install)

```python
# tests/test_models_unittest.py
import unittest
from models import Siswa, Kelas

class TestSiswa(unittest.TestCase):
    def setUp(self):
        self.s = Siswa("123", "Ani", "XI-1")

    def test_tambah_nilai_dan_rata_rata(self):
        self.s.tambah_nilai("Matematika", 80)
        self.s.tambah_nilai("Fisika", 90)
        self.assertAlmostEqual(self.s.rata_rata(), 85.0)

    def test_rata_rata_kosong_raise(self):
        with self.assertRaises(ValueError):
            self.s.rata_rata()

    def test_laporan_contains_nama(self):
        self.s.tambah_nilai("Matematika", 80)
        lap = self.s.laporan()
        self.assertIn("Ani", lap)
        self.assertIn("80", lap)

if __name__ == "__main__":
    unittest.main()
```

---

## 4. Coverage — Apa Saja yang Tercakap?

```bash
# Line coverage (default)
pytest --cov=utils --cov-report=term-missing

# Branch coverage (lebih ketat)
pytest --cov=utils --cov-branch --cov-report=term-missing
```

**Contoh output `term-missing`:**
```
Name                 Stmts   Miss Branch BrPart  Missing
--------------------------------------------------------
utils.py                25      2      6      2   18-19, 45-46
```
- **Stmts** = statements
- **Miss** = baris tidak dieksekusi
- **Branch** = cabang keputusan (if/else)
- **BrPart** = cabang parsial (satu sisi saja)
- **Missing** = nomor baris yang *miss*

> 💡 Target **branch coverage ≥ 80%** lebih sehat dari line coverage saja.

---

## 5. `mypy` — Static Type Checking

```bash
pip install mypy
```

```ini
# mypy.ini (atau pyproject.toml)
[mypy]
python_version = 3.10
strict = true                    # semua check ketat
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
```

```python
# utils.py — contoh typed dengan benar
from typing import List, Dict, Optional

def hitung_rata_rata(nilai: List[float]) -> float:
    """Hitung rata-rata list angka.

    Args:
        nilai: List nilai numerik (tidak boleh kosong).

    Returns:
        Rata-rata sebagai float.

    Raises:
        ValueError: Jika list kosong.
    """
    if not nilai:
        raise ValueError("List nilai tidak boleh kosong")
    return sum(nilai) / len(nilai)

# Generic function
from typing import TypeVar, Sequence

T = TypeVar("T")

def pertama(seq: Sequence[T]) -> Optional[T]:
    """Return elemen pertama atau None jika kosong."""
    return seq[0] if seq else None
```

**Jalankan:**
```bash
mypy utils.py models.py main.py
# atau
mypy .                    # cek seluruh project
```

> ⚠️ `strict = true` **akan mengeluarkan error** untuk kode tanpa type hints. Tambahkan type hints secara bertahap.

---

## 6. `ruff` — Linter & Formatter Super Cepat (Rust)

```bash
pip install ruff
```

```toml
# pyproject.toml
[tool.ruff]
line-length = 100
target-version = "py310"
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (import sorting)
    "N",   # pep8-naming
    "UP",  # pyupgrade
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "T20", # flake8-print (print statement)
]
ignore = ["E501"]  # line too long (formatter handle)
fixable = ["ALL"]
unfixable = []

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
```

**Jalankan:**
```bash
ruff check .        # lint only
ruff check --fix .  # auto-fix
ruff format .       # format (like black)
ruff format --check .  # check only (CI gate)
```

> 💡 `ruff` menggantikan `flake8` + `isort` + `black` + `pyupgrade` — **satu tool, super cepat**.

---

## 7. Docstring Standar — Google Style (Direkomendasikan)

```python
def hitung_statistik(nilai: List[float]) -> Dict[str, float]:
    """Hitung statistik deskriptif dasar dari list nilai.

    Args:
        nilai: List nilai numerik. Minimal 1 elemen.

    Returns:
        Dict dengan keys: 'mean', 'min', 'max', 'stdev' (populasi).

    Raises:
        ValueError: Jika list kosong atau hanya 1 elemen (stdev butuh ≥2).

    Example:
        >>> hitung_statistik([80, 90, 100])
        {'mean': 90.0, 'min': 80.0, 'max': 100.0, 'stdev': 8.16...}
    """
    if not nilai:
        raise ValueError("List tidak boleh kosong")
    if len(nilai) == 1:
        raise ValueError("Butuh minimal 2 nilai untuk stdev")

    mean = sum(nilai) / len(nilai)
    varians = sum((x - mean) ** 2 for x in nilai) / len(nilai)
    return {
        "mean": mean,
        "min": min(nilai),
        "max": max(nilai),
        "stdev": varians ** 0.5,
    }
```

**Generate docs otomatis:**
```bash
pip install pdoc
pdoc -o docs/html utils.py models.py
# atau
pip install mkdocstrings mkdocs
mkdocs serve
```

---

## 8. Semantic Versioning (SemVer) & Changelog

```
MAJOR.MINOR.PATCH   (contoh: 2.4.1)

MAJOR   — Breaking changes (API tidak kompatibel)
MINOR   — Fitur baru, backward compatible
PATCH   — Bug fix, backward compatible
```

**Contoh `CHANGELOG.md`:**
```markdown
# Changelog

## [2.1.0] - 2025-01-15
### Added
- Fitur ekspor rapor ke PDF (`utils.export_pdf`)
- CLI flag `--format json|csv|pdf`

### Fixed
- Bug perhitungan rata-rata saat nilai negatif (issue #42)

### Changed
- `grade_dari_nilai` sekarang return `Literal["A","B","C","D","E"]` (type hint)

## [2.0.0] - 2024-11-01
### Breaking
- `Siswa.nilai` berganti dari `Dict[str, int]` ke `Dict[str, List[int]]` (support multiple scores per mapel)
- Minimal Python 3.10 (was 3.9)
```

---

## 9. GitHub Actions CI — Pipeline Minimal

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: Install deps
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements-dev.txt
          # requirements-dev.txt: pytest pytest-cov pytest-mock mypy ruff

      - name: Lint (ruff)
        run: ruff format --check . && ruff check .

      - name: Type check (mypy)
        run: mypy .

      - name: Test + Coverage
        run: pytest --cov=. --cov-fail-under=80 --cov-branch -q

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        if: always()
```

**`requirements-dev.txt`:**
```
pytest>=7.4
pytest-cov>=4.1
pytest-mock>=3.12
mypy>=1.8
ruff>=0.4
```

> ✅ **Gate CI:** Semua harus hijau → baru bisa merge ke `main`.

---

## 10. Pre-commit Hook — Cegah Commit Buruk Secara Lokal

```bash
pip install pre-commit
```

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.0
    hooks:
      - id: ruff
        args: [--fix, --exit-non-zero-on-fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest -q
        language: system
        types: [python]
        stages: [commit]
        pass_filenames: false
        always_run: true
```

**Install:**
```bash
pre-commit install
# sekarang tiap `git commit` auto jalan ruff + mypy + pytest
```

---

## 🧪 Latihan

1. **Setup Proyek Baru** — Buat folder `proyek-baru/` dengan `pyproject.toml`, `mypy.ini`, `requirements-dev.txt`. Install deps. Jalankan `ruff check .`, `mypy .`, `pytest` (kosong — OK).
2. **TDD Sederhana** — Tulis test dulu untuk fungsi `fibonacci(n)` (return n-th Fibonacci). Lalu implementasikan. Pastikan test pass.
3. **Coverage Gate** — Tambah fungsi tanpa test. Jalankan `pytest --cov-fail-under=80`. Lihat gagal. Tambah test → hijau.
4. **Type Error Hunt** — Buat file `buggy.py` dengan type error sengaja (mis. `def f(x: int) -> str: return x`). Jalankan `mypy buggy.py`. Perbaiki.
5. **Docstring Coverage** — Pasang `pydocstyle` atau `ruff` rule `D` (docstring). Pastikan semua public function punya docstring Google style.
6. **CI Simulation** — Push branch ke GitHub, buat PR. Periksa Actions tab — pastikan semua step hijau.
7. **Pre-commit Test** — Commit file yang sengaja bermasalah (mis. `import os, sys` di satu baris). Lihat `ruff` auto-fix. Coba commit yang gagal test — ditolak.

---

## ✅ Checklist Paham

- [ ] Bisa tulis test `pytest` dengan fixture, parametrize, mock
- [ ] Bisa baca & tafsirkan output `pytest --cov --cov-branch`
- [ ] `mypy strict` pass untuk kode baru (type hints lengkap)
- [ ] `ruff check --fix .` + `ruff format .` bersihkan kode otomatis
- [ ] Docstring Google style di semua public function/class
- [ ] SemVer & `CHANGELOG.md` update tiap rilis
- [ ] GitHub Actions CI: lint → type-check → test+coverage gate
- [ ] `pre-commit` terpasang & jalan di lokal sebelum push
- [ ] Paham beda line vs branch coverage
- [ ] Bisa jelaskan keuntungan TDD (test-first) vs test-after

**Kalau semua tercentang → lanjut ke Modul 18 (Jaringan & Model OSI).**