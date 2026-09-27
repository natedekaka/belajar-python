# Modul 20: Dampak Sosial TIK — Studi Kasus & Argumentasi Kritis

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Dampak Sosial Informatika | DSI | Mengkaji, menganalisis, memberikan **argumentasi & rasional kritis** pada kasus-kasus sosial terkini terkait produk TIK & sistem komputasi |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Mengidentifikasi **dampak positif & negatif** TIK pada individu, masyarakat, & lingkungan
- Menganalisis **studi kasus nyata** (algorithm bias, deepfake, privacy, digital divide, AI ethics, gig economy, dsb.)
- Menyusun **argumentasi kritis** berbasis bukti (claim → evidence → reasoning → rebuttal)
- Menulis **position paper** (1–2 halaman) & berpartisipasi **debat terstruktur**
- Memahami **kerangka etika** (IEEE, ACM, UNESCO AI Ethics) & regulasi (UU PDP, AI Act EU, EO AI AS)
- Mendesain **solusi teknologi yang bertanggung jawab** (*responsible innovation*)

---

## 1. Kerangka Analisis Dampak Sosial (PERSIA + Etika)

| Dimensi | Pertanyaan Kunci |
|---------|------------------|
| **Politik** | Siapa yang berkuasa? Apakah teknologi memperkuat / melemahkan demokrasi? (mis. *microtargeting* pemilu, sensorShip) |
| **Ekonomi** | Siapa untung/rugi? Apakah menciptakan / menghapus lapangan kerja? (gig economy, otomatisasi, *platform capitalism*) |
| **Religius/Budaya** | Bagaimana pengaruh pada nilai, norma, identitas? (memetik, *filter bubble*, budaya *cancel culture*) |
| **Sosial** | Bagaimana hubungan antar manusia? (kekkangan, *cyberbullying*, *digital parenting*, *online radicalization*) |
| **Intellektual** | Apa yang dipelajari / tidak dipelajari? (ketergantungan AI, *critical thinking* erosi, *digital literacy*) |
| **Alam/Lingkungan** | Jejak karbon? *E-waste*? *Water usage* data center? (AI training carbon footprint, *planned obsolescence*) |
| **Etika** | Adakah pelanggaran hak asasi? Bias? Diskriminasi? Transparansi? *Accountability*? |

> 💡 Gunakan **PERSIA + Etika** sebagai *checklist* saat menganalisis kasus baru.

---

## 2. Studi Kasus Terpilih (Update Tiap Tahun)

### Kasus 1: *Algorithmic Bias* — *COMPAS Recidivism Risk Score* (AS, 2016)
- **Apa:** Algoritma prediksi risiko ulang jahat digunakan pengadilan. ProPublica temukan: *false positive* 2× lebih tinggi untuk defendant Hitam vs Putih.
- **Dimensi:** Sosial (diskriminasi rasial), Politik (kepercayaan keadilan), Etika (fairness, transparency).
- **Pelan Opsi:**
  - **A.** Hapus algoritma → kembali ke hakim penuh (risiko: inkonsisten, bias manusia)
  - **B.** Perbaiki data & model (debiasing), *audit* berkala, transparan ke publik
  - **C.** Batasi pemakaian: hanya *advisory*, bukan *binding*; *human-in-the-loop* wajib
- **Argumen Pro B:** *Accountability* teknis > *opacity* manusia. Data bisa dibersihkan, model bisa diuji.
- **Argumen Kontra B:** Bias struktural di data historis sulit dihapus total. *Fairness* definisi multiple (demographic parity vs equalized odds) — *trade-off* tak terhindarkan.

### Kasus 2: *Deepfake* & *Synthetic Media* (Global, 2018–sekarang)
- **Apa:** GAN / diffusion model buat video/audio palsu hyper-realistis. Digunakan: *non-consensual porn*, *political manipulation*, *voice phishing* (CEO fraud).
- **Dimensi:** Sosial (kepercayaan erosi), Politik (disinformasi), Hukum (UU ITE Pasal 27 ayat 3), Etika (consent, *truth*).
- **Solusi Teknis:** *Watermarking* (C2PA), *detector* (Microsoft Video Authenticator), *provenance* (blockchain/ledger).
- **Solusi Non-Teknis:** *Media literacy* kurikulum, regulasi *deepfake labeling* (China, EU AI Act), *platform policy* (Meta, TikTok labeling).

