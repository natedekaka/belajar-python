#!/usr/bin/env python3
"""
📂 Rename Tugas Siswa — Otomatis Merapikan Nama File Tugas

Fungsi: Merename file tugas dari format sembarang menjadi:
        [NIS]_[Nama]_[JenisTugas].[ext]

Cara pakai:
    python rename_tugas.py /path/folder-tugas

Contoh:
    "Budi_Tugas1.pdf"      → "1001_Budi Santoso_Tugas1.pdf"
    "ani-ipa-essay.docx"   → "1002_Ani Wijaya_IPA_Essay.docx"
"""

import os
import re
import sys
from pathlib import Path

# Dictionary mapping nama siswa → NIS (edit sesuai data kelas)
SISWA = {
    "budi santoso": "1001",
    "ani wijaya": "1002",
    "citra dewi": "1003",
    "dedi permana": "1004",
    "eva kurniawan": "1005",
    "fajar ramadhan": "1006",
    "gita sari": "1007",
    "hendra gunawan": "1008",
    "intan permata": "1009",
    "joko susilo": "1010",
}

# Jenis tugas yang dikenal
JENIS_TUGAS = ["tugas", "uts", "uas", "quiz", "essay", "praktikum"]

def bersihkan_nama(nama_kotor: str) -> str:
    """Bersihkan nama dari angka, underscore, delimiter"""
    # Hapus ekstensi
    nama = Path(nama_kotor).stem
    nama = re.sub(r'[_-]', ' ', nama)
    nama = re.sub(r'\d+', '', nama)
    nama = ' '.join(nama.split())
    return nama.strip().lower()

def cari_siswa(nama_bersih: str):
    """Cocokkan nama dengan database siswa"""
    for nama_siswa, nis in SISWA.items():
        kata_kunci = nama_siswa.split()
        if all(kata in nama_bersih for kata in kata_kunci):
            return nama_siswa.title(), nis
    return None, None

def cari_jenis_tugas(nama_file: str) -> str:
    """Cari jenis tugas dari nama file"""
    nama_lower = nama_file.lower()
    for jenis in JENIS_TUGAS:
        if jenis in nama_lower:
            return jenis.title()
    return "Tugas"

def rename_file(folder: str):
    """Proses rename semua file dalam folder"""
    folder_path = Path(folder)
    if not folder_path.exists():
        print(f"❌ Folder '{folder}' tidak ditemukan!")
        return
    
    files = [f for f in folder_path.iterdir() if f.is_file()]
    print(f"📁 Ditemukan {len(files)} file dalam '{folder}'")
    
    berhasil = 0
    gagal = 0
    
    for file in files:
        if file.name.startswith('.'):
            continue
        
        ekstensi = file.suffix
        nama_file = file.name
        nama_bersih = bersihkan_nama(nama_file)
        nama_siswa, nis = cari_siswa(nama_bersih)
        
        if nama_siswa and nis:
            jenis_tugas = cari_jenis_tugas(nama_file)
            nama_baru = f"{nis}_{nama_siswa}_{jenis_tugas}{ekstensi}"
            path_baru = file.parent / nama_baru
            
            try:
                file.rename(path_baru)
                print(f"  ✅ {nama_file:40s} → {nama_baru}")
                berhasil += 1
            except Exception as e:
                print(f"  ❌ {nama_file}: {e}")
                gagal += 1
        else:
            print(f"  ⚠️  {nama_file:40s} — Tidak bisa dikenali (skip)")
            gagal += 1
    
    print(f"\n📊 Ringkasan:")
    print(f"  Berhasil: {berhasil}")
    print(f"  Gagal/Skip: {gagal}")
    print(f"  Total: {berhasil + gagal}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
📂 Rename Tugas Siswa — Usage:
    python rename_tugas.py <folder_tugas>
    
    Contoh:
    python rename_tugas.py ./tugas_siswa
    python rename_tugas.py /home/user/Downloads/tugas
        """)
        sys.exit(1)
    
    rename_file(sys.argv[1])
