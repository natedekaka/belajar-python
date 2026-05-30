# Modul 13: Proyek Akhir — Aplikasi CLI Manajemen Nilai Sekolah

## 🏆 Tujuan

Mengaplikasikan **semua materi** yang sudah dipelajari (dari Modul 1 sampai Modul 12) dalam satu proyek nyata. Proyek ini bisa langsung kamu gunakan di sekolah.

---

## 📋 Spesifikasi Aplikasi

**Nama:** `sistem_nilai.py`  
**Tipe:** Command Line Interface (CLI)  
**Fitur:**
1. Manajemen data siswa (tambah, lihat, cari, hapus)
2. Input nilai per mata pelajaran
3. Hitung rata-rata dan grade otomatis
4. Cetak laporan rapor per siswa
5. Cetak statistik kelas
6. Simpan & baca data dari file CSV/JSON
7. Ranking siswa

---

## 📁 Struktur Proyek

```
proyek-akhir/
├── main.py                # Entry point — menu utama
├── models.py              # Class-class: Siswa, Kelas
├── utils.py               # Fungsi utilitas (hitungan, format)
├── data/                  # Folder penyimpanan data
│   ├── siswa.csv
│   └── kelas.json
└── README.md              # Dokumentasi
```

---

## 🧱 Langkah 1: Models (models.py)

Buat class-class yang merepresentasikan data.

### Class MataPelajaran

```python
# models.py

class MataPelajaran:
    """Mata pelajaran dengan nama dan nilai"""
    def __init__(self, nama: str, nilai: float = 0):
        self.nama = nama
        self.nilai = nilai
    
    def __str__(self):
        return f"{self.nama}: {self.nilai}"
    
    def lulus(self) -> bool:
        return self.nilai >= 75
```

### Class Siswa

```python
class Siswa:
    """Data lengkap seorang siswa"""
    def __init__(self, nis: str, nama: str, kelas: str):
        self.nis = nis
        self.nama = nama
        self.kelas = kelas
        self.mapel: dict[str, MataPelajaran] = {}  # {nama_mapel: objek}
    
    def tambah_nilai(self, nama_mapel: str, nilai: float):
        """Tambah atau update nilai mata pelajaran"""
        if nilai < 0 or nilai > 100:
            raise ValueError(f"Nilai {nilai} tidak valid (0-100)")
        self.mapel[nama_mapel] = MataPelajaran(nama_mapel, nilai)
    
    def get_nilai_list(self) -> list[float]:
        """Return list semua nilai"""
        return [m.nilai for m in self.mapel.values()]
    
    def rata_rata(self) -> float:
        """Hitung rata-rata nilai"""
        nilai_list = self.get_nilai_list()
        if not nilai_list:
            return 0.0
        return sum(nilai_list) / len(nilai_list)
    
    def grade(self) -> str:
        """Grade berdasarkan rata-rata"""
        rata = self.rata_rata()
        if rata >= 90:
            return "A"
        elif rata >= 80:
            return "B"
        elif rata >= 70:
            return "C"
        elif rata >= 60:
            return "D"
        else:
            return "E"
    
    def lulus(self) -> bool:
        """Lulus kalau rata-rata >= 75 dan tidak ada nilai < 60"""
        if self.rata_rata() < 75:
            return False
        for n in self.get_nilai_list():
            if n < 60:
                return False
        return True
    
    def to_dict(self) -> dict:
        """Konversi ke dictionary (untuk JSON)"""
        return {
            "nis": self.nis,
            "nama": self.nama,
            "kelas": self.kelas,
            "nilai": {nama: m.nilai for nama, m in self.mapel.items()}
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Buat object dari dictionary (dari JSON)"""
        s = cls(data["nis"], data["nama"], data["kelas"])
        for nama_mapel, nilai in data.get("nilai", {}).items():
            s.tambah_nilai(nama_mapel, nilai)
        return s
    
    def __str__(self):
        return f"{self.nis} | {self.nama:15} | {self.kelas:10} | Rata: {self.rata_rata():.1f} | Grade: {self.grade()}"
```

