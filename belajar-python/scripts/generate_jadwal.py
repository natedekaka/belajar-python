#!/usr/bin/env python3
"""
📅 Generate Jadwal Mengajar — Dari Template CSV ke Format Rapi

Cara pakai:
    python generate_jadwal.py

Membaca file template jadwal.csv dan generate jadwal rapi:
    format: Hari,Jam Ke-,Mata Pelajaran,Kelas,Ruang
"""

import csv
from datetime import datetime
from pathlib import Path

TEMPLATE_FILE = "jadwal_template.csv"
OUTPUT_FILE = "jadwal_mengajar.txt"

TEMPLATE_CONTOH = """Hari,Jam Ke-,Mata Pelajaran,Kelas,Ruang
Senin,1,Python Dasar,X IPA 1,Laboratorium Komputer
Senin,2,Python Dasar,X IPA 1,Laboratorium Komputer
Senin,3,Informatika,X IPA 2,Ruang 103
Selasa,1,Informatika,XI IPA 1,Ruang 104
Selasa,2,Praktek Python,XI IPA 1,Laboratorium Komputer
Rabu,3,Python Dasar,X IPA 2,Laboratorium Komputer
Rabu,4,Informatika,X IPA 2,Ruang 103
Kamis,1,Praktek Python,XII IPA 1,Laboratorium Komputer
Kamis,2,Praktek Python,XII IPA 1,Laboratorium Komputer
Jumat,1,Informatika,XI IPA 2,Ruang 104
"""

HARI_INDONESIA = [
    "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"
]

def buat_template():
    """Buat file template jika belum ada"""
    if not Path(TEMPLATE_FILE).exists():
        with open(TEMPLATE_FILE, "w") as f:
            f.write(TEMPLATE_CONTOH)
        print(f"📝 Template '{TEMPLATE_FILE}' telah dibuat.")
        print(f"   Edit file tersebut sesuai jadwal kamu, lalu jalankan ulang.")
        print(f"   Format: Hari,Jam Ke-,Mata Pelajaran,Kelas,Ruang")
        return False
    return True

def baca_jadwal():
    """Baca jadwal dari CSV"""
    jadwal = []
    with open(TEMPLATE_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            jadwal.append(row)
    return jadwal

def kelompok_per_hari(jadwal):
    """Kelompokkan jadwal per hari"""
    per_hari = {hari: [] for hari in HARI_INDONESIA}
    for entry in jadwal:
        hari = entry["Hari"].strip().title()
        if hari in per_hari:
            per_hari[hari].append(entry)
    return per_hari

def generate_txt(jadwal_per_hari):
    """Generate file jadwal rapi"""
    minggu_ke = (datetime.now().isocalendar()[1])
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("=" * 65 + "\n")
        f.write(f"        JADWAL MENGAJAR — Minggu ke-{minggu_ke}\n")
        f.write(f"        {datetime.now().strftime('%B %Y')}\n")
        f.write("=" * 65 + "\n\n")
        
        for hari in HARI_INDONESIA:
            entries = jadwal_per_hari.get(hari, [])
            if not entries:
                continue
            
            f.write(f"╔══ {hari.upper()} ═══════════════════════════════════════\n")
            
            for entry in sorted(entries, key=lambda x: int(x.get("Jam Ke-", 0))):
                jam = entry.get("Jam Ke-", "")
                mapel = entry.get("Mata Pelajaran", "")
                kelas = entry.get("Kelas", "")
                ruang = entry.get("Ruang", "")
                f.write(f"║  Jam {jam:>2}  │  {mapel:<20}  │  {kelas:<12}  │  {ruang}\n")
            
            f.write("╚" + "═" * 60 + "\n\n")
        
        # Ringkasan
        total_jam = sum(
            1 for hari_data in jadwal_per_hari.values()
            for _ in hari_data
        )
        f.write("-" * 65 + "\n")
        f.write(f"  Total jam mengajar minggu ini: {total_jam} jam\n")
        f.write(f"  Dicetak: {datetime.now().strftime('%d %B %Y %H:%M')}\n")
        f.write("-" * 65 + "\n")
    
    print(f"✅ Jadwal tersimpan ke '{OUTPUT_FILE}'")
    print(f"   Total {total_jam} jam mengajar minggu ini.")

def generate_html(jadwal_per_hari):
    """Generate jadwal versi HTML (bonus)"""
    html_file = "jadwal_mengajar.html"
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write("""<!DOCTYPE html>
<html lang="id">
<head><meta charset="UTF-8"><title>Jadwal Mengajar</title>
<style>
    body { font-family: sans-serif; max-width: 800px; margin: auto; padding: 20px; }
    h1 { text-align: center; color: #333; }
    h2 { background: #4a90d9; color: white; padding: 8px; border-radius: 5px; }
    table { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
    th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
    th { background: #f0f0f0; }
    .summary { background: #e8f5e9; padding: 15px; border-radius: 5px; }
</style></head><body>
<h1>📅 Jadwal Mengajar</h1>
""")
        
        for hari in HARI_INDONESIA:
            entries = jadwal_per_hari.get(hari, [])
            if not entries:
                continue
            f.write(f"<h2>{hari}</h2>\n<table>\n")
            f.write("<tr><th>Jam Ke-</th><th>Mata Pelajaran</th><th>Kelas</th><th>Ruang</th></tr>\n")
            for entry in sorted(entries, key=lambda x: int(x.get("Jam Ke-", 0))):
                f.write(f"<tr><td>{entry['Jam Ke-']}</td><td>{entry['Mata Pelajaran']}</td><td>{entry['Kelas']}</td><td>{entry['Ruang']}</td></tr>\n")
            f.write("</table>\n")
        
        f.write(f'<div class="summary"><p>Dicetak: {datetime.now().strftime("%d %B %Y %H:%M")}</p></div>\n')
        f.write("</body></html>")
    
    print(f"✅ Jadwal HTML tersimpan ke '{html_file}'")

if __name__ == "__main__":
    print("📅 GENERATE JADWAL MENGAJAR\n")
    
    if not buat_template():
        exit()
    
    jadwal = baca_jadwal()
    if not jadwal:
        print("❌ File jadwal kosong!")
        exit()
    
    per_hari = kelompok_per_hari(jadwal)
    generate_txt(per_hari)
    generate_html(per_hari)
