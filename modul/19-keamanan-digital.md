# Modul 19: Keamanan Digital & Siber

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Jaringan Komputer & Internet | JKI | Konsep *cyber security*, tata kelola kontrol akses data, faktor & konfigurasi keamanan jaringan |
| Dampak Sosial Informatika | DSI | Etika digital, *white hat* vs *black hat*, privasi, regulasi (UU ITE, PDP) |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjelaskan **CIA Triad** (Confidentiality, Integrity, Availability) sebagai fondasi keamanan
- Memahami **threat modeling** (STRIDE) & *attack surface*
- Mengenal **OWASP Top 10** (web) & **MITRE ATT&CK** (framework serangan)
- Mengimplementasikan **autentikasi & otorisasi** yang aman: hashing password (`bcrypt`), JWT, MFA, RBAC/ABAC
- Mengamankan **komunikasi**: TLS/HTTPS, sertifikat, *certificate pinning*
- Memahami **keamanan jaringan**: firewall, IDS/IPS, VPN, *zero trust*, segmentasi jaringan (DMZ, VLAN)
- Melakukan **secure coding practice**: input validation, output encoding, *parameterized query*, *secrets management*
- Menjelaskan **etika hacking** (*white hat*, *bug bounty*, *responsible disclosure*) & regulasi Indonesia (UU ITE, UU PDP)

---

## 1. CIA Triad — Fondasi Keamanan

| Unsur | Definisi | Contoh Pelanggaran | Kontrol Contoh |
|-------|----------|-------------------|----------------|
| **Confidentiality** (Kerahasiaan) | Hanya pihak berwenang yang bisa akses data | Kebocoran database, *sniffing* Wi-Fi | Enkripsi (AES, TLS), ACL, *data classification* |
| **Integrity** (Integritas) | Data utuh, tidak diubah tanpa otorisasi | *Man-in-the-middle* ubah transaksi, *ransomware* enkripsi file | Hash (SHA-256), digital signature, *immutable logs*, *WORM storage* |
| **Availability** (Ketersediaan) | Sistem & data accessible saat dibutuhkan | DDoS, *ransomware*, hardware failure | Redundansi, *load balancer*, backup & DRP, *rate limiting* |

> 💡 **Triad trade-off:** Terlalu ketat *confidentiality* (mis. enkripsi semua, MFA di mana-mana) bisa mengganggu *availability*. Butuh *risk assessment* untuk keseimbangan.

---

## 2. Threat Modeling — STRIDE

| Kategori STRIDE | Deskripsi | Contoh | Mitigasi |
|-----------------|-----------|--------|----------|
| **S**poofing | Berpura-pura identitas lain | *Phishing*, *IP spoofing*, session hijack | MFA, mutual TLS, *certificate pinning* |
| **T**ampering | Mengubah data tanpa izin | *SQL injection*, *parameter manipulation*, *MITM* | Input validation, *parameterized query*, HMAC, *integrity checks* |
| **R**epudiation | Menyangkut tindakan yg dilakukan | Hapus log audit, *non-repudiation* gagal | *Audit logging* tamper-proof, digital signature |
| **I**nformation Disclosure | Bocor info sensitif | *Error message* stack trace, *directory listing*, *insecure direct object reference* (IDOR) | *Least privilege*, *error handling* generic, *output encoding* |
| **D**enial of Service | Layanan tidak tersedia | *Volumetric DDoS*, *application-layer DoS* (slowloris), *resource exhaustion* | *Rate limiting*, *WAF*, *auto-scaling*, *circuit breaker* |
| **E**levation of Privilege | Naik hak akses | *Privilege escalation* (kernel exploit, *sudo misconfig*), *broken access control* | *Principle of least privilege*, *RBAC*, *patch management* |

**Langkah Threat Modeling (Ringkas):**
1. **Gambar arsitektur** (DFD — Data Flow Diagram)
2. **Identifikasi entry points** (API, UI, port jaringan, file upload)
3. **Terapkan STRIDE** per entry point
4. **Prioritaskan** (DREAD / CVSS skor)
5. **Rancang mitigasi** → update arsitektur / kode

---

## 3. OWASP Top 10 (2021) — Ringkas

