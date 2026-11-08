"""Jalankan main.ipynb secara headless tanpa membuka Jupyter.

Contoh:
    python run.py
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT / "main.ipynb"


def main() -> int:
    try:
        import nbformat
        from nbclient import NotebookClient
    except ImportError:
        print(
            "Dependensi belum terpasang. Jalankan: python -m pip install -r requirements.txt",
            file=sys.stderr,
        )
        return 1

    if not NOTEBOOK.is_file():
        print(f"Notebook tidak ditemukan: {NOTEBOOK}", file=sys.stderr)
        return 1

    nb = nbformat.read(NOTEBOOK, as_version=4)
    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}},
        allow_errors=False,
    )

    try:
        client.execute()
    except Exception as exc:
        print(f"Eksekusi notebook gagal: {exc}", file=sys.stderr)
        return 1

    print(f"Selesai. Notebook dieksekusi: {NOTEBOOK.name}")
    print(f"Grafik & tabel diperbarui di: {ROOT / 'hasil'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
