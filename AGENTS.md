# AGENTS.md

## Gambaran repositori
- Tugas kuliah: implementasi KNN dari nol (NumPy) + validasi scikit-learn pada dataset Iris.
- `main.ipynb` adalah sumber kebenaran. `run.py` mengeksekusinya secara headless. `hasil/` berisi artefak yang dihasilkan.
- Tidak ada test, lint, typecheck, atau CI yang dikonfigurasi.

## Lingkungan
- Target **Python 3.14.8**; gunakan `.venv` di root repo (diabaikan Git).
- Linux/macOS: `python3.14 -m venv .venv && source .venv/bin/activate`
- Windows: `py -3.14 -m venv .venv` lalu `.\.venv\Scripts\Activate.ps1`
- Instalasi: `python -m pip install --upgrade pip && python -m pip install -r requirements.txt`
- Versi paket utama di `requirements.txt` sengaja dipin; `jupyter` tidak dipin. Jangan naikkan versi tanpa diminta karena hasil dan grafik bergantung pada versi tersebut. Semua paket yang dipin sudah punya wheel untuk Python 3.14.

## Menjalankan / verifikasi
- Verifikasi penuh: `python run.py` (menjalankan `main.ipynb` lewat nbclient dengan cwd = root repo, memperbarui `hasil/`).
- Interaktif: `jupyter lab main.ipynb` (atau `jupyter notebook main.ipynb`).
- Tidak ada unit test. Verifikasi = `python run.py` yang bersih; notebook berisi assertion (mis. cek studi kasus manual) dan menulis `hasil/results.json`.

## Jebakan khusus repo ini
- Sel notebook bergantung urutan: `RESULTS`, scaler, dan grid eksperimen didefinisikan bertahap. Jangan ubah urutan atau memecah sel.
- `RANDOM_STATE = 20` mengikuti dua digit terakhir NIM (berakhiran 0). Mengubahnya akan mengubah split, fold CV, akurasi, dan semua angka yang dilaporkan.
- Bagian A **tidak boleh** memakai `sklearn.neighbors`; sklearn hanya untuk validasi di Bagian B.
- Semua file yang dihasilkan masuk ke `hasil/`. Itu output, bukan sumber; jangan diedit manual.
- Pertahankan prosa dan komentar notebook dalam bahasa Indonesia sesuai tugas.
- `run.py` membutuhkan `nbclient`, `nbconvert`, dan `ipykernel` (disediakan oleh paket `jupyter`) serta memakai nama kernel `python3`.
- Tidak ada kredensial/rahasia. Jaga tetap demikian sebelum push ke GitHub; `.venv/` dan `.env*` diabaikan.