| Rank | Risiko | Inti Masalah | Pencegahan Utama |
|------|--------|--------------|------------------|
| **A01** | Broken Access Control | User akses resource user lain (IDOR) | *Deny by default*, cek otorisasi **setiap request** |
| **A02** | Cryptographic Failures | Enkripsi lemah / tidak ada (HTTP, MD5, SHA1) | TLS 1.2+, AES-GCM, bcrypt/Argon2 untuk password |
| **A03** | Injection | SQLi, NoSQLi, Command Injection, LDAPi | **Parameterized query**, ORM, input validation, *allowlist* |
| **A04** | Insecure Design | Desain fundamental tidak aman (mis. *password reset* via email tanpa token) | *Threat modeling* di fase desain, *secure design patterns* |
| **A05** | Security Misconfiguration | Default creds, directory listing, *open S3 bucket*, *debug mode on* | *Hardening checklist*, *IaC scanning*, *config as code* |
| **A06** | Vulnerable Components | Library lama ber-CVE (Log4Shell, Spring4Shell) | *SCA* (Software Composition Analysis), `pip-audit`, `dependabot` |
| **A07** | Identification & Auth Failures | *Brute force*, *credential stuffing*, *weak password policy* | MFA, *rate limit login*, *breached password check* (HaveIBeenPwned) |
| **A08** | Software & Data Integrity Failures | *CI/CD compromise*, *unsigned dependency*, *auto-update tanpa verifikasi* | *Signed artifacts*, *SBOM*, *reproducible builds* |
| **A09** | Security Logging & Monitoring Failures | Tidak log, log tidak dimonitor, *alert fatigue* | *Centralized logging* (ELK/Loki), *SIEM*, *actionable alerts* |
| **A10** | Server-Side Request Forgery (SSRF) | Server fetch URL user-controlled → akses internal metadata (AWS 169.254.169.254) | *Allowlist* URL, *deny private IP ranges*, *network segmentation* |

---

## 4. Autentikasi & Otorisasi Aman

### Hashing Password — **SELALU `bcrypt` / `argon2`**

```python
import bcrypt
# argon2: pip install argon2-cffi → argon2.PasswordHasher()

def hash_password(plain: str) -> str:
    # bcrypt default rounds=12 (bisa naikkan via bcrypt.gensalt(rounds=14))
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(plain.encode(), salt).decode()

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())
```

> ⚠️ **JANGAN** `md5`, `sha1`, `sha256` **langsung** untuk password — terlalu cepat (GPU crack miliar per detik). **JANGAN** *custom crypto*.

### JWT (JSON Web Token) — Stateless Auth

```python
import jwt
import datetime

SECRET = "ganti-dengan-env-secret-32-byte-minimum"  # dari env var!

def buat_token(user_id: str, roles: list[str]) -> str:
    payload = {
        "sub": user_id,
        "roles": roles,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verifikasi_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
```

> 💡 **JWT best practice:** `HS256` untuk internal, `RS256` (asymmetric) untuk multi-service. **Selalu** `exp` claim. Simpan *refresh token* di DB (revokable).

### RBAC vs ABAC

| Model | Prinsip | Contoh | Cocok Untuk |
|-------|---------|--------|-------------|
| **RBAC** (Role-Based) | Hak akses oleh *role* (admin, guru, siswa) | `if "admin" in user.roles: allow` | Aplikasi standar, hierarchy jelas |
| **ABAC** (Attribute-Based) | Keputusan oleh *attribute* (user.dept == resource.dept AND time < 17:00) | Kebijakan kompleks, konteks-dinamis | Enterprise besar, *zero trust* |

---

## 5. TLS / HTTPS — Enkripsi Transit

```bash
# Generate self-signed cert (dev only)
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"
```

```python
# Python HTTPS server sederhana (dev)
import http.server, ssl

server = http.server.HTTPServer(('localhost', 8443), http.server.SimpleHTTPRequestHandler)
server.socket = ssl.wrap_socket(server.socket, keyfile="key.pem", certfile="cert.pem", server_side=True)
server.serve_forever()
```

**Production:** Gunakan **Let's Encrypt** (Certbot) → gratis, auto-renew 90 hari.
```bash
sudo certbot --nginx -d example.com -d www.example.com
```

