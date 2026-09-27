# Modul 16: Basis Data — SQL & SQLite

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Algoritma & Pemrograman | AP | Mengembangkan program modular besar, library pengolahan data bervolume besar |
| Analisis Data | AD | (Muatan AD diserap ke AP) — menginput, memproses, memvisualisasi data, query, indexing |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjelaskan **model relasional**: tabel, baris, kolom, primary key, foreign key
- Mendesain **ER Diagram** (Entitas-Relasi) & menerjemahkannya ke skema SQL
- Menulis **DDL** (`CREATE TABLE`, `ALTER`, `DROP`, `INDEX`) & **DML** (`INSERT`, `SELECT`, `UPDATE`, `DELETE`)
- Memahami **normalisasi** (1NF, 2NF, 3NF) & *denormalisasi* untuk performa
- Pakai **SQLite** via `sqlite3` modul bawaan Python — *zero-config*, file-based
- Mengamankan query dengan **parameterized query** (hindari SQL Injection)
- Menggunakan **transaksi** (`BEGIN`, `COMMIT`, `ROLLBACK`) untuk konsistensi
- Memahami **indexing** (B-Tree) & kapan *index* membantu / merugikan
- Memvisualisasikan hasil query ke Python (`pandas` opsional, atau manual)

---

## 1. Kenapa Basis Data Relasional?

| Masalah File CSV / JSON | Solusi Relasional (SQL) |
|-------------------------|--------------------------|
| Cari data = baca seluruh file O(n) | **Index** → O(log n) |
| Duplikasi data → inkonsisten | **Normalisasi** + **FK constraint** |
| Multi-user baca/tulis bersamaan → korup | **Transaksi ACID** |
| Relasi antar entitas manual | **JOIN** deklaratif |
| Schema tidak tertulis | **DDL** = kontrak eksplisit |

> 💡 **SQLite** = serverless, file tunggal, ACID compliant, cocok untuk embedded / desktop / prototipe. Produksi skala besar → PostgreSQL / MySQL.

---

## 2. Desain ER → Skema (Contoh: Sistem Nilai)

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   Siswa     │       │   Kelas     │       │  MataPelajaran
├─────────────┤       ├─────────────┤       ├─────────────┤
│ PK nis      │       │ PK id_kelas │       │ PK id_mapel │
│ nama        │       │ nama_kelas  │       │ nama_mapel  │
│ fk id_kelas │◄──────│ wali_kelas  │       │ sks         │
└─────────────┘       └─────────────┘       └─────────────┘
                           ▲
                           │
                    ┌──────┴──────┐
                    │   Nilai     │
                    ├─────────────┤
                    │ PK id_nilai │
                    │ FK nis      │
                    │ FK id_mapel │
                    │ nilai       │
                    │ semester    │
                    └─────────────┘
```

**Aturan ER → Tabel:**
- Entitas → Tabel
- Atribut → Kolom
- Primary Key → `PRIMARY KEY`
- Relasi 1:N → *Foreign Key* di sisi "many"
- Relasi M:N → **Tabel junction** (2 FK + PK komposit)

---

## 3. DDL — Buat Skema di SQLite

```python
import sqlite3
from contextlib import closing

DB_PATH = "sekolah.db"

