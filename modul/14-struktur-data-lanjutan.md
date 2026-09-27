# Modul 14: Struktur Data Lanjutan & Library Standar

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Algoritma & Pemrograman | AP | Merancang & mengimplementasikan struktur data abstrak kompleks dengan *library* standar |
| Berpikir Komputasional | BK | Memilih struktur data yang tepat untuk efisiensi & abstraksi |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Memilih struktur data yang **tepat** untuk persoalan (bukan cuma pakai `list`/`dict` default)
- Menggunakan `collections` (`deque`, `Counter`, `defaultdict`, `OrderedDict`, `namedtuple`)
- Memahami & memakai `dataclasses` untuk kelas data yang bersih
- Mengetikkan kode dengan `typing` (`TypeVar`, `Generic`, `Protocol`, `TypedDict`)
- Memanfaatkan `heapq` untuk *priority queue* & `itertools` untuk kombinatori
- Menjelaskan *trade-off* mutabilitas vs imutabilitas, performa memori & akses

---

## 1. Kenapa Butuh Lebih dari `list` & `dict`?

`list` & `dict` serbaguna — tapi **tidak optimal** untuk semua kasus.

| Kebutuhan | Struktur Standar | Lebih Tepat (`collections` / `heapq` / `dataclasses`) |
|-----------|------------------|------------------------------------------------------|
| Antrian FIFO efisien | `list.pop(0)` → **O(n)** | `deque.popleft()` → **O(1)** |
| Tumpukan LIFO | `list.append`/`pop` → OK | `deque` juga OK |
| Hitung frekuensi item | `dict` manual | `Counter` → 1 baris |
| Dictionary dengan nilai default | `if k not in d: d[k]=[]` | `defaultdict(list)` |
| Record data immutable | `tuple` / `dict` | `namedtuple` / `dataclass(frozen=True)` |
| Prioritas (min/max cepat) | `sorted(list)` tiap kali | `heapq` → **O(log n)** |
| Kombinasi / permutasi | *nested loop* manual | `itertools` → declaratif & cepat |

> 💡 **Prinsip:** Pilih struktur yang **mencerminkan maksud** kode — kode jadi terbaca, cepat, & minim bug.

---

## 2. `collections.deque` — Antrian & Tumpukan Cepat

```python
from collections import deque

# Antrian (FIFO) — O(1) di kedua ujung
antrian = deque(["Ali", "Budi", "Citra"])
antrian.append("Dewi")      # kanan
antrian.popleft()           # kiri → "Ali"

# Tumpukan (LIFO) — juga O(1)
tumpuk = deque()
tumpuk.append(1)
tumpuk.append(2)
tumpuk.pop()                # 2

# Rotasi (berguna untuk scheduling round-robin)
d = deque([1, 2, 3, 4])
d.rotate(1)                 # deque([4, 1, 2, 3])
d.rotate(-2)                # deque([3, 4, 1, 2])
```

> ⚠️ `deque` **tidak** mendukung indexing `d[5]` secepat `list` (O(1) vs O(n)). Pakai untuk *head/tail* operations.

---

## 3. `collections.Counter` — Hitung Frekuensi Otomatis

```python
from collections import Counter

teks = "banana"
hitung = Counter(teks)
print(hitung)               # Counter({'a': 3, 'n': 2, 'b': 1})

# Operasi set-like
Counter('abracadabra') + Counter('alakazam')
# Counter({'a': 6, 'b': 2, 'r': 2, 'c': 2, 'd': 1, 'l': 1, 'k': 1, 'z': 1, 'm': 1})

# Top-N terbanyak
Counter("abracadabra").most_common(3)
# [('a', 5), ('b', 2), ('r', 2)]
```

---

## 4. `collections.defaultdict` — Hilangkan Cek `if key in dict`