> 🔒 **TLS 1.2 minimum**, TLS 1.3 prefer. Cipher suite: `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`.

---

## 6. Keamanan Jaringan — Defense in Depth

| Lapisan | Teknologi / Praktik |
|---------|---------------------|
| **Perimeter** | Firewall (stateful), *Next-Gen Firewall* (app-aware), *WAF* (ModSecurity / Cloudflare) |
| **Network Segmentation** | **VLAN** (pisah: server, client, IoT, management), **DMZ** (public-facing), *Zero Trust* (micro-segmentation) |
| **Monitoring** | **IDS/IPS** (Suricata, Zeek), *NetFlow* analysis, *SIEM* (Elastic, Splunk, Wazuh) |
| **Remote Access** | **VPN** (WireGuard, OpenVPN) + MFA, *Zero Trust Network Access* (Tailscale, Cloudflare Tunnel) |
| **Endpoint** | *EDR* (CrowdStrike, Defender for Endpoint), *disk encryption* (BitLocker, LUKS), *auto-update* |

**Zero Trust Principles:**
1. **Verify explicitly** — selalu autentikasi & otorisasi (tidak percaya IP/internal)
2. **Least privilege** — akses minimal yang dibutuhkan
3. **Assume breach** — desain seolah sudah kompromi (segmentasi, monitoring, *blast radius* minimal)

---

## 7. Secure Coding Checklist (Python)

| Praktik | Contoh Benar | Contoh Salah |
|---------|--------------|--------------|
| **Input Validation** | `pydantic` model / `allowlist` regex | `eval(user_input)`, `exec()` |
| **SQL Injection** | `cursor.execute("SELECT * FROM users WHERE id = ?", (uid,))` | `f"SELECT * FROM users WHERE id = {uid}"` |
| **Command Injection** | `subprocess.run(["ping", "-c", "3", host], capture_output=True)` | `os.system(f"ping -c 3 {host}")` |
| **Path Traversal** | `safe_path = (BASE_DIR / user_path).resolve(); assert safe_path.is_relative_to(BASE_DIR)` | `open(user_path).read()` |
| **Secrets Management** | `os.getenv("DB_PASSWORD")` / **Vault** / **AWS Secrets Manager** | `password = "hardcoded123"` di kode / `.env` di commit |
| **Error Handling** | `except Exception: logger.exception("..."); raise` / generic user message | `except: print(traceback.format_exc())` di UI |
| **Dependencies** | `pip-audit`, `pip install --require-hashes`, `dependabot` alerts | `pip install -r requirements.txt` tanpa review CVE |

```python
# Contoh pydantic validation (FastAPI style)
from pydantic import BaseModel, EmailStr, Field

class DaftarSiswa(BaseModel):
    nis: str = Field(pattern=r"^\d{10}$")  # 10 digit
    nama: str = Field(min_length=2, max_length=100)
    email: EmailStr
    kelas_id: str = Field(pattern(r"^XI-\d$") )
```

---

## 8. Etika & Regulasi Indonesia

| Aspek | Penjelasan |
|-------|------------|
| **White Hat / Ethical Hacker** | Hacking dengan **izin tertulis** (*scope* jelas), *responsible disclosure* (lapor ke vendor, tunggu patch, baru publish) |
| **Bug Bounty** | Platform: HackerOne, Bugcrowd, YesWeHack. Bayaran per *valid vulnerability* |
| **UU ITE (No. 11/2008 + No. 1/2024)** | Pasal 27–30: konten terlarang, pencemaran nama baik, akses ilegal, penyadapan. **Sanksi pidana** |
| **UU PDP (No. 27/2022)** | Hak subjek data (akses, hapus, portabilitas), *consent*, *data controller/processor* kewajiban, *DPO*, *cross-border transfer* |
| **Sertifikasi** | **BNSP** (BNSP-014: *Cyber Security Analyst*), **CompTIA Security+**, **(ISC)² CISSP**, **EC-Council CEH** |

> 💡 **Etika guru:** Ajarkan siswa **hanya** di lingkungan *lab* terisolasi (VM, *capture the flag* platform seperti Hack The Box, TryHackMe, PicoCTF). **Tidak pernah** serang sistem tanpa izin.

---

## 9. Praktik: Hardening Checklist Mini (Server Linux)