def init_db():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("PRAGMA foreign_keys = ON")  # wajib untuk FK enforce
        cur = conn.cursor()

        # Siswa
        cur.execute("""
            CREATE TABLE IF NOT EXISTS siswa (
                nis       TEXT PRIMARY KEY,
                nama      TEXT NOT NULL,
                id_kelas  TEXT NOT NULL,
                FOREIGN KEY (id_kelas) REFERENCES kelas(id_kelas) ON DELETE RESTRICT
            )
        """)

        # Kelas
        cur.execute("""
            CREATE TABLE IF NOT EXISTS kelas (
                id_kelas   TEXT PRIMARY KEY,
                nama_kelas TEXT NOT NULL,
                wali_kelas TEXT
            )
        """)

        # Mata Pelajaran
        cur.execute("""
            CREATE TABLE IF NOT EXISTS mata_pelajaran (
                id_mapel  TEXT PRIMARY KEY,
                nama_mapel TEXT NOT NULL,
                sks       INTEGER DEFAULT 2
            )
        """)

        # Nilai (junction + atribut)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS nilai (
                id_nilai   INTEGER PRIMARY KEY AUTOINCREMENT,
                nis        TEXT NOT NULL,
                id_mapel   TEXT NOT NULL,
                nilai      REAL CHECK (nilai >= 0 AND nilai <= 100),
                semester   TEXT NOT NULL,  -- "2024/2025-1"
                FOREIGN KEY (nis)      REFERENCES siswa(nis) ON DELETE CASCADE,
                FOREIGN KEY (id_mapel) REFERENCES mata_pelajaran(id_mapel) ON DELETE CASCADE,
                UNIQUE (nis, id_mapel, semester)  -- satu nilai per mapel per semester
            )
        """)

        # Index untuk query cepat
        cur.execute("CREATE INDEX IF NOT EXISTS idx_nilai_nis ON nilai(nis)")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_nilai_mapel ON nilai(id_mapel)")

        conn.commit()
        print("✅ Skema siap")

if __name__ == "__main__":
    init_db()
```

> ⚠️ **`PRAGMA foreign_keys = ON`** wajib di SQLite — default OFF!

---

## 4. DML — Insert, Select, Update, Delete (Parameterized!)

```python
def tambah_siswa(nis, nama, id_kelas):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute(
            "INSERT INTO siswa (nis, nama, id_kelas) VALUES (?, ?, ?)",
            (nis, nama, id_kelas)
        )
        conn.commit()

def cari_siswa(nis):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row  # akses by nama kolom
        cur = conn.execute("SELECT * FROM siswa WHERE nis = ?", (nis,))
        return cur.fetchone()  # Row object → dict-like

def update_nama_siswa(nis, nama_baru):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cur = conn.execute(
            "UPDATE siswa SET nama = ? WHERE nis = ?",
            (nama_baru, nis)
        )
        conn.commit()
        return cur.rowcount  # 0 jika tidak ditemukan

def hapus_siswa(nis):
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        cur = conn.execute("DELETE FROM siswa WHERE nis = ?", (nis,))
        conn.commit()
        return cur.rowcount
```

> 🔒 **SELALU pakai `?` placeholder** — **JANGAN** f-string / `%` formatting. Itu **SQL Injection**.

---

## 5. Query Kompleks — JOIN, Agregat, Subquery

```python
def rapor_siswa(nis, semester):
    """Return list of dict: mapel, nilai, grade."""
    sql = """
        SELECT mp.nama_mapel, n.nilai,
               CASE
                   WHEN n.nilai >= 90 THEN 'A'
                   WHEN n.nilai >= 80 THEN 'B'
                   WHEN n.nilai >= 70 THEN 'C'
                   WHEN n.nilai >= 60 THEN 'D'
                   ELSE 'E'
               END AS grade
        FROM nilai n
        JOIN mata_pelajaran mp ON n.id_mapel = mp.id_mapel
        WHERE n.nis = ? AND n.semester = ?
        ORDER BY mp.nama_mapel
    """
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(sql, (nis, semester))
        return [dict(row) for row in cur.fetchall()]

def statistik_kelas(id_kelas, semester):
    """Rata-rata per mapel untuk satu kelas."""
    sql = """
        SELECT mp.nama_mapel,
               AVG(n.nilai) AS rata2,
               MIN(n.nilai) AS min_nilai,
               MAX(n.nilai) AS max_nilai,
               COUNT(*)     AS jumlah_siswa
        FROM nilai n
        JOIN siswa s ON n.nis = s.nis
        JOIN mata_pelajaran mp ON n.id_mapel = mp.id_mapel
        WHERE s.id_kelas = ? AND n.semester = ?
        GROUP BY mp.id_mapel, mp.nama_mapel
        ORDER BY rata2 DESC
    """
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(sql, (id_kelas, semester))
        return [dict(row) for row in cur.fetchall()]

# Subquery: siswa yang nilai di BAWAH rata-rata kelas per mapel
def siswa_perlu_bimbingan(semester):
    sql = """
        SELECT s.nis, s.nama, mp.nama_mapel, n.nilai, k.nama_kelas
        FROM nilai n
        JOIN siswa s ON n.nis = s.nis
        JOIN kelas k ON s.id_kelas = k.id_kelas
        JOIN mata_pelajaran mp ON n.id_mapel = mp.id_mapel
        WHERE n.semester = ?
          AND n.nilai < (
              SELECT AVG(n2.nilai)
              FROM nilai n2
              JOIN siswa s2 ON n2.nis = s2.nis
              WHERE n2.id_mapel = n.id_mapel
                AND n2.semester = n.semester
                AND s2.id_kelas = s.id_kelas
          )
        ORDER BY k.nama_kelas, mp.nama_mapel, n.nilai
    """
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(sql, (semester,))
        return [dict(row) for row in cur.fetchall()]
```

---

## 6. Transaksi — ACID di SQLite

```python
def pindah_kelas_siswa(nis, id_kelas_baru):
    """Atomic: update siswa + log ke tabel audit (contoh)."""
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        try:
            conn.execute("BEGIN")
            # 1. Update siswa
            conn.execute(
                "UPDATE siswa SET id_kelas = ? WHERE nis = ?",
                (id_kelas_baru, nis)
            )
            # 2. Insert log (asumsi tabel audit ada)
            conn.execute(
                "INSERT INTO audit_log (nis, aksi, detail, waktu) VALUES (?, ?, ?, datetime('now'))",
                (nis, "PINDAH_KELAS", id_kelas_baru)
            )
            conn.execute("COMMIT")
            return True
        except sqlite3.Error as e:
            conn.execute("ROLLBACK")
            print(f"❌ Transaksi gagal: {e}")
            return False
```

> 💡 **`BEGIN` → `COMMIT` / `ROLLBACK`** = satu unit kerja. Gagal di tengah → **semua dibatalkan**.

---

## 7. Indexing — Kapan Membantu, Kapan Merugikan

| Situasi | Index Membantu? | Alasan |
|---------|-----------------|--------|
| `WHERE kolom = ?` / `kolom IN (...)` | ✅ Ya | B-Tree seek O(log n) |
| `WHERE kolom > ?` / `BETWEEN` | ✅ Ya | Range scan |
| `ORDER BY kolom` | ✅ Ya | Hindari sort |
| `JOIN ON a.kolom = b.kolom` | ✅ Ya | Hash join / merge join cepat |
| `WHERE kolom LIKE '%abc'` | ❌ Tidak | Leading wildcard → full scan |
| `WHERE UPPER(kolom) = 'X'` | ❌ Tidak | Fungsi di kolom → index tidak dipakai (pakai *expression index* / `COLLATE NOCASE`) |
| Tabel kecil (< 1000 baris) | ⚠️ Mungkin tidak | Overhead index > full scan |
| Kolom *low cardinality* (boolean, gender) | ❌ Tidak | Selektivitas rendah → planner abaikan |

```python
# Cek query plan
with closing(sqlite3.connect(DB_PATH)) as conn:
    cur = conn.execute("EXPLAIN QUERY PLAN SELECT * FROM nilai WHERE nis = '123'")
    for row in cur:
        print(row)
# Output contoh: (0, 0, 0, 'SEARCH TABLE nilai USING INDEX idx_nilai_nis (nis=?)')
```

---

## 8. Migrasi Skema — `ALTER TABLE` & Versioning

```python
def migrasi_tambah_kolom_email():
    with closing(sqlite3.connect(DB_PATH)) as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        # SQLite ALTER TABLE terbatas: ADD COLUMN, RENAME, DROP COLUMN (3.35+)
        conn.execute("ALTER TABLE siswa ADD COLUMN email TEXT")
        conn.commit()

# Untuk migrasi kompleks (ubah tipe, rename kolom, dll):
# 1. Buat tabel baru dengan skema final
# 2. COPY data dari lama → baru (transformasi jika perlu)
# 3. DROP tabel lama, RENAME tabel baru
# 4. Recreate index & trigger
```

> 💡 Produksi: pakai **Alembic** / **sqlalchemy-migrate** untuk versioning otomatis.

---

## 9. Integrasi ke Proyek Modul 13 (Upgrade)

```python
# models.py — ganti CSV/JSON ke SQLite
import sqlite3
from dataclasses import dataclass
from contextlib import closing

@dataclass
class Siswa:
    nis: str
    nama: str
    id_kelas: str
    # nilai di-load lazy via Kelas / repository

class KelasRepository:
    def __init__(self, db_path="sekolah.db"):
        self.db_path = db_path

    def _conn(self):
        c = sqlite3.connect(self.db_path)
        c.execute("PRAGMA foreign_keys = ON")
        c.row_factory = sqlite3.Row
        return c

    def semua_siswa(self, id_kelas):
        with closing(self._conn()) as conn:
            cur = conn.execute(
                "SELECT nis, nama, id_kelas FROM siswa WHERE id_kelas = ? ORDER BY nama",
                (id_kelas,)
            )
            return [Siswa(**row) for row in cur.fetchall()]

    def tambah_nilai(self, nis, id_mapel, nilai, semester):
        with closing(self._conn()) as conn:
            conn.execute("""
                INSERT INTO nilai (nis, id_mapel, nilai, semester)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(nis, id_mapel, semester) DO UPDATE SET nilai = excluded.nilai
            """, (nis, id_mapel, nilai, semester))
            conn.commit()
```

> 💡 `ON CONFLICT ... DO UPDATE` = **upsert** (insert atau update). SQLite 3.24+.

---

## 🧪 Latihan

1. **Desain ER** — Buat ER diagram untuk "Perpustakaan": Buku, Anggota, Peminjaman, Kategori. Tulis DDL-nya.
2. **CRUD Lengkap** — Implementasikan `BukuRepository` dengan `tambah`, `cari_by_isbn`, `update_stok`, `hapus`, `cari_by_judul` (LIKE).
3. **Transaksi Peminjaman** — `pinjam_buku(anggota_id, isbn)`: cek stok > 0, kurangi stok, insert ke `peminjaman` — semua dalam 1 transaksi.
4. **Laporan Terlambat** — Query: daftar peminjaman yang `tanggal_kembali < today` AND `status != 'dikembalikan'`. Tampilkan nama anggota, judul buku, hari terlambat.
5. **Index vs No Index** — Buat tabel 100k baris. Query `WHERE nama = 'X'` sebelum & sesudah `CREATE INDEX`. Ukur `timeit`.
6. **SQL Injection Demo** — Coba `cari_siswa("' OR '1'='1")` dengan kode **tanpa** parameterized query (pakai f-string). Lihat apa yang terjadi. Lalu perbaiki.
7. **Normalisasi Praktik** — Diberi tabel `penjualan(no_nota, tgl, id_pelanggan, nama_pelanggan, id_barang, nama_barang, harga, qty)`. Normalisasi ke 3NF. Tulis DDL hasilnya.

---

## ✅ Checklist Paham

- [ ] Bisa gambar ER diagram & turunkan ke DDL `CREATE TABLE` + FK + INDEX
- [ ] Selalu pakai **parameterized query** (`?`) — tidak pernah f-string di SQL
- [ ] `PRAGMA foreign_keys = ON` di setiap koneksi
- [ ] Transaksi: `BEGIN` → operasi → `COMMIT` / `ROLLBACK` pada `except`
- [ ] `JOIN` (INNER, LEFT), `GROUP BY` + agregat (`AVG`, `COUNT`, `SUM`)
- [ ] Subquery di `WHERE` & `SELECT` untuk perbandingan ke rata-rata
- [ ] `EXPLAIN QUERY PLAN` baca & tafsirkan output
- [ ] Tahu kapan index membantu vs merugikan
- [ ] `ON CONFLICT ... DO UPDATE` untuk upsert
- [ ] Rencana migrasi skema tanpa kehilangan data

**Kalau semua tercentang → lanjut ke Modul 17 (Testing, Dokumentasi & Kualitas Kode).**