# Modul 18: Jaringan Komputer & Model OSI

## 📌 Pemetaan CP Fase F
| Elemen | Kode CP | Capaian Terkait |
|--------|---------|-----------------|
| Jaringan Komputer & Internet | JKI | Memahami konsep lanjutan: topologi, aspek teknis jaringan, **OSI Layer**, komponen jaringan, mekanisme pertukaran data |

---

## 🏆 Target Pemahaman

Setelah modul ini, kamu bisa:
- Menjelaskan **7 Layer Model OSI** (fungsi, protokol, PDU, perangkat per layer)
- Membandingkan **OSI vs TCP/IP Model** (4 layer)
- Mengidentifikasi **topologi jaringan** (star, mesh, bus, ring, hybrid) — kelebihan/kekurangan
- Memahami **addressing**: MAC (Layer 2), IP (Layer 3), Port (Layer 4)
- Menjelaskan **encapsulation & decapsulation** (PDU berubah per layer)
- Memahami **TCP vs UDP** (three-way handshake, flow control, congestion control)
- Praktik **socket programming** dasar Python (`socket` module)
- Menganalisis *packet capture* sederhana (Wireshark / `scapy`)

---

## 1. Kenapa Model Layer?

Jaringan kompleks → **pecah jadi lapisan** (layer) yang masing-masing punya tanggung jawab tunggal.

| Prinsip | Penjelasan |
|---------|------------|
| **Abstraksi** | Layer atas tidak peduli detail layer bawah |
| **Standardisasi** | Vendor beda tetap bisa interoperabel (mis. TCP/IP) |
| **Troubleshooting** | Isolasi masalah per layer (cable → IP → port → app) |
| **Modularitas** | Ganti protokol satu layer tanpa hancurkan yang lain |

---

## 2. 7 Layer OSI — Dari Bawah ke Atas

| Layer | Nama | Fungsi Utama | PDU (Protocol Data Unit) | Protokol / Standar | Perangkat |
|-------|------|--------------|--------------------------|-------------------|-----------|
| **7** | **Application** | Interface user ↔ jaringan (HTTP, DNS, SMTP, FTP, SSH) | **Data** | HTTP, DNS, SMTP, FTP, SSH, DHCP | — |
| **6** | **Presentation** | Translasi, enkripsi, kompresi (SSL/TLS, JPEG, ASCII) | **Data** | TLS/SSL, MIME, ASCII, JPEG, MPEG | — |
| **5** | **Session** | Manajemen dialog, sinkronisasi, checkpoint | **Data** | NetBIOS, RPC, PPTP, SIP | — |
| **4** | **Transport** | End-to-end delivery, segmentasi, flow/error control | **Segment** (TCP) / **Datagram** (UDP) | **TCP**, **UDP**, SCTP | — |
| **3** | **Network** | Routing, logical addressing (IP), fragmentasi | **Packet** | **IPv4**, **IPv6**, ICMP, OSPF, BGP | **Router**, Layer-3 Switch |
| **2** | **Data Link** | Framing, MAC addressing, error detection, akses media | **Frame** | Ethernet (802.3), Wi-Fi (802.11), PPP, Switch | **Switch**, Bridge, NIC |
| **1** | **Physical** | Bit transmission: kabel, sinyal, voltage, pinout | **Bit** | Copper (Cat5e/6/6a), Fiber, Radio | **Hub**, Repeater, Kabel, Konektor |

> 💡 **Mnemonic:** **"All People Seem To Need Data Processing"** (Application → Physical)

---

## 3. OSI vs TCP/IP Model (4 Layer)

| OSI (7 Layer) | TCP/IP (4 Layer) | Catatan |
|---------------|------------------|---------|
| Application | Application | Gabung L5+L6+L7 |
| Presentation |  |  |
| Session |  |  |
| Transport | Transport | Sama (TCP/UDP) |
| Network | Internet | IP + routing |
| Data Link | Network Access / Link | Ethernet + Physical |
| Physical |  |  |

> 💡 **Dunia nyata pakai TCP/IP model.** OSI dipakai untuk *pembelajaran & troubleshooting* konseptual.

---

## 4. Topologi Jaringan

| Topologi | Deskripsi | Kelebihan | Kekurangan | Contoh Penggunaan |
|----------|-----------|-----------|------------|-------------------|
| **Star** | Semua node ke switch pusat | Mudah manajemen, isolasi gangguan | Titik gagal tunggal (switch) | **Kantor, sekolah, rumah** (paling umum) |
| **Mesh** | Setiap node ke semua node | Redundansi tinggi, toleran gagal | Kabel & port sangat banyak | Backbone ISP, data center kritis |
| **Bus** | Satu kabel backbone (coaxial) | Sederhana, murah | Kolisi tinggi, susah troubleshoot | Legacy (10BASE2), tidak dipakai lagi |
| **Ring** | Lingkaran, token passing | Deterministik, tidak kolisi | Satu putus → jaringan mati | Token Ring (legacy), Metro Ethernet (ring protection) |
| **Hybrid** | Kombinasi (mis. star-mesh) | Fleksibel, skalabil | Desain kompleks | Enterprise besar, campus |

