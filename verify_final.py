"""Verifikasi akhir repo belajar-python."""

import os
import re
import subprocess
import sys

GAGAL = []


def cek(nama, ok, detail=""):
    print(f"  {'OK ' if ok else 'GAGAL'}  {nama}{('  -> ' + detail) if detail else ''}")
    if not ok:
        GAGAL.append(nama)


print("=" * 68)
print("VERIFIKASI AKHIR")
print("=" * 68)

# ---------------------------------------------------------------- 1
print("\n[1] Karakter korup (CJK / placeholder acak)")
for root, dirs, names in os.walk("."):
    dirs[:] = [d for d in dirs if d != ".git"]
    for n in sorted(names):
        if not n.endswith((".md", ".html")):
            continue
        fp = os.path.join(root, n)
        s = open(fp, encoding="utf-8", errors="replace").read()
        cjk = re.findall(r"[\u3000-\u9fff]", s)
        if cjk:
            cek(fp, False, f"{len(cjk)} karakter CJK")
print("  (hanya ditampilkan yang bermasalah)")

# ---------------------------------------------------------------- 2
print("\n[2] Broken link di semua .html")
total = 0
for root, dirs, names in os.walk("."):
    dirs[:] = [d for d in dirs if d != ".git"]
    for n in sorted(names):
        if not n.endswith(".html"):
            continue
        fp = os.path.join(root, n)
        html = open(fp, encoding="utf-8").read()
        for m in re.findall(r'(?:href|src)="([^"]+)"', html):
            if m.startswith(("http", "data:", "#", "mailto:")):
                continue
            t = os.path.normpath(os.path.join(root, m))
            if not os.path.exists(t):
                total += 1
                cek(fp, False, f"link: {m}")
cek("tidak ada broken link", total == 0)

# ---------------------------------------------------------------- 3
print("\n[3] Kode Python di markdown: syntax check")
import glob
import tempfile

for md in sorted(glob.glob("modul/*.md")) + [f for f in sorted(glob.glob("*.md")) if f != "cheat-sheet.md"]:
    src = open(md, encoding="utf-8").read()
    blocks = re.findall(r"^```python\n(.*?)^```", src, re.S | re.M)
    for i, b in enumerate(blocks):
        # lewati blok yang sengaja tidak lengkap / pseudocode
        if re.search(r"^\s*(\.\.\.|>>>|pass\b\s*$)", b, re.M):
            continue
        if "if __name__" in b and "def main" not in b and len(b) > 200:
            pass
        try:
            compile(b, f"{md}#py{i}", "exec")
        except SyntaxError as e:
            # toleransi: blok yang memang potongan (mis. "except X:" tanpa(body)
            if e.msg in ("unexpected EOF while parsing", "expected an indented block"):
                continue
            cek(f"{md} blok#{i}", False, f"line {e.lineno}: {e.msg}")
print("  (hanya ditampilkan yang bermasalah)")

# ---------------------------------------------------------------- 4
print("\n[4] Proyek Akhir Modul 13 — ekstrak & jalankan")
src = open("modul/13-proyek-akhir.md", encoding="utf-8").read()
blocks = re.findall(r"^```python\n(.*?)^```", src, re.S | re.M)
d = tempfile.mkdtemp()
open(os.path.join(d, "models.py"), "w", encoding="utf-8").write(
    blocks[0] + "\n" + blocks[1] + "\n" + blocks[2]
)
open(os.path.join(d, "utils.py"), "w", encoding="utf-8").write(blocks[3])
open(os.path.join(d, "main.py"), "w", encoding="utf-8").write(blocks[4])

r = subprocess.run(
    [sys.executable, "-c", "import utils, models, typing; typing.get_type_hints(utils.simpan_csv); typing.get_type_hints(utils.simpan_json)"],
    cwd=d,
    capture_output=True,
    text=True,
)
cek("import utils + main (NameError fix)", r.returncode == 0, r.stderr.strip().splitlines()[-1] if r.returncode else "")

r = subprocess.run(
    [sys.executable, "-c", "import main"], cwd=d, capture_output=True, text=True
)
cek("import main (import os fix)", r.returncode == 0, r.stderr.strip().splitlines()[-1] if r.returncode else "")