```bash
# 1. Update & minimal install
apt update && apt upgrade -y
apt install --no-install-recommends openssh-server ufw fail2ban aide

# 2. SSH hardening (/etc/ssh/sshd_config)
# PermitRootLogin no
# PasswordAuthentication no
# PubkeyAuthentication yes
# Port 2222  # non-standard
# AllowUsers guruadmin
systemctl reload ssh

# 3. Firewall (UFW)
ufw default deny incoming
ufw default allow outgoing
ufw allow 2222/tcp   # SSH
ufw allow 80,443/tcp # HTTP/HTTPS
ufw enable

# 4. Fail2ban (SSH brute force)
# /etc/fail2ban/jail.local
# [sshd]
# enabled = true
# port = 2222
# maxretry = 3
# bantime = 1h
systemctl enable --now fail2ban

# 5. AIDE (file integrity)
aideinit
mv /var/lib/aide/aide.db.new /var/lib/aide/aide.db
# cron harian: aide --check

# 6. Auditd (audit log)
apt install auditd
auditctl -w /etc/passwd -p wa -k passwd_changes
auditctl -w /etc/shadow -p wa -k shadow_changes
```

---

## 🧪 Latihan

1. **Threat Model Mini** — Aplikasi "Rapor Online" (guru input nilai, siswa lihat rapor). Buat DFD sederhana. Terapkan STRIDE pada 3 entry point. Tulis tabel mitigasi.
2. **OWASP Demo** — Buat Flask app sederhana dengan 3 kerentanan sengaja: (a) SQLi di `/search?q=`, (b) IDOR di `/rapor/<nis>`, (c) XSS reflected di `/hello?name=`. Eksploitasi masing-masing. Lalu perbaiki.
3. **Password Hashing** — Implementasikan `register(username, password)` & `login(username, password)` pakai `bcrypt`. Tambah *rate limit* 5 percobaan per 15 menit per IP (pakai `flask-limiter` atau Redis).
4. **JWT Auth** — Buat endpoint `/login` → return JWT. Endpoint `/profile` → butuh `Authorization: Bearer <token>`. Test *expired token*, *tampered token*, *missing token*.
5. **TLS Lab** — Generate self-signed cert. Jalankan `python -m http.server` dengan SSL. Akses via `curl -k https://localhost:8443`. Periksa sertifikat dengan `openssl x509 -in cert.pem -text -noout`.
6. **Network Scan** — Di VM terisolasi: `nmap -sS -sV -O target_ip`. Identifikasi port terbuka, layanan, OS. Tulis rekomendasi *hardening* (tutup port tidak perlu, update layanan lama).
7. **Log Analysis** — Diberi `auth.log` (SSH login attempts). Pakai Python (`re` / `pandas`) ekstrak: IP paling banyak *failed login*, waktu serangan, apakah *distributed* (banyak IP) atau *single source*.
8. **Responsible Disclosure Draft** — Temukan bug (mis. *IDOR* di situs sekolah dummy). Tulis email *disclosure* ke admin: deskripsi, *steps to reproduce*, *impact*, *suggested fix*, *timeline request* (90 hari).

---

## ✅ Checklist Paham

- [ ] Bisa jelaskan CIA Triad & trade-off nya
- [ ] Bisa terapkan STRIDE pada arsitektur sederhana
- [ ] Hafal OWASP Top 10 2021 & pencegahan utamanya
- [ ] Bisa implementasikan `bcrypt` hash & verify password
- [ ] Bisa bikin & verifikasi JWT (HS256) dengan `exp` claim
- [ ] Paham beda RBAC vs ABAC & kapan pakai mana
- [ ] Bisa setup TLS/HTTPS (self-signed dev + Let's Encrypt prod)
- [ ] Paham *defense in depth*: firewall, segmentasi (VLAN/DMZ), IDS/IPS, VPN, Zero Trust
- [ ] Bisa tulis *secure code* Python: parameterized query, pydantic validation, secrets dari env
- [ ] Tahu UU ITE & UU PDP poin kunci + etika *white hat* / *bug bounty*

**Kalau semua tercentang → lanjut ke Modul 20 (Dampak Sosial TIK — Studi Kasus & Argumentasi Kritis).**