---

## 5. Addressing — 3 Identitas Utama

| Layer | Alamat | Panjang | Contoh | Cakupan |
|-------|--------|---------|--------|---------|
| **2 (Data Link)** | **MAC Address** | 48 bit (6 byte) | `00:1A:2B:3C:4D:5E` | **Local segment** (broadcast domain) — tidak lewat router |
| **3 (Network)** | **IP Address** | IPv4: 32 bit, IPv6: 128 bit | `192.168.1.10` / `2001:db8::1` | **Global / internetwork** — lewat router |
| **4 (Transport)** | **Port Number** | 16 bit (0–65535) | `80` (HTTP), `443` (HTTPS), `53` (DNS) | **Proses/aplikasi** di host |

**Well-known ports (0–1023):** butuh root/admin. **Registered (1024–49151)**, **Ephemeral (49152–65535)** — client random.

---

## 6. Encapsulation & Decapsulation (Proses Kirim & Terima)

```
KIRIM (Sender)                              TERIMA (Receiver)
┌─────────────────────────────────────┐     ┌─────────────────────────────────────┐
│ Application Data                    │     │ Frame → cek FCS → strip header/trailer│
│   ↓ (add App header)                │     │   ↓                                 │
│ Presentation Data                   │     │ Packet → cek IP → strip IP header    │
│   ↓ (add Presentation header)       │     │   ↓                                 │
│ Session Data                        │     │ Segment → reorder, ACK → strip TCP   │
│   ↓ (add Session header)            │     │   ↓                                 │
│ Transport Segment (TCP/UDP header)  │     │ Data → kirim ke Application          │
│   ↓ (add Transport header)          │     │                                     │
│ Network Packet (IP header)          │     │                                     │
│   ↓ (add Network header)            │     │                                     │
│ Data Link Frame (MAC header+trailer)│     │                                     │
│   ↓ (add Physical preamble)         │     │                                     │
│ Physical Bits (signal)  ──────────► │     │                                     │
└─────────────────────────────────────┘     └─────────────────────────────────────┘
```

**PDU per layer:** Data → Segment → Packet → Frame → Bits

---

## 7. TCP vs UDP — Perbandingan Lengkap

| Fitur | **TCP** (Transmission Control Protocol) | **UDP** (User Datagram Protocol) |
|-------|-----------------------------------------|----------------------------------|
| **Koneksi** | Connection-oriented (3-way handshake) | Connectionless |
| **Keandalan** | **Garansi** delivery, urutan, tanpa duplikat | **Tidak** garansi (best-effort) |
| **Flow Control** | Sliding window (receiver-driven) | Tidak ada |
| **Congestion Control** | Tahoe/Reno/CUBIC (slow start, AIMD) | Tidak ada |
| **Header Size** | 20–60 byte | 8 byte |
| **Latency** | Lebih tinggi (handshake, ACK) | **Rendah** (fire-and-forget) |
| **Use Case** | Web (HTTP/HTTPS), Email, SSH, FTP | DNS, Streaming, VoIP, Gaming, DHCP, SNMP |

### TCP Three-Way Handshake
```
Client                          Server
  │                                │
  ├─ SYN (seq=x) ────────────────► │
  │                                │
  │ ◄──────── SYN-ACK (seq=y, ack=x+1) │
  │                                │
  ├─ ACK (ack=y+1) ──────────────► │
  │                                │
  └─ Established ── Data transfer ──►
```

### TCP State Diagram (Ringkas)
```
CLOSED → SYN_SENT → SYN_RCVD → ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED
                │                                    │
                ▼                                    ▼
            LISTEN                              CLOSE_WAIT → LAST_ACK → CLOSED
```

---

## 8. Socket Programming Dasar Python

```python
# TCP Server (Echo)
import socket
import threading

def handle_client(conn, addr):
    print(f"[+] Connected: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)  # echo back
    print(f"[-] Disconnected: {addr}")

def tcp_server(host="0.0.0.0", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

# TCP Client
def tcp_client(host="127.0.0.1", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Halo server!")
        resp = s.recv(1024)
        print(f"Server reply: {resp.decode()}")
```

```python
# UDP Server
import socket

def udp_server(host="0.0.0.0", port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"UDP Server on {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            print(f"From {addr}: {data.decode()}")
            s.sendto(b"ACK: " + data, addr)

# UDP Client
def udp_client(host="127.0.0.1", port=5001):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(b"Halo UDP", (host, port))
        resp, _ = s.recvfrom(1024)
        print(f"Reply: {resp.decode()}")
```

