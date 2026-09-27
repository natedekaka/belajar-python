# Modul 15: Kompleksitas Algoritma & Analisis Strategi

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Berpikir Komputasional | BK | Menganalisis beberapa strategi algoritmik secara kritis → banyak alternatif solusi, justifikasi efisiensi/kelebihan/keterbatasan, memilih solusi terbaik dengan merancang struktur data yang lebih kompleks & abstrak |
| Algoritma & Pemrograman | AP | Memahami algoritma standar & strategi efisiensinya |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menghitung & membandingkan **kompleksitas waktu & ruang** (Big-O, Big-Ω, Big-Θ)
- Menganalisis **best / average / worst case** sebuah algoritma
- Memahami strategi *divide & conquer*, *greedy*, *dynamic programming*, *backtracking*
- Membandingkan **sorting**: Timsort (Python), Quicksort, Mergesort, Heapsort — kapan pakai mana
- Memahami **hashing**: tabel hash, collision handling, load factor
- Melakukan **benchmarking** jujur di Python (`timeit`, `cProfile`)
- Menuliskan **justifikasi tertulis** pemilihan algoritma (seperti yang CP minta)

---

## 1. Kenapa Analisis Kompleksitas?

```python
# Dua cara cari max di list
def max_v1(arr):
    m = arr[0]
    for x in arr:
        if x > m:
            m = x
    return m

def max_v2(arr):
    return max(arr)  # built-in C-optimized
```

Keduanya **benar**. Tapi `max_v1` O(n) Python-level loop, `max_v2` O(n) C-level → **10–100× lebih cepat**.

> 💡 **Analisis kompleksitas** bukan soal "mana benar" — tapi "mana **efisien & tepat** untuk skala & konteks".

---

## 2. Notasi Asimtotik — Bahasa Umum Efisiensi

| Notasi | Artinya | Contoh |
|--------|---------|--------|
| **O(f(n))** | Batas **atas** (worst-case) | `O(n²)` — tidak lebih lambat dari n² |
| **Ω(f(n))** | Batas **bawah** (best-case) | `Ω(n)` — tidak lebih cepat dari n |
| **Θ(f(n))** | Batas **ketat** (average/tight) | `Θ(n log n)` — persis proporsional n log n |

**Aturan praktis:**
- Hanya **suku dominan**: `O(3n² + 5n + 100)` → `O(n²)`
- **Konstanta diabaikan**: `O(1000n)` → `O(n)`
- **Tambah** untuk sequential: `O(n) + O(m)` → `O(n + m)`
- **Kali** untuk nested: `O(n) * O(m)` → `O(n × m)`

---

## 3. Hirarki Umum (Dari Cepat ke Lambat)

```
O(1)       < O(log n) < O(√n)   < O(n)   < O(n log n) < O(n²)    < O(n³)     < O(2ⁿ)      < O(n!)
konstan    log        akar       linier  linier-log    kuadratik  kubik      eksponensial faktorial
```

> ⚠️ **n = 10⁶**: `O(n)` ~ 1 ms, `O(n log n)` ~ 20 ms, `O(n²)` ~ 17 menit, `O(2ⁿ)` > umur alam semesta.

---

## 4. Analisis Best / Average / Worst Case

```python
def linear_search(arr, target):
    for i, x in enumerate(arr):
        if x == target:
            return i
    return -1

# Best:    Ω(1)  — target di index 0
# Average: Θ(n)  — target di tengah (asumsi uniform)
# Worst:   O(n)  — target tidak ada / di akhir
```

```python
def binary_search(arr, target):  # PREREQ: arr TERURUT
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# Best:    Ω(1)      — target di mid pertama
# Average: Θ(log n) — setengah ruang dibuang tiap iterasi
# Worst:   O(log n) — target tidak ada
```

> 💡 **Worst-case** paling penting untuk *real-time* / *safety-critical*. **Average-case** untuk *throughput* umum.

---

## 5. Strategi Algoritmik — Bandingkan Alternatif