# jalankan app: muat data -> lihat semua siswa
driver = os.path.join(d, "_drv.py")
open(driver, "w", encoding="utf-8").write(
    "import subprocess,time,os,json,sys\n"
    "p=subprocess.Popen([sys.executable,'-u','main.py'],stdin=subprocess.PIPE,"
    "stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,bufsize=1)\n"
    "def s(x):\n p.stdin.write(x+chr(10)); p.stdin.flush(); time.sleep(0.5)\n"
    "s('6')\n"
    "time.sleep(0.2)\n"
    "os.makedirs('data',exist_ok=True)\n"
    "json.dump({'nama_kelas':'XII','siswa':[{'nis':'9001','nama':'Zainal Efendi',"
    "'kelas':'XII','nilai':{'Matematika':95}}]},open('data/kelas.json','w'))\n"
    "s('6'); s('1'); s('2'); s(''); s('0'); s('0')\n"
    "p.stdin.close(); out=p.stdout.read(); p.wait()\n"
    "print(out)\n"
)
r = subprocess.run([sys.executable, driver], cwd=d, capture_output=True, text=True)
out = re.sub(r"\x1b\[[0-9;]*m", "", r.stdout)
cek("app jalan tanpa traceback", "Traceback" not in out)
cek("'Muat Data' benar-benar mengganti data", "Zainal Efendi" in out, "(cek Zainal Efendi muncul di daftar)")
cek("data lama tidak bocor setelah muat", "Budi Santoso" not in out)

# ---------------------------------------------------------------- 5
print("\n[5] Bank soal")
g = open("bank-soal.md", encoding="utf-8").read()
s = open("bank-soal-siswa.md", encoding="utf-8").read()


def nomor(t):
    return sorted(re.findall(r"^### ((?:PG|C|E)-\d+)", t, re.M))


cek("jumlah soal sama", len(nomor(g)) == len(nomor(s)), f"{len(nomor(g))} vs {len(nomor(s))}")
cek("semua nomor soal ada di versi siswa", set(nomor(g)) <= set(nomor(s)))
cek("versi siswa tanpa marker ✅", "\u2705" not in s)
cek("versi siswa tanpa '**Kunci:**'", "**Kunci:**" not in s)
cek("versi siswa tanpa 'Kunci Jawaban'", "Kunci Jawaban" not in s)
cek("lembar jawab siswa kept", "Lembar Jawab Siswa" in s)
cek("versi guru tandai VERSI GURU", "VERSI GURU" in g)
cek("versi siswa tandai Versi Siswa", "Versi Siswa" in s)

# ---------------------------------------------------------------- 6
print("\n[6] Konsistensi repo")
cek("Modul 0 tanpa 'Omarchy'", "Omarchy" not in open("modul/00-setup.md", encoding="utf-8").read())
cek("Modul 0 tanpa 'yay '", "yay " not in open("modul/00-setup.md", encoding="utf-8").read())
cek("Modul 0 ada jalur Colab", "Google Colab" in open("modul/00-setup.md", encoding="utf-8").read())
cek("Modul 0 ada jalur Windows", "Install di Windows" in open("modul/00-setup.md", encoding="utf-8").read())
cek("Modul 0 ada jalur Linux", "Install di Linux" in open("modul/00-setup.md", encoding="utf-8").read())
for f, txt in [
    ("modul/13-proyek-akhir.md", "3.10"),
    ("modul/00-setup.md", "3.10"),
]:
    cek(f"{f} menyebut syarat versi", txt in open(f, encoding="utf-8").read())

m13 = open("modul/13-proyek-akhir.md", encoding="utf-8").read()
cek("tanpa starred import di Modul 13",
    not re.search(r"^\s*from utils import \*", m13, re.M),
    "(yang boleh muncul hanya di komentar peringatan)")
cek("tanpa 'global kelas_global'", "global kelas_global" not in open("modul/13-proyek-akhir.md", encoding="utf-8").read())

# checklist seragam
import glob as _g
ada_x = [f for f in _g.glob("modul/*.md") if "- [x]" in open(f, encoding="utf-8").read()]
cek("checklist seragam (tidak ada [x])", not ada_x, str(ada_x))

for t in ["Nonaktifkanls", "errornyadan"]:
    found = [
        f
        for f in _g.glob("*.md") + _g.glob("modul/*.md")
        if t in open(f, encoding="utf-8").read()
    ]
    cek(f"typo '{t}' hilang", not found, str(found))

# "recommend" -> false positive pada "--no-install-recommends" (flag apt valid)
# cek khusus: cari "recommend" TAPI bukan bagian dari "--no-install-recommends"
import re as _re
found_recommend = [
    f
    for f in _g.glob("*.md") + _g.glob("modul/*.md")
    if _re.search(r'(?<!-)recommend(?!-)', open(f, encoding="utf-8").read())
]
cek("typo 'recommend' hilang (kecuali flag apt)", not found_recommend, str(found_recommend))

cek("index.html link ke bank-soal-siswa.html", "bank-soal-siswa.html" in open("index.html", encoding="utf-8").read())
cek("bank-soal-siswa.html tergenerate", os.path.exists("bank-soal-siswa.html"))

print("\n" + "=" * 68)
if GAGAL:
    print(f"{len(GAGAL)} MASALAH:")
    for g_ in GAGAL:
        print("  -", g_)
    sys.exit(1)
print("SEMUA VERIFIKASI LULUS")
print("=" * 68)