### Class Kelas

```python
class Kelas:
    """Kumpulan siswa dalam satu kelas"""
    def __init__(self, nama_kelas: str = ""):
        self.nama_kelas = nama_kelas
        self.daftar_siswa: dict[str, Siswa] = {}  # {nis: Siswa}
    
    def tambah_siswa(self, siswa: Siswa):
        if siswa.nis in self.daftar_siswa:
            raise ValueError(f"Siswa dengan NIS {siswa.nis} sudah ada!")
        self.daftar_siswa[siswa.nis] = siswa
    
    def cari_siswa(self, keyword: str) -> list[Siswa]:
        """Cari siswa berdasarkan nama atau NIS"""
        hasil = []
        for s in self.daftar_siswa.values():
            if keyword.lower() in s.nama.lower() or keyword == s.nis:
                hasil.append(s)
        return hasil
    
    def hapus_siswa(self, nis: str) -> bool:
        if nis in self.daftar_siswa:
            del self.daftar_siswa[nis]
            return True
        return False
    
    def ranking(self) -> list[Siswa]:
        """Urutkan siswa berdasarkan rata-rata (tertinggi ke terendah)"""
        return sorted(self.daftar_siswa.values(), 
                     key=lambda s: s.rata_rata(), 
                     reverse=True)
    
    def statistik(self) -> dict:
        """Statistik kelas"""
        if not self.daftar_siswa:
            return {}
        
        rata_list = [s.rata_rata() for s in self.daftar_siswa.values()]
        lulus = sum(1 for s in self.daftar_siswa.values() if s.lulus())
        
        return {
            "total_siswa": len(self.daftar_siswa),
            "rata_kelas": sum(rata_list) / len(rata_list),
            "tertinggi": max(rata_list),
            "terendah": min(rata_list),
            "lulus": lulus,
            "tidak_lulus": len(self.daftar_siswa) - lulus
        }
    
    def to_dict(self) -> dict:
        return {
            "nama_kelas": self.nama_kelas,
            "siswa": [s.to_dict() for s in self.daftar_siswa.values()]
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        k = cls(data["nama_kelas"])
        for s_data in data["siswa"]:
            k.tambah_siswa(Siswa.from_dict(s_data))
        return k
```

---

## ⚙️ Langkah 2: Utilitas (utils.py)