> ⚠️ **TCP:** `SOCK_STREAM`, butuh `listen()`/`accept()`, *stream* byte (bisa *fragmented* — pakai delimiter / length prefix).
> **UDP:** `SOCK_DGRAM`, *datagram* (message boundary terjaga), tidak butuh koneksi.

---

## 9. Analisis Paket dengan `scapy` (Opsional)

```bash
pip install scapy
```

```python
from scapy.all import sniff, IP, TCP, UDP, DNS, Raw

def analisis_paket(pkt):
    if IP in pkt:
        ip = pkt[IP]
        print(f"IP {ip.src} → {ip.dst} | Proto: {ip.proto}", end=" ")
        if TCP in pkt:
            tcp = pkt[TCP]
            print(f"TCP {tcp.sport}→{tcp.dport} Flags: {tcp.flags}")
        elif UDP in pkt:
            udp = pkt[UDP]
            print(f"UDP {udp.sport}→{udp.dport}", end=" ")
            if DNS in pkt:
                dns = pkt[DNS]
                if dns.qr == 0:  # query
                    print(f"DNS Query: {dns.qd.qname.decode()}")
                else:
                    print(f"DNS Answer: {dns.an.rdata if dns.an else 'N/A'}")
        print()

# Jalankan (butuh root/admin untuk mode promiscuous)
# sniff(prn=analisis_paket, filter="tcp or udp", count=10)
```

---

## 10. Troubleshooting Layered (Checklist Cepat)

| Gejala | Layer Terduga | Cek Cepat |
|--------|---------------|-----------|
| Tidak bisa ping ke IP lain | 1 (kabel), 2 (switch), 3 (IP/gateway) | `ip link`, `ip addr`, `ping gateway`, `traceroute` |
| Bisa ping IP, tapi tidak bisa browsing | 7 (DNS), 4 (port 80/443 firewall) | `dig google.com`, `curl -I http://ip`, `telnet ip 80` |
| Koneksi putus-putus (Wi-Fi) | 1 (sinyal), 2 (channel overlap) | `iwconfig`, `nmcli dev wifi list` |
| Transfer file lambat | 4 (TCP window), 1 (kabel/port) | `iperf3`, cek duplex mismatch (`ethtool`) |
| Bisa SSH tapi tidak bisa akses web server | 4 (port 80/443 block), 7 (web server down) | `systemctl status nginx`, `ss -tlnp | grep :80` |

---

## 🧪 Latihan

1. **Diagram OSI** — Gambar 7 layer OSI dengan PDU, protokol, & perangkat per layer. Jelaskan encapsulation 1 paket HTTP request.
2. **Topologi Desain** — Sekolah 3 gedung (A, B, C). Gedung A = server & internet gateway. Desain topologi (gambar + justifikasi). Hitung kebutuhan switch & kabel.
3. **Subnetting** — Network `192.168.10.0/24`. Bagi jadi 4 subnet untuk 4 lab komputer (maks 30 host per lab). Tuliskan: network address, broadcast, usable range, subnet mask.
4. **Socket Chat Mini** — Buat chat room sederhana: 1 server TCP broadcast ke semua client. Client bisa kirim & terima pesan real-time (threading).
5. **UDP Time Sync** — Client request time ke server UDP. Server balik timestamp (ISO format). Ukur *round-trip time* rata-rata 10 request.
6. **Packet Capture** — Jalankan `python -m http.server 8000`. Buka browser ke `http://localhost:8000`. Capture dengan Wireshark / `scapy`. Identifikasi: TCP handshake, HTTP GET, HTTP Response, TCP teardown.
7. **Firewall Rule** — Tuliskan `iptables` / `nftables` rule: allow SSH (22) dari subnet `192.168.10.0/24` saja, drop yang lain. Allow HTTP/HTTPS dari mana saja.

---

## ✅ Checklist Paham

- [ ] Bisa sebut 7 layer OSI urut + fungsi + PDU + protokol contoh
- [ ] Bisa bandingkan OSI vs TCP/IP model
- [ ] Bisa jelaskan topologi star/mesh/bus/ring + pros/cons
- [ ] Paham perbedaan MAC / IP / Port — layer & cakupan masing-masing
- [ ] Bisa jelaskan encapsulation (kirim) & decapsulation (terima)
- [ ] Bisa bandingkan TCP vs UDP tabel + use case
- [ ] Bisa gambar TCP 3-way handshake & state diagram
- [ ] Bisa tulis TCP & UDP server/client dasar Python `socket`
- [ ] Bisa baca `scapy` output / Wireshark capture dasar
- [ ] Bisa troubleshooting layered (cek layer 1 → 7 berurutan)

**Kalau semua tercentang → lanjut ke Modul 19 (Keamanan Digital & Siber).**