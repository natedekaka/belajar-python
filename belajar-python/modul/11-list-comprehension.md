# Modul 11: List Comprehension & Lambda

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menulis list comprehension untuk mengganti loop sederhana
- Menjelaskan ke murid: "ini cara Pythonic — lebih pendek, lebih jelas"
- Menggunakan `map()`, `filter()`, dan `lambda`
- Membedakan kapan pakai comprehension vs loop biasa

---

## 1. Apa Itu List Comprehension?

List comprehension (LC) adalah cara **singkat dan Pythonic** untuk membuat list baru dari iterable.

### Tanpa LC (Loop Biasa)

```python
# Buat list kuadrat dari 0-9
kuadrat = []
for i in range(10):
    kuadrat.append(i ** 2)
print(kuadrat)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Dengan LC

```python
kuadrat = [i ** 2 for i in range(10)]
print(kuadrat)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Struktur LC

```
[ekspresi  for  item  in  iterable]
    ↑        ↑     ↑       ↑
   hasil    kata   var    sumber data
   setiap   kunci          (list, range, dll)
   item
```

## 2. Contoh-Contoh LC

### Basic

```python
# Angka genap 0-20
genap = [i for i in range(0, 21, 2)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Panjang setiap kata
kata = ["Python", "Java", "C", "JavaScript"]
panjang = [len(k) for k in kata]
# [6, 4, 1, 10]

# Huruf besar
buah = ["apel", "pisang", "jeruk"]
buah_besar = [b.upper() for b in buah]
# ['APEL', 'PISANG', 'JERUK']

# Operasi matematika
suhu_c = [0, 10, 20, 30, 40]
suhu_f = [(c * 9/5) + 32 for c in suhu_c]
# [32.0, 50.0, 68.0, 86.0, 104.0]
```

### Dengan If (Filtering)

```python
# Angka genap dari 0-20
angka = range(0, 21)
genap = [a for a in angka if a % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Kata yang panjangnya > 4
kata = ["Python", "Java", "C", "JavaScript", "HTML"]
panjang = [k for k in kata if len(k) > 4]
# ['Python', 'JavaScript']

# Bilangan yang bisa dibagi 3 dan 5 (FizzBuzz)
fb = [i for i in range(1, 51) if i % 3 == 0 and i % 5 == 0]
# [15, 30, 45]
```

### Dengan If-Else (Ternary di Dalam LC)

```python
# Ganti angka genap jadi "Genap", ganjil jadi "Ganjil"
angka = range(1, 11)
label = ["Genap" if a % 2 == 0 else "Ganjil" for a in angka]
# ['Ganjil', 'Genap', 'Ganjil', 'Genap', 'Ganjil', ...]

# Nilai: lulus/tidak lulus
nilai = [85, 45, 92, 30, 78, 60]
status = ["Lulus" if n >= 75 else "Tidak lulus" for n in nilai]
# ['Lulus', 'Tidak lulus', 'Lulus', 'Tidak lulus', 'Lulus', 'Tidak lulus']
```

### Nested Loop di LC

```python
# Cartesian product
warna = ["merah", "biru"]
ukuran = ["S", "M", "L"]
produk = [(w, u) for w in warna for u in ukuran]
# [('merah', 'S'), ('merah', 'M'), ('merah', 'L'),
#  ('biru', 'S'), ('biru', 'M'), ('biru', 'L')]

# Flatten matriks
matriks = [[1, 2], [3, 4], [5, 6]]
flat = [item for baris in matriks for item in baris]
# [1, 2, 3, 4, 5, 6]
```

## 3. Dictionary & Set Comprehension

Bukan cuma list — Python juga punya dictionary comprehension dan set comprehension.

### Dictionary Comprehension

```python
# Kuadrat sebagai value
angka = [1, 2, 3, 4, 5]
kuadrat_dict = {a: a**2 for a in angka}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Dari dua list jadi dict
nama = ["Budi", "Ani", "Citra"]
nilai = [85, 92, 78]
nilai_dict = {nama[i]: nilai[i] for i in range(len(nama))}
# {'Budi': 85, 'Ani': 92, 'Citra': 78}

# Filter dict
siswa_aktif = {k: v for k, v in nilai_dict.items() if v >= 80}
# {'Budi': 85, 'Ani': 92}
```

### Set Comprehension

```python
# Kuadrat angka — duplikat otomatis hilang
angka = [1, 2, 2, 3, 3, 3, 4]
kuadrat_set = {a**2 for a in angka}
# {16, 1, 9, 4}

# Huruf unik dalam kalimat
kalimat = "Python Programming"
huruf_unik = {h.lower() for h in kalimat if h.isalpha()}
# {'p', 'y', 't', 'h', 'o', 'n', 'r', 'g', 'a', 'm', 'i'}
```

## 4. Lambda Function

Lambda = **fungsi anonim (tanpa nama)** satu baris.

### Bentuk Umum

```python
# lambda parameter: ekspresi

# Fungsi biasa
def kali_dua(x):
    return x * 2

# Lambda
kali_dua_lambda = lambda x: x * 2

print(kali_dua(5))        # 10
print(kali_dua_lambda(5)) # 10
```

### Lambda dengan Banyak Parameter