### Kasus 3: *Privasi Data* — *Cambridge Analytica* (2018) & *Indonesia: PeduliLindungi / e-HAC*
- **Apa:** Data 87 juta user Facebook diambil via kuis → profil psikografis → *microtargeting* politik (Brexit, Trump 2016). Di Indonesia: aplikasi pandemi mengumpulkan data lokasi & kesehatan massal.
- **Dimensi:** Privasi (hak kontrol data), Ekonomi (*surveillance capitalism*), Hukum (UU PDP Pasal 16–18: *consent*, *purpose limitation*).
- **Pelajaran:** *Data minimization*, *purpose limitation*, *storage limitation*, *transparency* (privacy notice bahasa Indonesia baku).

### Kasus 4: *Digital Divide* — Akses & Keterampilan (Indonesia)
- **Fakta:** APJII 2023: penetrasi internet 78%, tapi *gap* perkotaan-pedesaan 30%+. Keterampilan digital rendah (PISA 2022: Indonesia ranking 69/81 *creative thinking*).
- **Dimensi:** Ekonomi (kesempatan kerja), Sosial (inklusi), Pendidikan (belajar daring pandemi).
- **Intervensi:** *Infrastruktur* (Palapa Ring, BTS 4G/5G desa), *Affordability* (paket data murah), *Literacy* (kurikulum *digital citizenship*, *coding* wajib?), *Accessibility* (disabilitas).

### Kasus 5: *AI Ethics* — *Generative AI* (ChatGPT, Midjourney, Copilot, 2022–sekarang)
- **Isu:** *Copyright* (training data tanpa izin), *Hallucination* (confidently wrong), *Job displacement* (copywriter, illustrator, junior dev), *Academic integrity* (plagiarisme AI), *Environmental* (GPT-3 training ≈ 500 tCO₂e).
- **Kerangka:** **UNESCO Recommendation on Ethics of AI (2021)** — 4 nilai: *Human rights*, *Environment*, *Diversity*, *Peace*. **EU AI Act (2024)** — *risk-based*: *unacceptable* (social scoring), *high-risk* (recruitment, medical), *limited* (chatbot), *minimal* (spam filter).
- **Posisi Guru:** Bukan *ban* AI, tapi *AI literacy*: *prompt engineering*, *verification*, *citation*, *ethical use policy* kelas.

### Kasus 6: *Gig Economy* — *Platform Worker* (Gojek, Grab, Shopee Food)
- **Isu:** *Algorithmic management* (rating, dispatch, deactivation otomatis), tidak ada *collective bargaining*, *social security* minim (BPJS Ketenagakerjaan diperluas 2023 tapi *compliance* rendah).
- **Dimensi:** Ekonomi (prekarisasi), Sosial (keamanan kerja), Hukum (PKWT vs PKWTT, *outsourcing* palsu).
- **Argumen Pro Platform:** Fleksibilitas, penghasilan tambahan, *low barrier entry*.
- **Argumen Kontra:** *Asymmetric power*, *algorithmic opacity*, *no safety net*.

---

## 3. Menyusun Argumentasi Kritis (Framework CER)

| Komponen | Penjelasan | Contoh (Kasus Deepfake) |
|----------|------------|-------------------------|
| **Claim** (Klaim) | Pernyataan yang diadvokasi | "Pemerintah wajib mewajibkan *labeling* deepfake di semua platform media sosial." |
| **Evidence** (Bukti) | Data, studi, kasus nyata, kutipan ahli | "EU AI Act Annex III klasifikasikan deepfake *high-risk*. Studi MIT 2023: label mengurangi *sharing* 40%." |
| **Reasoning** (Penalaran) | Mengapa bukti mendukung klaim | "Labeling meningkatkan *media literacy* real-time tanpa sensor. Biaya implementasi rendah (metadata C2PA)." |
| **Rebuttal** (Tangkapan) | Menjawab counter-argument | "Kontra: 'Label bisa dihapus.' Jawab: *Embedded watermark* (C2PA) tahan crop/compress. Bukti: Adobe Content Credentials." |