```python
# utils.py
import csv
import json
import os

# Warna ANSI untuk terminal (biar cantik)
class Warna:
    HIJAU = '\033[92m'
    KUNING = '\033[93m'
    MERAH = '\033[91m'
    BIRU = '\033[94m'
    UNGU = '\033[95m'
    BOLD = '\033[1m'
    END = '\033[0m'

def bersihkan_layar():
    """Bersihkan terminal"""
    os.system('clear' if os.name == 'posix' else 'cls')

def tampilkan_header(judul: str):
    """Tampilkan header dengan garis"""
    print(f"\n{Warna.BOLD}{Warna.BIRU}{'='*50}{Warna.END}")
    print(f"{Warna.BOLD}{judul.center(50)}{Warna.END}")
    print(f"{Warna.BOLD}{Warna.BIRU}{'='*50}{Warna.END}\n")

def tampilkan_menu(judul: str, opsi: list[str]) -> str:
    """Tampilkan menu dan minta input pilihan"""
    tampilkan_header(judul)
    for i, o in enumerate(opsi, 1):
        print(f"  {Warna.KUNING}{i}.{Warna.END} {o}")
    print(f"  {Warna.KUNING}0.{Warna.END} Kembali/Keluar")
    print()
    return input(f"{Warna.BOLD}Pilihan [0-{len(opsi)}]: {Warna.END}").strip()

def minta_angka(pesan: str, min_v=0, max_v=100) -> float:
    """Minta input angka dengan validasi"""
    while True:
        try:
            nilai = float(input(pesan))
            if min_v <= nilai <= max_v:
                return nilai
            print(f"{Warna.MERAH}Nilai harus antara {min_v}-{max_v}!{Warna.END}")
        except ValueError:
            print(f"{Warna.MERAH}Input harus angka!{Warna.END}")

def simpan_csv(siswa_list: list[Siswa], filename: str):
    """Simpan data siswa ke CSV"""
    # Kumpulkan semua mapel yang ada
    semua_mapel = set()
    for s in siswa_list:
        semua_mapel.update(s.mapel.keys())
    semua_mapel = sorted(semua_mapel)
    
    header = ["NIS", "Nama", "Kelas"] + semua_mapel + ["Rata-rata", "Grade"]
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for s in siswa_list:
            row = [s.nis, s.nama, s.kelas]
            for m in semua_mapel:
                if m in s.mapel:
                    row.append(s.mapel[m].nilai)
                else:
                    row.append("")
            row.append(f"{s.rata_rata():.1f}")
            row.append(s.grade())
            writer.writerow(row)
    
    print(f"{Warna.HIJAU}Data disimpan ke {filename}{Warna.END}")

def simpan_json(kelas: 'Kelas', filename: str):
    """Simpan data kelas ke JSON"""
    with open(filename, "w") as f:
        json.dump(kelas.to_dict(), f, indent=2)
    print(f"{Warna.HIJAU}Data disimpan ke {filename}{Warna.END}")

def baca_json(filename: str):
    """Baca data dari JSON"""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
```

---

## 🎮 Langkah 3: Main Program (main.py)