| Strategi | Prinsip | Contoh Klasik | Kelebihan | Keterbatasan |
|----------|---------|---------------|-----------|--------------|
| **Brute Force** | Coba semua | TSP naive, substring search | Sederhana, selalu benar | Lambat (eksponensial) |
| **Divide & Conquer** | Bagi → selesaikan → gabung | Mergesort, Quicksort, Binary Search | Paralelisasi mudah, O(n log n) | Overhead rekursi, stack depth |
| **Greedy** | Pilih lokal optimal tiap langkah | Dijkstra, Huffman, Interval Scheduling | Cepat, simpel | **Tidak selalu optimal global** |
| **Dynamic Programming** | Simpan sub-solusi overlapping | Fibonacci, Knapsack, LCS, Edit Distance | Optimal untuk submasalah overlapping | Memori O(n²) sering, butuh *optimal substructure* |
| **Backtracking** | Coba & mundur (DFS + pruning) | N-Queens, Sudoku, Subset Sum | Lengkap (cari semua solusi) | Eksponensial tanpa pruning baik |
| **Randomized** | Acak untuk hindari worst-case | Quicksort randomized, Monte Carlo | Menghindari worst-case deterministik | Non-deterministik, butuh seed |

---

## 6. Sorting — Bandingkan 4 Algoritma Utama

| Algoritma | Best | Average | Worst | Ruang | Stabil? | Catatan |
|-----------|------|---------|-------|-------|---------|---------|
| **Timsort** (Python `sorted`/`list.sort`) | O(n) | O(n log n) | O(n log n) | O(n) | ✅ | Hybrid merge+insertion, adaptive untuk data *almost sorted* |
| **Quicksort** | O(n log n) | O(n log n) | **O(n²)** | O(log n) | ❌ | In-place, cache-friendly, randomized pivot hindari worst |
| **Mergesort** | O(n log n) | O(n log n) | O(n log n) | O(n) | ✅ | Stabil, cocok *linked list* & external sort |
| **Heapsort** | O(n log n) | O(n log n) | O(n log n) | O(1) | ❌ | Garansi O(n log n), tapi konstanta besar |

```python
import random, timeit

data = list(range(10000))
random.shuffle(data)

# Python built-in (Timsort) — paling cepat untuk data umum
t1 = timeit.timeit(lambda: sorted(data), number=100)

# Quicksort manual (educational)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid  = [x for x in arr if x == pivot]
    right= [x for x in arr if x > pivot]
    return quicksort(left) + mid + quicksort(right)

t2 = timeit.timeit(lambda: quicksort(data), number=100)
print(f"Timsort: {t1:.3f}s, Quicksort manual: {t2:.3f}s")
# Timsort biasanya 5-10x lebih cepat (C vs Python overhead)
```

> 💡 **Di Python: pakai `sorted()` / `list.sort()`**. Hanya implementasikan manual untuk *belajar* atau kebutuhan khusus (mis. *custom comparator* kompleks di versi lama).

---

## 7. Hashing & Dictionary — Di Balik Layar `dict`

```python
# Python dict = hash table open addressing (since 3.6: compact dict)
# Key harus hashable (immutable: int, str, tuple of immutables)
# Value bisa apa saja

# Collision handling: open addressing + probing
# Load factor ~ 2/3 → resize (amortized O(1) insert/lookup)

# Custom __hash__ & __eq__
class Siswa:
    def __init__(self, nis, nama):
        self.nis = nis
        self.nama = nama

    def __eq__(self, other):
        return isinstance(other, Siswa) and self.nis == other.nis

    def __hash__(self):
        return hash(self.nis)  # konsisten dengan __eq__

s1 = Siswa("123", "Ani")
s2 = Siswa("123", "Ani Baru")
d = {s1: "Kelas A"}
print(d[s2])  # "Kelas A" — key dianggap sama!
```

> ⚠️ **Jebakan:** `list` & `dict` **tidak hashable** → tidak bisa jadi key. Pakai `tuple` / `frozenset` / `dataclass(frozen=True)`.

---

## 8. Benchmarking Jujur di Python

```python
import timeit
import statistics

def bench(func, *args, repeat=10, number=1000):
    """Jalankan benchmark statistik."""
    times = timeit.repeat(lambda: func(*args), repeat=repeat, number=number)
    return {
        "mean": statistics.mean(times) / number * 1_000_000,  # µs per call
        "stdev": statistics.stdev(times) / number * 1_000_000 if repeat > 1 else 0,
        "min": min(times) / number * 1_000_000,
        "max": max(times) / number * 1_000_000,
    }

# Contoh: list comprehension vs loop
def via_comp(n): return [x*2 for x in range(n)]
def via_loop(n):
    res = []
    for x in range(n):
        res.append(x*2)
    return res

print(bench(via_comp, 1000))
print(bench(via_loop, 1000))
```

```python
import cProfile, pstats, io

profiler = cProfile.Profile()
profiler.enable()

# ... kode yang di-profile ...

profiler.disable()
s = io.StringIO()
ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
ps.print_stats(20)
print(s.getvalue())
```