```python
tambah = lambda a, b: a + b
print(tambah(5, 3))  # 8

luas_segitiga = lambda a, t: 0.5 * a * t
print(luas_segitiga(10, 5))  # 25.0
```

## 5. Map, Filter, Reduce

Fungsi-fungsi ini sering dipasangkan dengan lambda.

### Map — Terapkan Fungsi ke Setiap Item

```python
angka = [1, 2, 3, 4, 5]

# Pakai map + lambda
kuadrat = list(map(lambda x: x**2, angka))
print(kuadrat)  # [1, 4, 9, 16, 25]

# Sebenarnya LC lebih bersih:
kuadrat2 = [x**2 for x in angka]
```

### Filter — Ambil Item yang Memenuhi Kondisi

```python
angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Pakai filter + lambda
genap = list(filter(lambda x: x % 2 == 0, angka))
print(genap)  # [2, 4, 6, 8, 10]

# LC lebih bersih:
genap2 = [x for x in angka if x % 2 == 0]
```

### Reduce — Akumulasi Nilai

```python
from functools import reduce

angka = [1, 2, 3, 4, 5]

# Jumlah semua — reduce bertahap: (((1+2)+3)+4)+5
jumlah = reduce(lambda a, b: a + b, angka)
print(jumlah)  # 15

# Faktorial dengan reduce
faktorial = reduce(lambda a, b: a * b, range(1, 6))
print(faktorial)  # 120 (1*2*3*4*5)
```

### Kapan Map/Filter vs List Comprehension?

```python
# ✅ LC lebih Pythonic untuk kasus sederhana
[x**2 for x in range(10)]

# ✅ Map/Filter berguna kalau sudah punya fungsi yang ada
list(map(str.upper, ["a", "b", "c"]))
# Sama dengan: [s.upper() for s in ["a", "b", "c"]]
```

> 💡 **Saran:** Gunakan list comprehension dulu. Map/filter untuk kasus khusus (misal fungsi sudah ada).

## 6. Kapan Pakai Comprehension vs Loop Biasa?

| Situasi | Pakai |
|---------|-------|
| Membuat list baru dari iterable | ✅ Comprehension |
| Transformasi sederhana (kuadrat, upper) | ✅ Comprehension |
| Filter + transformasi | ✅ Comprehension dengan if |
| Operasi sampingan (print, file.write) | ❌ Loop biasa |
| Logika kompleks (banyak if, try/except) | ❌ Loop biasa |
| Perlu break/continue | ❌ Loop biasa |

```python
# ✅ Comprehension — tepat
genap = [x for x in range(100) if x % 2 == 0]

# ❌ Comprehension — dipaksakan (ada side-effect)
# [print(x) for x in range(10)]  # Bisa jalan, tapi ini abuse!

# ✅ Loop biasa — lebih tepat
for x in range(10):
    print(x)
```

---

## 🧪 Latihan Modul 11

### Latihan 1: Transformasi dengan LC

```python
# Selesaikan dengan list comprehension:

# 1. Buat list bilangan kuadrat dari 1-20
# 2. Buat list kata "Genap" atau "Ganjil" untuk angka 0-15
# 3. Dari list suhu_c = [0, 5, 10, 15, 20, 25, 30], buat list suhu_f
# 4. Ambil kata yang mengandung huruf 'a' dari: ["apel", "jeruk", "mangga", "pisang", "anggur"]
# 5. Buat list tuple (angka, kuadratnya) untuk 1-10
```

### Latihan 2: Filter dengan LC

```python
nilai_siswa = [("Budi", 85), ("Ani", 92), ("Citra", 45), ("Dedi", 78), ("Eva", 30)]

# 1. Nama siswa yang lulus (nilai >= 75)
# 2. Nama + status lulus/tidak
# 3. Rata-rata nilai dari siswa yang lulus saja
```

### Latihan 3: Dictionary Comprehension

```python
kata = ["Python", "Java", "C", "JavaScript", "HTML", "CSS"]

# Buat dictionary: {kata: panjang_kata}
# Filter: hanya kata dengan panjang > 2
# Output: {'Python': 6, 'Java': 4, 'JavaScript': 10, 'HTML': 4, 'CSS': 3}
```

### Latihan 4: Lambda + Map/Filter

```python
# 1. Gunakan map untuk mengubah list suhu Celsius ke Fahrenheit
# 2. Gunakan filter untuk ambil bilangan prima dari 2-50
#    (bikin fungsi is_prime dulu, lalu filter)
# 3. Gunakan reduce untuk mencari nilai terbesar di list
```

### Latihan 5: Challenge — FizzBuzz dengan LC

```python
# Buat FizzBuzz (1-50) dengan list comprehension
# Output: [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", ...]
# Hint: pakai ternary di dalam LC
```

---

## ✅ Checklist Paham

- [ ] Saya bisa nulis list comprehension `[expr for item in iterable]`
- [ ] Saya bisa nambah filter `[expr for item in iterable if condition]`
- [ ] Saya paham ternary di dalam LC
- [ ] Saya bisa bikin dictionary & set comprehension
- [ ] Saya bisa bikin lambda sederhana
- [ ] Saya paham `map()`, `filter()`, `reduce()`
- [ ] Saya tau kapan pakai LC vs loop biasa

**Kalau semua checklist tercentang → lanjut ke Modul 12.**
