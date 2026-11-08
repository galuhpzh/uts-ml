# Tugas K-Nearest Neighbors (KNN) — Iris

Implementasi algoritma KNN dari nol (NumPy) dan validasi dengan scikit-learn.
Dataset utama: **Iris** dengan `random_state = 20` (dua digit terakhir NIM).
Seluruh hasil grafik, tabel, dan angka ringkasan disimpan di folder `hasil/`.

## Struktur Proyek

```
.
├── main.ipynb          # Notebook utama (Bagian A–D)
├── run.py              # Menjalankan main.ipynb secara headless
├── requirements.txt    # Dependensi Python (versi utama dipin)
├── hasil/              # Output otomatis: PNG, CSV, results.json
├── README.md
└── AGENTS.md
```

## Prasyarat

- **Python 3.14.8** (versi acuan proyek ini)
- `pip` terbaru
- Virtual environment `.venv` di root proyek (jangan di-commit)

> Proyek ini menargetkan Python 3.14.8 pada Linux, Windows, dan macOS. Seluruh versi
> paket di `requirements.txt` sudah menyediakan wheel untuk Python 3.14.

## Setup di Linux / macOS

```bash
# 1. Buat virtual environment
python3.14 -m venv .venv

# 2. Aktifkan
source .venv/bin/activate

# 3. Perbarui pip lalu instal dependensi
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jika `python3.14` tidak ditemukan:

- macOS (Homebrew): `brew install python@3.14`
- Debian/Ubuntu: `sudo apt install python3.14 python3.14-venv`
- Fedora: `sudo dnf install python3.14`

## Setup di Windows

**PowerShell**

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jika aktivasi diblokir kebijakan eksekusi:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Command Prompt (cmd)**

```bat
py -3.14 -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jika `py -3.14` tidak tersedia, instal Python 3.14.8 dari
<https://www.python.org/downloads/windows/> dan pastikan opsi **Add python.exe to PATH** dicentang.

## Menjalankan

### Opsi 1 — headless (tanpa membuka Jupyter)

```bash
python run.py
```

`run.py` mengeksekusi `main.ipynb` secara berurutan, lalu memperbarui file di `hasil/`.
Cocok untuk verifikasi cepat atau CI.

### Opsi 2 — Jupyter

```bash
jupyter lab main.ipynb
```

atau:

```bash
jupyter notebook main.ipynb
```

Jalankan semua sel dari atas ke bawah (`Run All`). Urutan sel penting karena variabel
dan `RESULTS` didefinisikan bertahap.

## Output

Setelah eksekusi berhasil, folder `hasil/` berisi:

| File | Isi |
| --- | --- |
| `gambar1_k_vs_akurasi.png` | Grafik gabungan pengaruh K terhadap akurasi |
| `gambar2_confusion_matrix.png` | Confusion matrix data uji |
| `grid_uniform.csv` | Grid eksperimen KNN uniform |
| `grid_distance.csv` | Grid eksperimen KNN berbobot jarak |
| `results.json` | Angka ringkasan untuk laporan |

## Catatan Reproduksibilitas

- Versi paket utama di `requirements.txt` sengaja **dipin** agar hasil antar-OS konsisten.
  Jangan mengubah versi tanpa menjalankan ulang seluruh notebook.
- `RANDOM_STATE = 20` mengikuti dua digit terakhir NIM. Mengubahnya akan mengubah
  pembagian data, akurasi, dan semua angka di laporan.
- Normalisasi selalu dihitung dari data latih saja (tidak ada kebocoran data).
- File di `hasil/` dihasilkan otomatis; jangan diedit manual.

## Keamanan untuk GitHub

- `.venv/`, cache, dan file environment lokal sudah dikecualikan lewat `.gitignore`.
- Proyek ini tidak memerlukan kredensial, API key, token, atau koneksi internet saat runtime.
- Jangan menambahkan `.env` atau data sensitif ke repositori.

## Troubleshooting

| Masalah | Solusi |
| --- | --- |
| `ModuleNotFoundError` | Pastikan `.venv` aktif, lalu `python -m pip install -r requirements.txt` |
| Kernel notebook tidak ditemukan | `python -m ipykernel install --user --name python3` |
| Aktivasi PowerShell ditolak | Jalankan `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` |
| Grafik tidak muncul di server/headless | Gunakan `python run.py`; file PNG tetap tersimpan di `hasil/` |
