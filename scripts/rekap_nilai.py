#!/usr/bin/env python3
"""
📊 Rekap Nilai Siswa — Baca Folder Berisi CSV Nilai → Generate Laporan Excel/CSV

Cara pakai:
    python rekap_nilai.py                      # Baca semua CSV di folder ./nilai/
    python rekap_nilai.py /path/folder-nilai   # Baca dari folder tertentu

Format CSV yang dibaca (dalam folder):
    nilai_kelas_x_ipa_1.csv:
        Nama,MTK,IPA,ING,PPKn
        Budi,85,90,78,80
        ...
"""

import csv
import os
import sys
from pathlib import Path
from datetime import datetime

def baca_folder_nilai(folder="nilai"):
    """Baca semua file CSV dalam folder"""
    path = Path(folder)
    if not path.exists():
        print(f"❌ Folder '{folder}' tidak ditemukan!")
        print(f"   Buat folder 'nilai/' dan isi dengan file CSV nilai siswa.")
        return {}

    semua_data = {}
    for file in path.glob("*.csv"):
        nama_kelas = file.stem.replace("_", " ").title()
        siswa_list = []

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                siswa = {"nama": row.get("Nama", "").strip()}
                for k, v in row.items():
                    if k.lower() != "nama" and v.strip():
                        try:
                            siswa[k] = float(v)
                        except ValueError:
                            siswa[k] = 0.0
                siswa_list.append(siswa)

        if siswa_list:
            semua_data[nama_kelas] = siswa_list
            print(f"  ✅ {file.name}: {len(siswa_list)} siswa")

    return semua_data

def hitung_statistik(siswa_list):
    """Hitung statistik per siswa dan per kelas"""
    mapel_list = []
    for s in siswa_list:
        for k in s:
            if k != "nama":
                mapel_list.append(k)
    mapel_list = sorted(set(mapel_list))

    for siswa in siswa_list:
        nilai_list = [siswa.get(m, 0) for m in mapel_list]
        siswa["rata_rata"] = sum(nilai_list) / len(nilai_list) if nilai_list else 0
        siswa["grade"] = grade(siswa["rata_rata"])
        siswa["status"] = "Lulus" if siswa["rata_rata"] >= 75 else "Tidak Lulus"

    return mapel_list

def grade(nilai):
    if nilai >= 90:
        return "A"
    elif nilai >= 80:
        return "B"
    elif nilai >= 70:
        return "C"
    elif nilai >= 60:
        return "D"
    else:
        return "E"

def generate_csv(semua_data):
    """Generate file CSV rekap"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"rekap_nilai_{timestamp}.csv"

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)

        for kelas, siswa_list in sorted(semua_data.items()):
            mapel_list = hitung_statistik(siswa_list)
            header = ["Kelas", "Nama"] + mapel_list + ["Rata-rata", "Grade", "Status"]
            if f.tell() == 0:
                writer.writerow(header)

            for s in sorted(siswa_list, key=lambda x: x["rata_rata"], reverse=True):
                row = [kelas, s["nama"]]
                for m in mapel_list:
                    row.append(f"{s.get(m, 0):.1f}")
                row.append(f"{s['rata_rata']:.1f}")
                row.append(s["grade"])
                row.append(s["status"])
                writer.writerow(row)

            writer.writerow([])

    print(f"\n✅ Rekap tersimpan ke '{output_file}'")

def generate_laporan_txt(semua_data):
    """Generate laporan TXT rapi"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"laporan_nilai_{timestamp}.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write(f"{'LAPORAN REKAP NILAI SISWA':^80}\n")
        f.write(f"{datetime.now().strftime('%d %B %Y %H:%M'):^80}\n")
        f.write("=" * 80 + "\n\n")

        total_siswa = 0
        total_lulus = 0

        for kelas, siswa_list in sorted(semua_data.items()):
            mapel_list = hitung_statistik(siswa_list)
            f.write(f"{kelas}\n")
            f.write("-" * 80 + "\n")

            fmt_header = f"{'No':4} {'Nama':20}"
            for m in mapel_list:
                fmt_header += f" {m:>8}"
            fmt_header += f" {'Rata':>8} {'Grade':6} {'Status':12}"
            f.write(fmt_header + "\n")
            f.write("-" * 80 + "\n")

            rata_kelas = []
            for i, s in enumerate(sorted(siswa_list, key=lambda x: x["rata_rata"], reverse=True), 1):
                fmt_row = f"{i:4} {s['nama']:20}"
                for m in mapel_list:
                    fmt_row += f" {s.get(m, 0):>8.1f}"
                fmt_row += f" {s['rata_rata']:>8.1f} {s['grade']:6} {s['status']:12}"
                f.write(fmt_row + "\n")
                rata_kelas.append(s["rata_rata"])

            rata_all = sum(rata_kelas) / len(rata_kelas) if rata_kelas else 0
            lulus = sum(1 for s in siswa_list if s["status"] == "Lulus")
            f.write("-" * 80 + "\n")
            f.write(f"{'Rata-rata Kelas':25}: {rata_all:.1f}\n")
            f.write(f"{'Jumlah Siswa':25}: {len(siswa_list)}\n")
            f.write(f"{'Lulus':25}: {lulus}\n")
            f.write(f"{'Tidak Lulus':25}: {len(siswa_list) - lulus}\n\n")

            total_siswa += len(siswa_list)
            total_lulus += lulus

        f.write("=" * 80 + "\n")
        f.write(f"{'RINGKASAN':^80}\n")
        f.write("=" * 80 + "\n")
        f.write(f"{'Total Siswa':25}: {total_siswa}\n")
        f.write(f"{'Total Lulus':25}: {total_lulus}\n")
        f.write(f"{'Total Tidak Lulus':25}: {total_siswa - total_lulus}\n")

    print(f"✅ Laporan tersimpan ke '{output_file}'")

if __name__ == "__main__":
    print("📊 REKAP NILAI SISWA\n")
    print("Membaca folder nilai...")

    folder = sys.argv[1] if len(sys.argv) > 1 else "nilai"
    semua_data = baca_folder_nilai(folder)

    if not semua_data:
        print("\nTidak ada data nilai ditemukan.")
        print("Buat folder 'nilai/' dengan file CSV seperti:")
        print("  nilai/kelas_x_ipa_1.csv:")
        print("    Nama,MTK,IPA,ING,PPKn")
        print("    Budi,85,90,78,80")
        exit()

    print(f"\n📁 Ditemukan {len(semua_data)} kelas:")
    for kelas in semua_data:
        print(f"  • {kelas}: {len(semua_data[kelas])} siswa")

    generate_csv(semua_data)
    generate_laporan_txt(semua_data)