```python
from collections import defaultdict

# Kelompokkan kata by panjang
kata = ["apel", "jeruk", "mangga", "pisang", "durian"]
kelompok = defaultdict(list)
for k in kata:
    kelompok[len(k)].append(k)

print(dict(kelompok))
# {5: ['apel', 'mangga'], 6: ['jeruk', 'pisang', 'durian']}

# Counter alternatif
dd = defaultdict(int)
for huruf in "banana":
    dd[huruf] += 1
```

> 💡 `defaultdict` **otomatis** bikin key baru saat diakses — cocok untuk *grouping* & *counting*.

---

## 5. `collections.namedtuple` — Record Ringan Immutable

```python
from collections import namedtuple

# Definisi sekali, pakai berkali-kali
Siswa = namedtuple("Siswa", ["nama", "kelas", "nilai"])

s1 = Siswa("Ani", "XI-1", 88)
s2 = Siswa(nama="Budi", kelas="XI-2", nilai=92)  # keyword args OK

print(s1.nama)      # "Ani" — akses atribut, BUKAN s1[0]
print(s1._asdict()) # {'nama': 'Ani', 'kelas': 'XI-1', 'nilai': 88}

# Immutable — aman untuk key dict / set
daftar = {s1: "Lulus", s2: "Lulus"}
```

---

## 6. `dataclasses` — Kelas Data Modern (Python 3.7+)

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Siswa:
    nama: str
    kelas: str
    nilai: List[int] = field(default_factory=list)  # mutable default aman

    def rata_rata(self) -> float:
        return sum(self.nilai) / len(self.nilai) if self.nilai else 0.0

# Pakai
s = Siswa("Citra", "XI-3", [80, 90, 85])
print(s.rata_rata())   # 85.0

# Immutable version
@dataclass(frozen=True)
class Koordinat:
    x: float
    y: float

# p = Koordinat(1, 2)
# p.x = 3  # FrozenInstanceError — aman!
```

> 💡 **`field(default_factory=...)`** wajib untuk *mutable default* (list, dict, set). Tanpa itu, *shared reference* bug muncul.

---

## 7. `typing` — Type Hints Lanjutan

```python
from typing import TypeVar, Generic, Protocol, TypedDict, List, Dict

# Generic — class yang kerja untuk banyak tipe
T = TypeVar("T")

class Kotak(Generic[T]):
    def __init__(self, isi: T) -> None:
        self.isi = isi

    def ambil(self) -> T:
        return self.isi

k_int = Kotak(42)
k_str = Kotak("halo")

# Protocol — structural subtyping (duck typing formal)
class BisaSuara(Protocol):
    def suara(self) -> str: ...

class Kucing:
    def suara(self) -> str: return "Meong"

class Mobil:
    def suara(self) -> str: return "Broom"

def dengarkan(hewan: BisaSuara) -> None:
    print(hewan.suara())

dengarkan(Kucing())  # OK
dengarkan(Mobil())   # OK — tidak perlu inherit!

# TypedDict — dict dengan schema
class Film(TypedDict):
    judul: str
    tahun: int
    rating: float

f: Film = {"judul": "Matrix", "tahun": 1999, "rating": 8.7}
# f["genre"] = "Sci-Fi"  # Error static checker — key tidak di schema
```

---

## 8. `heapq` — Priority Queue (Min-Heap)

```python
import heapq

# Min-heap default
h = []
for x in [5, 2, 8, 1, 9]:
    heapq.heappush(h, x)

print(h)               # [1, 2, 8, 5, 9] — struktur heap
print(heapq.heappop(h))# 1 — selalu terkecil

# Max-heap: negasi nilai
max_h = []
for x in [5, 2, 8, 1, 9]:
    heapq.heappush(max_h, -x)

print(-heapq.heappop(max_h))  # 9

# heapify — ubah list jadi heap in-place O(n)
data = [5, 2, 8, 1, 9]
heapq.heapify(data)
print(data)  # [1, 2, 8, 5, 9]
```

> 💡 `heapq` **hanya min-heap**. Untuk max-heap, negasi nilai. Tidak ada *decrease-key* bawaan — buat *lazy deletion* jika butuh.

---

## 9. `itertools` — Kombinatori & Iterator Efisien

```python
import itertools