> 💡 **Struktur Position Paper (1–2 halaman):**
> 1. **Judul & Posisi** (1 kalimat)
> 2. **Latar Belakang & Definisi** (2–3 paragraf)
> 3. **Argumen Utama** (3 poin CER)
> 4. **Counter-argument & Rebuttal** (1–2 poin)
> 5. **Rekomendasi Kebijakan / Tindakan** (konkret, actionable)
> 6. **Referensi** (APA/IEEE style)

---

## 4. Debat Terstruktur (Format *British Parliamentary* / *Asian Parliamentary*)

| Peran | Waktu | Tugas |
|-------|-------|-------|
| **PM** (Prime Minister / Pemerintah) | 7 menit | Definisi *motion*, *framework*, 2–3 argumen utama |
| **LO** (Leader of Opposition) | 7 menit | *Rebuttal* PM + *counter-case* 2–3 argumen |
| **DPM** (Deputy PM) | 7 menit | *Rebuttal* LO + *extend* argumen PM |
| **DLO** (Deputy LO) | 7 menit | *Rebuttal* DPM + *extend* argumen LO |
| **GW** (Government Whip) | 4 menit | *Summary* + *crystallize* clashes (tidak argumen baru) |
| **OW** (Opposition Whip) | 4 menit | *Summary* + *crystallize* clashes |

**Motion Contoh:**
- "Ini Sidang berpendapat: **Pemerintah harus melarang penggunaan AI generatif untuk tugas sekolah**."
- "Ini Sidang berpendapat: **Platform gig economy wajib menyediakan BPJS Kesehatan & Ketenagakerjaan penuh untuk mitra driver**."
- "Ini Sidang berpendapat: **Hak *right to be forgotten* (hapus data pribadi) harus jadi hak konstitusional**."

---

## 5. Desain Teknologi Bertanggung Jawab (*Responsible Innovation*)

| Prinsip (AREA) | Pertanyaan Desain | Contoh Implementasi |
|----------------|-------------------|---------------------|
| **A**nticipate | Apa dampak jangka panjang (5–10 thn)? | *Scenario planning*: "Jika model ini dipakai polisi, apa risiko *false arrest*?" |
| **R**eflect | Apa asumsi & nilai kita? | Tim divers (gender, etnis, disabilitas) review desain |
| **E**ngage | Siapa *stakeholder*? Sudah dikonsultasi? | *Co-design* dengan komunitas terdampak (mis. *disabled users* untuk aksesibilitas) |
| **A**ct | Apa tindakan mitigasi konkrit? | *Bias audit* tiap 6 bln, *kill switch* fitur berisiko, *transparency dashboard* publik |

**Checklist *Responsible AI* (Ringkas):**
- [ ] **Fairness**: diuji *disparate impact* per grup terlindungi
- [ ] **Transparency**: *model card* (Google) / *datasheet for datasets* (Gebru et al.)
- [ ] **Accountability**: *human-in-the-loop* untuk keputusan *high-stakes*
- [ ] **Privacy**: *data minimization*, *federated learning* jika memungkinkan
- [ ] **Security**: *adversarial robustness* test (FGSM, PGD attack)
- [ ] **Environment**: estimasi karbon (ML CO₂ Impact Calculator), *green AI* (distillation, pruning)

---

## 6. Proyek Akhir Modul: *Position Paper* + *Debat Kelas*

**Tugas:**
1. Pilih 1 topik dari daftar (atau usulkan baru, disetujui guru):
   - *Facial recognition* di ruang publik (keamanan vs privasi)
   - *AI-generated code* (Copilot) — hak cipta & tanggung jawab bug
   - *Digital ID* (KTP digital, *single sign-on* gov) — *surveillance* vs *convenience*
   - *Content moderation* platform — *free speech* vs *harm reduction*
   - *EdTech surveillance* (proctoring AI, *keystroke logging*) — *academic integrity* vs *student privacy*