```python
#!/usr/bin/env python3
"""Sistem Manajemen Nilai Sekolah — CLI App"""

from models import Siswa, Kelas
from utils import *

def menu_utama(kelas: Kelas):
    """Menu utama aplikasi"""
    while True:
        pilihan = tampilkan_menu("🏫 SISTEM MANAJEMEN NILAI SEKOLAH", [
            "Manajemen Siswa",
            "Input Nilai",
            "Laporan & Ranking",
            "Statistik Kelas",
            "Simpan Data",
            "Muat Data"
        ])
        
        if pilihan == "0":
            print(f"\n{Warna.HIJAU}Terima kasih! Sampai jumpa. 👋{Warna.END}")
            break
        elif pilihan == "1":
            menu_siswa(kelas)
        elif pilihan == "2":
            menu_nilai(kelas)
        elif pilihan == "3":
            menu_laporan(kelas)
        elif pilihan == "4":
            tampilkan_statistik(kelas)
        elif pilihan == "5":
            menu_simpan(kelas)
        elif pilihan == "6":
            menu_muat(kelas)
        else:
            print(f"{Warna.MERAH}Pilihan tidak valid!{Warna.END}")

def menu_siswa(kelas: Kelas):
    """Menu manajemen siswa"""
    while True:
        pilihan = tampilkan_menu("👨‍🎓 MANAJEMEN SISWA", [
            "Tambah Siswa",
            "Lihat Semua Siswa",
            "Cari Siswa",
            "Hapus Siswa"
        ])
        
        if pilihan == "0":
            break
        elif pilihan == "1":
            tambah_siswa(kelas)
        elif pilihan == "2":
            lihat_semua_siswa(kelas)
        elif pilihan == "3":
            cari_siswa(kelas)
        elif pilihan == "4":
            hapus_siswa(kelas)

def tambah_siswa(kelas: Kelas):
    """Tambah siswa baru"""
    tampilkan_header("TAMBAH SISWA")
    
    nis = input("NIS: ").strip()
    if not nis:
        print(f"{Warna.MERAH}NIS tidak boleh kosong!{Warna.END}")
        return
    
    if nis in kelas.daftar_siswa:
        print(f"{Warna.MERAH}Siswa dengan NIS '{nis}' sudah ada!{Warna.END}")
        return
    
    nama = input("Nama lengkap: ").strip().title()
    if not nama:
        print(f"{Warna.MERAH}Nama tidak boleh kosong!{Warna.END}")
        return
    
    nama_kelas = input("Kelas: ").strip().upper()
    
    siswa = Siswa(nis, nama, nama_kelas)
    kelas.tambah_siswa(siswa)
    print(f"{Warna.HIJAU}Siswa '{nama}' berhasil ditambahkan! ✅{Warna.END}")

def lihat_semua_siswa(kelas: Kelas):
    """Tampilkan semua siswa"""
    tampilkan_header(f"DAFTAR SISWA ({len(kelas.daftar_siswa)})")
    
    if not kelas.daftar_siswa:
        print(f"{Warna.KUNING}Belum ada data siswa.{Warna.END}")
        return
    
    print(f"{Warna.BOLD}{'NIS':8} | {'Nama':20} | {'Kelas':12} | {'Rata-rata':9} | Grade{Warna.END}")
    print("-" * 65)
    
    for s in kelas.daftar_siswa.values():
        warna = Warna.HIJAU if s.lulus() else Warna.MERAH
        print(f"{warna}{s.nis:8} | {s.nama:20} | {s.kelas:12} | {s.rata_rata():>8.1f} | {s.grade()}{Warna.END}")
    
    input(f"\n{Warna.KUNING}Tekan ENTER untuk kembali...{Warna.END}")

def cari_siswa(kelas: Kelas):
    """Cari siswa berdasarkan NIS atau nama"""
    tampilkan_header("🔍 CARI SISWA")
    
    keyword = input("Masukkan NIS atau nama: ").strip()
    if not keyword:
        return
    
    hasil = kelas.cari_siswa(keyword)
    
    if not hasil:
        print(f"{Warna.MERAH}Siswa tidak ditemukan.{Warna.END}")
        return
    
    print(f"\nDitemukan {len(hasil)} siswa:")
    for s in hasil:
        print(f"\n  {Warna.BOLD}NIS:{Warna.END}   {s.nis}")
        print(f"  {Warna.BOLD}Nama:{Warna.END}  {s.nama}")
        print(f"  {Warna.BOLD}Kelas:{Warna.END} {s.kelas}")
        print(f"  {Warna.BOLD}Nilai:{Warna.END}")
        for m in s.mapel.values():
            status = "✅" if m.lulus() else "❌"
            print(f"    {m.nama:15}: {m.nilai:>5} {status}")
        print(f"  {Warna.BOLD}Rata:{Warna.END}   {s.rata_rata():.1f} | Grade: {s.grade()}")
    
    input(f"\n{Warna.KUNING}Tekan ENTER untuk kembali...{Warna.END}")

def hapus_siswa(kelas: Kelas):
    """Hapus siswa"""
    tampilkan_header("HAPUS SISWA")
    
    nis = input("Masukkan NIS siswa yang akan dihapus: ").strip()
    
    if kelas.hapus_siswa(nis):
        print(f"{Warna.HIJAU}Siswa dengan NIS '{nis}' berhasil dihapus.{Warna.END}")
    else:
        print(f"{Warna.MERAH}Siswa dengan NIS '{nis}' tidak ditemukan.{Warna.END}")

def menu_nilai(kelas: Kelas):
    """Menu input nilai"""
    tampilkan_header("📝 INPUT NILAI")
    
    if not kelas.daftar_siswa:
        print(f"{Warna.KUNING}Belum ada data siswa. Tambah siswa dulu!{Warna.END}")
        return
    
    nis = input("NIS siswa: ").strip()
    if nis not in kelas.daftar_siswa:
        print(f"{Warna.MERAH}Siswa dengan NIS '{nis}' tidak ditemukan.{Warna.END}")
        return
    
    siswa = kelas.daftar_siswa[nis]
    print(f"\nInput nilai untuk: {Warna.BOLD}{siswa.nama}{Warna.END}")
    
    while True:
        print(f"\nNilai saat ini:")
        for m in siswa.mapel.values():
            print(f"  {m.nama}: {m.nilai}")
        
        nama_mapel = input(f"\nNama mata pelajaran (atau kosongkan untuk selesai): ").strip().title()
        if not nama_mapel:
            break
        
        try:
            nilai = minta_angka(f"Nilai {nama_mapel} (0-100): ")
            siswa.tambah_nilai(nama_mapel, nilai)
            print(f"{Warna.HIJAU}Nilai {nama_mapel} = {nilai} tersimpan!{Warna.END}")
        except ValueError as e:
            print(f"{Warna.MERAH}Error: {e}{Warna.END}")

def menu_laporan(kelas: Kelas):
    """Tampilkan laporan dan ranking"""
    pilihan = tampilkan_menu("📊 LAPORAN & RANKING", [
        "Rapor Individual",
        "Ranking Kelas",
        "Cetak Semua Rapor",
        "Export ke CSV"
    ])
    
    if pilihan == "0":
        return
    elif pilihan == "1":
        tampilkan_rapor(kelas)
    elif pilihan == "2":
        tampilkan_ranking(kelas)
    elif pilihan == "3":
        cetak_semua_rapor(kelas)
    elif pilihan == "4":
        simpan_csv(list(kelas.daftar_siswa.values()), "data/laporan_nilai.csv")

def tampilkan_rapor(kelas: Kelas):
    """Tampilkan rapor seorang siswa"""
    tampilkan_header("📄 RAPOR SISWA")
    
    nis = input("NIS siswa: ").strip()
    if nis not in kelas.daftar_siswa:
        print(f"{Warna.MERAH}Siswa tidak ditemukan.{Warna.END}")
        return
    
    s = kelas.daftar_siswa[nis]
    
    print(f"\n{Warna.BOLD}{'='*50}{Warna.END}")
    print(f"{Warna.BOLD}           RAPOR SISWA{Warna.END}")
    print(f"{Warna.BOLD}{'='*50}{Warna.END}")
    print(f"  NIS          : {s.nis}")
    print(f"  Nama         : {s.nama}")
    print(f"  Kelas        : {s.kelas}")
    print(f"  {'-'*40}")
    print(f"  {'Mata Pelajaran':20} {'Nilai':>8} {'Status':>10}")
    print(f"  {'-'*40}")
    
    for m in s.mapel.values():
        status = "✅ Lulus" if m.lulus() else "❌ Tidak"
        print(f"  {m.nama:20} {m.nilai:>8.1f} {status:>10}")
    
    print(f"  {'-'*40}")
    print(f"  {'Rata-rata':20} {s.rata_rata():>8.1f} {'Grade ' + s.grade():>10}")
    status_lulus = f"{Warna.HIJAU}✅ LULUS{Warna.END}" if s.lulus() else f"{Warna.MERAH}❌ TIDAK LULUS{Warna.END}"
    print(f"  {'Status':20} {status_lulus}")
    print(f"{Warna.BOLD}{'='*50}{Warna.END}\n")
    
    input(f"{Warna.KUNING}Tekan ENTER untuk kembali...{Warna.END}")

def tampilkan_ranking(kelas: Kelas):
    """Tampilkan ranking berdasarkan rata-rata"""
    tampilkan_header("🏆 RANKING SISWA")
    
    if not kelas.daftar_siswa:
        print(f"{Warna.KUNING}Belum ada data siswa.{Warna.END}")
        return
    
    ranking = kelas.ranking()
    
    print(f"{Warna.BOLD}{'Rank':5} | {'NIS':8} | {'Nama':20} | {'Kelas':10} | {'Rata':7} | Grade | Status{Warna.END}")
    print("-" * 75)
    
    medali = ["🥇", "🥈", "🥉"]
    for i, s in enumerate(ranking, 1):
        rank_str = f"{medali[i-1]}" if i <= 3 else f"{i:>4}."
        status = "✅" if s.lulus() else "❌"
        print(f"{rank_str} | {s.nis:8} | {s.nama:20} | {s.kelas:10} | {s.rata_rata():>6.1f} |  {s.grade()}   |  {status}")
    
    input(f"\n{Warna.KUNING}Tekan ENTER untuk kembali...{Warna.END}")

def cetak_semua_rapor(kelas: Kelas):
    """Cetak rapor semua siswa"""
    for s in kelas.daftar_siswa.values():
        print(f"\n{Warna.BOLD}{'='*50}{Warna.END}")
        print(f"  NIS: {s.nis}  |  {s.nama:20}  |  {s.kelas}")
        print(f"  {'-'*40}")
        for m in s.mapel.values():
            print(f"  {m.nama:20}: {m.nilai}")
        print(f"  {'-'*40}")
        print(f"  Rata-rata: {s.rata_rata():.1f}  |  Grade: {s.grade()}  |  {'LULUS' if s.lulus() else 'TIDAK LULUS'}")

def tampilkan_statistik(kelas: Kelas):
    """Tampilkan statistik kelas"""
    tampilkan_header("📈 STATISTIK KELAS")
    
    if not kelas.daftar_siswa:
        print(f"{Warna.KUNING}Belum ada data siswa.{Warna.END}")
        return
    
    stat = kelas.statistik()
    
    print(f"  {Warna.BOLD}Total Siswa:{Warna.END}     {stat['total_siswa']}")
    print(f"  {Warna.BOLD}Rata-rata Kelas:{Warna.END} {stat['rata_kelas']:.1f}")
    print(f"  {Warna.BOLD}Nilai Tertinggi:{Warna.END} {stat['tertinggi']:.1f}")
    print(f"  {Warna.BOLD}Nilai Terendah:{Warna.END}  {stat['terendah']:.1f}")
    print(f"  {Warna.BOLD}Lulus:{Warna.END}            {Warna.HIJAU}{stat['lulus']}{Warna.END}")
    print(f"  {Warna.BOLD}Tidak Lulus:{Warna.END}      {Warna.MERAH}{stat['tidak_lulus']}{Warna.END}")
    
    # Distribusi grade
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for s in kelas.daftar_siswa.values():
        grade_count[s.grade()] += 1
    print(f"\n  {Warna.BOLD}Distribusi Grade:{Warna.END}")
    for g, c in grade_count.items():
        if c > 0:
            print(f"    Grade {g}: {c} siswa {'█' * c}")
    
    input(f"\n{Warna.KUNING}Tekan ENTER untuk kembali...{Warna.END}")

def menu_simpan(kelas: Kelas):
    """Menu simpan data"""
    pilihan = tampilkan_menu("💾 SIMPAN DATA", [
        "Simpan ke CSV",
        "Simpan ke JSON"
    ])
    
    if pilihan == "0":
        return
    elif pilihan == "1":
        simpan_csv(list(kelas.daftar_siswa.values()), "data/laporan_nilai.csv")
    elif pilihan == "2":
        simpan_json(kelas, "data/kelas.json")

def menu_muat(kelas: Kelas):
    """Menu muat data"""
    global kelas_global
    tampilkan_header("📂 MUAT DATA")
    
    filename = "data/kelas.json"
    data = baca_json(filename)
    
    if data is None:
        print(f"{Warna.MERAH}File '{filename}' tidak ditemukan.{Warna.END}")
        return
    
    kelas_global = Kelas.from_dict(data)
    print(f"{Warna.HIJAU}Data berhasil dimuat! {len(kelas_global.daftar_siswa)} siswa.{Warna.END}")

# === MAIN ===
if __name__ == "__main__":
    # Inisialisasi folder data
    os.makedirs("data", exist_ok=True)
    
    # Coba muat data otomatis
    kelas_global = Kelas("XII IPA 1")
    data = baca_json("data/kelas.json")
    if data:
        kelas_global = Kelas.from_dict(data)
        print(f"{Warna.HIJAU}Data otomatis dimuat: {len(kelas_global.daftar_siswa)} siswa.{Warna.END}")
    else:
        print(f"{Warna.KUNING}Data baru akan dibuat.{Warna.END}")
    
    # Tambah data contoh
    if not kelas_global.daftar_siswa:
        s1 = Siswa("1001", "Budi Santoso", "XII IPA 1")
        s1.tambah_nilai("Matematika", 85)
        s1.tambah_nilai("IPA", 90)
        s1.tambah_nilai("Bahasa Inggris", 78)
        s1.tambah_nilai("PPKn", 80)
        kelas_global.tambah_siswa(s1)
        
        s2 = Siswa("1002", "Ani Wijaya", "XII IPA 1")
        s2.tambah_nilai("Matematika", 92)
        s2.tambah_nilai("IPA", 88)
        s2.tambah_nilai("Bahasa Inggris", 95)
        s2.tambah_nilai("PPKn", 85)
        kelas_global.tambah_siswa(s2)
        
        s3 = Siswa("1003", "Citra Dewi", "XII IPA 1")
        s3.tambah_nilai("Matematika", 76)
        s3.tambah_nilai("IPA", 80)
        s3.tambah_nilai("Bahasa Inggris", 82)
        s3.tambah_nilai("PPKn", 78)
        kelas_global.tambah_siswa(s3)
        
        print(f"{Warna.KUNING}Data contoh ditambahkan.{Warna.END}")
    
    try:
        menu_utama(kelas_global)
    except KeyboardInterrupt:
        print(f"\n\n{Warna.KUNING}Program dihentikan. Data terakhir disimpan.{Warna.END}")
        simpan_json(kelas_global, "data/kelas.json")
```

