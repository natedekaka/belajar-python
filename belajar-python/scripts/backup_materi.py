#!/usr/bin/env python3
"""
💾 Backup Materi Ajar — Otomatis Backup & Versi Folder Materi

Cara pakai:
    python backup_materi.py ~/Documents/Materi-Ajar
    python backup_materi.py ~/Documents/Materi-Ajar ~/Backup/Materi
"""

import shutil
import sys
from pathlib import Path
from datetime import datetime
import json

KONFIG_FILE = Path.home() / ".config" / "backup_materi_config.json"

def backup_file(src: Path, dst: Path):
    """Copy single file with progress"""
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        return True, None
    except Exception as e:
        return False, str(e)

def backup_folder(src: str, dst: str = None):
    """Backup folder materi dengan timestamp"""
    src_path = Path(src).expanduser().resolve()

    if not src_path.exists():
        print(f"❌ Folder source tidak ditemukan: {src_path}")
        return False

    if dst is None:
        dst = str(src_path.parent / f"{src_path.name}_backup")
    dst_path = Path(dst).expanduser().resolve()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    dst_timestamped = dst_path / f"{src_path.name}_{timestamp}"

    print(f"📂 Source: {src_path}")
    print(f"💾 Destinasi: {dst_timestamped}")
    print()

    total_files = sum(1 for _ in src_path.rglob("*") if _.is_file())
    if total_files == 0:
        print("⚠️  Tidak ada file untuk di-backup.")
        return False

    print(f"📊 Total file: {total_files}")
    print(f"⏳ Memulai backup...\n")

    copied = 0
    failed = 0

    for file_path in src_path.rglob("*"):
        if file_path.is_file():
            relative = file_path.relative_to(src_path)
            dest_file = dst_timestamped / relative

            success, error = backup_file(file_path, dest_file)
            if success:
                copied += 1
                if copied % 10 == 0 or copied == total_files:
                    print(f"  ✅ {copied}/{total_files} — {relative}", end="\r")
            else:
                failed += 1
                print(f"\n  ❌ Gagal: {relative} — {error}")

    print(f"\n\n📋 Hasil Backup:")
    print(f"  ✅ Berhasil: {copied}")
    print(f"  ❌ Gagal: {failed}")
    print(f"  📁 Tersimpan di: {dst_timestamped}")

    info = {
        "source": str(src_path),
        "destination": str(dst_timestamped),
        "timestamp": timestamp,
        "total_files": total_files,
        "copied": copied,
        "failed": failed,
        "size": f"{sum(f.stat().st_size for f in src_path.rglob('*') if f.is_file()) / 1024 / 1024:.1f} MB"
    }

    info_file = dst_timestamped / "_info_backup.json"
    with open(info_file, "w") as f:
        json.dump(info, f, indent=2)

    print(f"  📄 Info backup: {info_file}")
    print(f"  💾 Ukuran: {info['size']}")

    simpan_riwayat(info)
    return True

def simpan_riwayat(info: dict):
    """Simpan riwayat backup ke file konfigurasi"""
    riwayat = []
    if KONFIG_FILE.exists():
        try:
            with open(KONFIG_FILE, "r") as f:
                data = json.load(f)
                riwayat = data.get("riwayat", [])
        except (json.JSONDecodeError, KeyError):
            riwayat = []

    KONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    riwayat.append(info)
    with open(KONFIG_FILE, "w") as f:
        json.dump({"riwayat": riwayat[-50:]}, f, indent=2)

def lihat_riwayat():
    """Lihat riwayat backup"""
    if not KONFIG_FILE.exists():
        print("📭 Belum ada riwayat backup.")
        return

    with open(KONFIG_FILE, "r") as f:
        data = json.load(f)

    riwayat = data.get("riwayat", [])
    if not riwayat:
        print("📭 Belum ada riwayat backup.")
        return

    print(f"\n📜 RIWAYAT BACKUP (terakhir 50)")
    print("=" * 80)
    for i, r in enumerate(reversed(riwayat), 1):
        print(f"{i:3}. {r['timestamp']} — {r['source']}")
        print(f"     → {r['destination']}")
        print(f"     {r['copied']} file, {r['size']}")
        print()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("""
💾 Backup Materi Ajar

Usage:
    python backup_materi.py <folder_source> [folder_destinasi]

    Contoh:
    python backup_materi.py ~/Documents/Materi-Ajar
    python backup_materi.py ~/Documents/Materi-Ajar ~/Backup/Materi

Perintah:
    python backup_materi.py --riwayat     Lihat riwayat backup
        """)
        sys.exit(1)

    if sys.argv[1] == "--riwayat":
        lihat_riwayat()
    else:
        src = sys.argv[1]
        dst = sys.argv[2] if len(sys.argv) > 2 else None
        backup_folder(src, dst)
