# B_K-1_Kelompok5 — Implementasi IPC

Tugas K-1 Sistem Operasi: demonstrasi komunikasi menggunakan socket TCP dan pipe.

## Identitas lingkungan yang diketahui
- Hostname VM: `srv-mobile-250660121033`
- Sistem operasi: Ubuntu 26.04.1 LTS
- Kernel: `7.0.0-38-generic`
- RAM VM yang dilaporkan `free -h`: total sekitar 1.6 GiB
- vCPU yang dilaporkan `nproc`: 2
- Bahasa: Python 3 (pastikan versi dengan `python3 --version`)
- Port socket: 5000
- Alamat client saat pengujian: `127.0.0.1`

## File
- `server.py`: server TCP.
- `client.py`: client TCP.
- `pipe_ipc.py`: demonstrasi `os.pipe()` dalam satu proses.
- `konfigurasi/konfigurasi-praktikum.txt`: rincian konfigurasi.

## Cara menjalankan
Jalankan server lebih dahulu di terminal pertama:
```bash
python3 server.py
```
Kemudian di terminal kedua:
```bash
python3 client.py
```
Untuk demo pipe:
```bash
python3 pipe_ipc.py
```

## Catatan pengujian
Socket menggunakan `127.0.0.1`, jadi pengujian ini dilakukan pada VM yang sama, bukan dua perangkat berbeda. `pipe_ipc.py` menunjukkan pipe di dalam satu proses Python, bukan komunikasi antardua proses terpisah. Sesuaikan laporan dengan hasil aktual pengujian kelompok.