# Produk Cartesian (nested loop declaratif)
for a, b in itertools.product("AB", "12"):
    print(a, b)  # A1, A2, B1, B2

# Permutasi & Kombinasi
list(itertools.permutations("ABC", 2))  # AB, AC, BA, BC, CA, CB
list(itertools.combinations("ABC", 2))  # AB, AC, BC

# Infinite iterators
itertools.count(10, 2)   # 10, 12, 14, ...
itertools.cycle("AB")    # A, B, A, B, ...
itertools.repeat(7, 3)   # 7, 7, 7

# Combinatoric iterators praktis
list(itertools.accumulate([1, 2, 3, 4]))  # [1, 3, 6, 10] — prefix sum
list(itertools.chain([1,2], [3,4]))       # [1, 2, 3, 4]
```

---

## 10. Mutabilitas vs Imutabilitas — Pilih Bijak

| Tipe | Mutable? | Cocok Untuk |
|------|----------|-------------|
| `list` | Ya | Koleksi berubah |
| `dict` | Ya | Mapping berubah |
| `set` | Ya | Unik berubah |
| `tuple` | **Tidak** | Record tetap, key dict |
| `frozenset` | **Tidak** | Set sebagai key dict |
| `dataclass(frozen=True)` | **Tidak** | DTO, value object |
| `namedtuple` | **Tidak** | Record ringan |

> ⚠️ **Jebakan:** `tuple` yang isinya `list` **bisa diubah** isi list-nya! `t = ([1], [2]); t[0].append(99)` → `([1, 99], [2])`. Gunakan `frozen=True` dataclass atau `tuple(tuple(...))` untuk benar-benar immutable.

---

## 🧪 Latihan

1. **Antrian Printer** — Buat simulasi antrian cetak pakai `deque`: `tambah_job(nama, halaman)`, `proses_satu()` → cetak nama & sisa antrian.
2. **Analisis Teks** — Pakai `Counter` hitung 10 kata paling sering di file `cerita.txt` (abaikan stopwords sederhana).
3. **Grouping Siswa** — Pakai `defaultdict(list)` kelompokkan list `dict` siswa by `kelas`.
4. **Dataclass vs Namedtuple** — Buat `Mahasiswa` pakai keduanya. Coba ubah nilai di keduanya. Catat perbedaan error.
5. **Generic Stack** — Tulis `class Stack(Generic[T])` dengan `push`, `pop`, `peek`, `is_empty`. Uji dengan `Stack[int]` & `Stack[str]`.
6. **Top-K dengan Heap** — Diberi list 10000 angka acak, ambil 5 terbesar pakai `heapq` (hint: `heapq.nlargest`).
7. **Kombinasi Menu** — Warung punya 5 makanan & 3 minuman. Pakai `itertools.product` cetak semua combo "makanan + minuman".

---

## ✅ Checklist Paham

- [ ] Bisa jelaskan kapan pakai `deque` vs `list`
- [ ] `Counter` & `defaultdict` menghilangkan boilerplate counting/grouping
- [ ] `namedtuple` & `dataclass` untuk record — bedakan kapan pakai mana
- [ ] `field(default_factory=...)` untuk mutable default di dataclass
- [ ] `TypeVar` + `Generic` bikin class reusable multi-tipe
- [ ] `Protocol` = interface structural (duck typing formal)
- [ ] `TypedDict` validasi schema dict di static checker
- [ ] `heapq` untuk priority queue O(log n)
- [ ] `itertools` untuk kombinatori declaratif
- [ ] Sadar: `tuple` bersarang `list` **bukan** benar-benar immutable

**Kalau semua tercentang → lanjut ke Modul 15 (Kompleksitas Algoritma).**