2. Tulis **Position Paper** (max 2 halaman A4, font 11, 1.5 spasi) — format CER.
3. **Debat Kelas** — berpasangan *Pro vs Contra*, 7+7+4+4 menit. Guru jadi *adjudicator*.
4. **Refleksi Individu** (200 kata): "Apa yang berubah dari pemikiran awalmu setelah riset & debat?"

**Rubrik Penilaian (100):**
| Kriteria | Bobot | Deskripsi |
|----------|-------|-----------|
| **Kedalaman Analisis** (PERSIA+Etika) | 30% | Cakupan dimensi, bukti kredibel, nuansa (bukan hitam-putih) |
| **Struktur Argumentasi** (CER) | 25% | Claim jelas, evidence relevan, reasoning logis, rebuttal tajam |
| **Kualitas Penulisan** | 15% | Bahasa baku, sitasi benar, formatting rapi |
| **Kinerja Debat** | 20% | *Rebuttal* responsif, *clash* tajam, *delivery* percaya diri |
| **Refleksi & Etika** | 10% | Jujur, *growth mindset*, sadar bias sendiri |

---

## 🧪 Latihan

1. **PERSIA Mapping** — Pilih 1 berita teknologi terbaru (kompas.teknno, The Verge, MIT Tech Review). Isi tabel PERSIA+Etika. Presentasikan 5 menit.
2. **CER Writing** — Topik: *"Sekolah wajib mengajarkan *prompt engineering* sebagai literasi dasar."* Tulis 1 halaman CER.
3. **Debat Mini** — Berkelompok 4. Motion: *"Platform wajib bayar royalti ke kreator konten yang jadi data latih AI."* 2 pro, 2 contra. 5 menit masing-masing.
4. **Model Card** — Buat *model card* sederhana untuk klasifikasi teks sentimen (dataset: SentiWordNet Indonesia). Isi: *intended use*, *training data*, *metrics per subgroup*, *limitations*, *ethical considerations*.
5. **Carbon Footprint** — Estimasi emisi CO₂ training model kecil (mis. BERT-base 1 epoch di GPU T4). Bandingkan dengan *inference* 1 juta request. Sumber: *ML CO₂ Impact Calculator* (https://mlco2.github.io/impact/).
6. **Accessibility Audit** — Pilih 1 web sekolah / e-learning. Cek WCAG 2.1 AA: kontras warna, *alt text*, *keyboard navigation*, *heading hierarchy*. Laporkan 5 temuan + perbaikan.
7. **Regulasi Mapping** — Buat tabel: UU PDP Pasal 16–23 (hak subjek data) ↔ implementasi teknis (API *data access*, *deletion*, *portability*). Contoh kode Flask endpoint `/my-data` & `/delete-me`.

---

## ✅ Checklist Paham

- [ ] Bisa gunakan **PERSIA + Etika** menganalisis kasus TIK baru
- [ ] Kenal 6 studi kasus utama (COMPAS, Deepfake, Cambridge Analytica, Digital Divide, GenAI, Gig Economy)
- [ ] Bisa menyusun **CER** (Claim–Evidence–Reasoning–Rebuttal) tertulis
- [ ] Bisa menulis **Position Paper** 1–2 halaman format baku
- [ ] Bisa berdebat terstruktur (British/Asian Parliamentary) dengan *rebuttal* & *clash*
- [ ] Kenal kerangka etika: UNESCO AI Ethics, IEEE Ethically Aligned Design, ACM Code of Ethics
- [ ] Paham prinsip **AREA** (*Anticipate, Reflect, Engage, Act*) untuk *responsible innovation*
- [ ] Bisa bikin *Model Card* / *Datasheet for Datasets* mini
- [ ] Sadar *carbon footprint* AI & *accessibility* (WCAG) sebagai tanggung jawab developer
- [ ] Bisa merujuk UU PDP & UU ITE poin relevan di argumen

**Kalau semua tercentang → Modul Fase F selesai. Lanjut ke Proyek Akhir PLB (Modul 13 upgrade) & RPS.**