> 💡 **`timeit`** untuk mikro-benchmark (fungsi kecil). **`cProfile`** untuk profiling program utuh — cari *hotspot*.

---

## 9. Studi Kasus: Cari Pasangan yang Jumlahnya `target`

```python
# Masalah: Diberi list int, cari 2 angka yg jumlahnya = target. Return indices.
# Asumsi: tepat 1 solusi, tidak boleh pakai elemen sama 2x.

# Strategi 1: Brute Force O(n²)
def two_sum_brute(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None

# Strategi 2: Hash Table O(n) — trade-off ruang O(n)
def two_sum_hash(arr, target):
    seen = {}  # value -> index
    for i, x in enumerate(arr):
        need = target - x
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None

# Strategi 3: Sort + Two Pointer O(n log n) — jika boleh ubah urutan / return values
def two_sum_sort(arr, target):
    indexed = sorted(enumerate(arr), key=lambda p: p[1])
    l, r = 0, len(indexed)-1
    while l < r:
        s = indexed[l][1] + indexed[r][1]
        if s == target:
            return (indexed[l][0], indexed[r][0])
        elif s < target:
            l += 1
        else:
            r -= 1
    return None
```

**Analisis Tertulis (Contoh Format CP):**

| Strategi | Waktu | Ruang | Kelebihan | Keterbatasan | Keputusan |
|----------|-------|-------|-----------|--------------|-----------|
| Brute Force | O(n²) | O(1) | Tanpa memori extra, simpel | Lambat untuk n > 10⁴ | ❌ Tolak |
| Hash Table | **O(n)** | O(n) | Paling cepas, satu pass | Butuh memori extra | ✅ **Pilih** (default) |
| Sort + Two Pointer | O(n log n) | O(n) | Tanpa hash, deterministik | Perlu sort, mengubah urutan | ✅ Alternatif jika memori kritis |

> 🏆 **Format justifikasi CP:** Tabel perbandingan → **pilih satu** → tulis alasan (efisiensi, keterbatasan, konteks).

---

## 🧪 Latihan

1. **Analisis Kompleksitas** — Tentukan best/average/worst Big-O untuk:
   - `for i in range(n): for j in range(i, n): print(i, j)`
   - `while n > 1: n //= 2`
   - Rekursif `def f(n): return 1 if n<=1 else f(n-1)+f(n-2)` (Fibonacci naive)

2. **Implementasikan Mergesort** — Versi *top-down* rekursif & *bottom-up* iteratif. Bandingkan performa vs `sorted()` untuk n=10⁵.

3. **Knapsack 0/1** — DP bottom-up `O(nW)` ruang `O(W)` (1D array). Uji dengan n=100, W=1000.

4. **Benchmark Dictionary vs List Lookup** — Buat 10⁶ item. Cari 1000 key acak. Ukur `timeit` rata-rata.

5. **Collision Demo** — Buat class dengan `__hash__` konstan (return 42). Masukkan 1000 instance ke `set`. Ukur performa vs hash bervariasi.

6. **Justifikasi Tertulis** — Persoalan: "Cari median streaming data (data datang satu-satu)". Bandingkan: (a) sort tiap kali, (b) two heaps (min-heap + max-heap), (c) Quickselect. Tulis tabel keputusan.

7. **cProfile Project** — Jalankan `python -m cProfile -o prof.bin modul13/main.py` (proyek akhir). Buka dengan `snakeviz prof.bin` atau `pstats`. Identifikasi 3 fungsi paling mahal.

---

## ✅ Checklist Paham

- [ ] Bisa hitung Big-O dari kode (loop, rekursi, nested)
- [ ] Bisa jelaskan beda O / Ω / Θ dengan contoh sendiri
- [ ] Paham kapan *greedy* gagal (contoh: coin change non-kanonik)
- [ ] Paham DP butuh *optimal substructure* + *overlapping subproblems*
- [ ] Bisa bandingkan 4 sorting utama: Timsort, Quicksort, Mergesort, Heapsort
- [ ] Tahu Python `dict` = hash table open addressing, load factor ~0.66
- [ ] Bisa bikin `__hash__` & `__eq__` konsisten untuk custom class
- [ ] Bisa pakai `timeit.repeat` + statistik untuk benchmark jujur
- [ ] Bisa pakai `cProfile` cari bottleneck program besar
- [ ] Bisa tulis **tabel justifikasi** memilih algoritma (format CP)

**Kalau semua tercentang → lanjut ke Modul 16 (Basis Data).**