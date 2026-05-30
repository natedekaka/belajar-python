#!/usr/bin/env python3
"""
📋 Absensi Siswa — Generate & Cetak Daftar Hadir dari Daftar Siswa

Cara pakai:
    python absensi.py                   # Generate absensi dari 'daftar_siswa.csv'
    python absensi.py data_siswa.csv    # Generate dari file tertentu

Format daftar_siswa.csv:
    NIS,Nama,Kelas
    1001,Budi Santoso,X IPA 1
    1002,Ani Wijaya,X IPA 1
"""

import csv
import sys
from pathlib import Path
from datetime import datetime, timedelta
import calendar

BULAN_INDONESIA = [
    "", "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

HARI_INDONESIA = [
    "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"
]

def baca_daftar_siswa(filename="daftar_siswa.csv"):
    """Baca daftar siswa dari CSV"""
    if not Path(filename).exists():
        print(f"❌ File '{filename}' tidak ditemukan!")
        print(f"\nBuat file '{filename}' dengan format:")
        print("  NIS,Nama,Kelas")
        print("  1001,Budi Santoso,X IPA 1")
        print("  1002,Ani Wijaya,X IPA 1")
        print("\nAtau generate file contoh:")
        print(f"  python {Path(__file__).name} --create-template")
        return []

    siswa = []
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            siswa.append({
                "nis": row.get("NIS", "").strip(),
                "nama": row.get("Nama", "").strip(),
                "kelas": row.get("Kelas", "").strip()
            })
    return siswa

def buat_template():
    """Buat file contoh daftar_siswa.csv"""
    contoh = "NIS,Nama,Kelas\n"
    contoh += "1001,Budi Santoso,X IPA 1\n"
    contoh += "1002,Ani Wijaya,X IPA 1\n"
    contoh += "1003,Citra Dewi,X IPA 1\n"
    contoh += "1004,Dedi Permana,X IPA 1\n"
    contoh += "1005,Eva Kurniawan,X IPA 1\n"

    with open("daftar_siswa.csv", "w") as f:
        f.write(contoh)
    print("✅ File 'daftar_siswa.csv' telah dibuat.")
    print("   Edit file tersebut dengan data siswa kamu.")

def generate_absensi_harian(siswa, tanggal=None):
    """Generate absensi untuk satu hari"""
    if tanggal is None:
        tanggal = datetime.now()

    hari_inggris = tanggal.strftime("%A")
    hari = hari_inggris
    for en, id_ in zip(
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        HARI_INDONESIA
    ):
        hari = hari.replace(en, id_)

    tanggal_str = f"{hari}, {tanggal.day} {BULAN_INDONESIA[tanggal.month]} {tanggal.year}"
    
    kelompok = {}
    for s in siswa:
        k = s["kelas"]
        if k not in kelompok:
            kelompok[k] = []
        kelompok[k].append(s)

    output = f"absensi_{tanggal.strftime('%Y%m%d')}.txt"
    with open(output, "w", encoding="utf-8") as f:
        f.write("=" * 60 + "\n")
        f.write(f"{'ABSENSI SISWA':^60}\n")
        f.write(f"{tanggal_str:^60}\n")
        f.write("=" * 60 + "\n\n")

        for kelas, siswa_kelas in sorted(kelompok.items()):
            f.write(f"Kelas: {kelas}\n")
            f.write("-" * 60 + "\n")
            f.write(f"{'No':4} {'NIS':8} {'Nama':25} {'Hadir':10}\n")
            f.write("-" * 60 + "\n")

            for i, s in enumerate(sorted(siswa_kelas, key=lambda x: x["nama"]), 1):
                f.write(f"{i:4} {s['nis']:8} {s['nama']:25} {'_____':10}\n")

            f.write("-" * 60 + "\n")
            f.write(f"{'Jumlah Siswa':20}: {len(siswa_kelas)}\n")
            f.write(f"{'Hadir':20}: _____\n")
            f.write(f"{'Sakit':20}: _____\n")
            f.write(f"{'Izin':20}: _____\n")
            f.write(f"{'Tanpa Keterangan':20}: _____\n\n")

    print(f"✅ Absensi harian → '{output}'")

def generate_absensi_bulanan(siswa, tahun=None, bulan=None):
    """Generate absensi untuk satu bulan penuh"""
    now = datetime.now()
    tahun = tahun or now.year
    bulan = bulan or now.month

    hari_dalam_bulan = calendar.monthrange(tahun, bulan)[1]
    tanggal_awal = datetime(tahun, bulan, 1)
    nama_bulan = BULAN_INDONESIA[bulan]

    kelompok = {}
    for s in siswa:
        k = s["kelas"]
        if k not in kelompok:
            kelompok[k] = []
        kelompok[k].append(s)

    for kelas, siswa_kelas in sorted(kelompok.items()):
        output = f"absensi_{kelas.replace(' ', '_')}_{tahun}_{bulan:02d}.txt"
        with open(output, "w", encoding="utf-8") as f:
            f.write("=" * 80 + "\n")
            f.write(f"{'DAFTAR HADIR SISWA':^80}\n")
            f.write(f"{f'Bulan {nama_bulan} {tahun}':^80}\n")
            f.write(f"{f'Kelas: {kelas}':^80}\n")
            f.write("=" * 80 + "\n\n")

            header = f"{'No':4} {'NIS':8} {'Nama':22}"
            for tgl in range(1, hari_dalam_bulan + 1):
                tgl_date = datetime(tahun, bulan, tgl)
                if tgl_date.weekday() < 5:
                    header += f"{tgl:3d}"
            header += f" {'Hadir':6} {'%':5}"
            f.write(header + "\n")
            f.write("-" * 80 + "\n")

            hari_sekolah = sum(1 for d in range(1, hari_dalam_bulan + 1)
                               if datetime(tahun, bulan, d).weekday() < 5)

            for i, s in enumerate(sorted(siswa_kelas, key=lambda x: x["nama"]), 1):
                row = f"{i:4} {s['nis']:8} {s['nama']:22}"
                row += f"{'___' * hari_sekolah:^{hari_sekolah * 3}}"
                row += f" {'_____':6} {'___':5}"
                f.write(row + "\n")

            f.write("\n" + "=" * 80 + "\n")
            f.write(f"{'Keterangan':20}: Isi tanda centang (✓) atau ketidakhadiran (S/I/A)\n")
            f.write(f"{'S':20}: Sakit\n")
            f.write(f"{'I':20}: Izin\n")
            f.write(f"{'A':20}: Tanpa Keterangan\n")

        print(f"✅ Absensi bulanan → '{output}'")

if __name__ == "__main__":
    print("📋 ABSENSI SISWA\n")

    if len(sys.argv) > 1:
        if sys.argv[1] == "--create-template":
            buat_template()
            sys.exit(0)
        else:
            filename = sys.argv[1]
    else:
        filename = "daftar_siswa.csv"

    siswa = baca_daftar_siswa(filename)
    if not siswa:
        sys.exit(1)

    print(f"📊 Total siswa: {len(siswa)}")
    for kelas in sorted(set(s["kelas"] for s in siswa)):
        count = sum(1 for s in siswa if s["kelas"] == kelas)
        print(f"   • {kelas}: {count} siswa")

    print(f"\nPilih jenis absensi:")
    print(f"  1. Harian (hari ini)")
    print(f"  2. Bulanan (bulan ini)")
    print(f"  3. Buat template daftar_siswa.csv")
    pilihan = input(f"\nPilihan [1/2/3]: ").strip()

    if pilihan == "1":
        generate_absensi_harian(siswa)
    elif pilihan == "2":
        generate_absensi_bulanan(siswa)
    elif pilihan == "3":
        buat_template()
    else:
        print("Pilihan tidak valid.")