---

## 🚀 Cara Menjalankan

```bash
# Masuk ke folder proyek
cd ~/belajar-python
mkdir -p proyek-akhir
cd proyek-akhir

# Install semua file
# (copy kode di atas ke file masing-masing)

# Jalankan
python main.py
```

---

## 🧪 Latihan Pengembangan Lanjutan

Setelah proyek dasar selesai, coba kembangkan sendiri:

1. **Filter per kelas** — dukungan multiple kelas (X IPA 1, X IPA 2, dll)
2. **Export PDF** — gunakan library `reportlab` atau `fpdf`
3. **Grafik** — pakai `matplotlib` untuk visualisasi distribusi nilai
4. **Database** — ganti penyimpanan JSON ke SQLite (`import sqlite3`)
5. **Web App** — ubah jadi web app dengan `Flask`
6. **Autentikasi** — login guru dengan password

---

## 🎯 Checklist Proyek Selesai

- [ ] Semua modul Python (Models, Utils, Main) berfungsi
- [ ] Bisa tambah, lihat, cari, hapus siswa
- [ ] Bisa input nilai per mata pelajaran
- [ ] Rata-rata dan grade otomatis terhitung
- [ ] Ranking siswa berdasarkan rata-rata
- [ ] Statistik kelas lengkap
- [ ] Data bisa disimpan dan dimuat kembali (CSV & JSON)
- [ ] Program tidak crash di situasi tak terduga (try/except)
- [ ] Tampilan rapi di terminal

---

## 🏁 SELAMAT! Kamu sudah menyelesaikan seluruh materi!

Dari **Modul 0 sampai Modul 13**, sekarang kamu sudah:
- ✅ Mengerti Python dari nol
- ✅ Bisa membuat aplikasi CLI sendiri
- ✅ Memiliki bahan ajar lengkap buat ngajar
- ✅ Tau cara mengelola data siswa secara digital

**Langkah selanjutnya:** Mulai ngajar! Materi ini bisa kamu pakai langsung untuk mengajar siswa.

Kalau ada bagian yang kurang jelas atau mau dikembangkan, tinggal bilang saja.
