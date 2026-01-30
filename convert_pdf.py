#!/usr/bin/env python3
"""
Script de conversion PDF vers Word
Convertit tous les fichiers PDF du répertoire input_PDF/
et génère les fichiers Word dans output_Word/
"""

from pathlib import Path
from pdf2docx import Converter


def convert_pdf_to_docx(pdf_path: Path, output_dir: Path) -> bool:
    """Convertit un fichier PDF en DOCX."""
    docx_name = pdf_path.stem + ".docx"
    docx_path = output_dir / docx_name

    print(f"Conversion: {pdf_path.name} -> {docx_name}")

    try:
        cv = Converter(str(pdf_path))
        cv.convert(str(docx_path))
        cv.close()
        print(f"  OK: {docx_path}")
        return True
    except Exception as e:
        print(f"  ERREUR: {e}")
        return False


def main():
    script_dir = Path(__file__).parent
    input_dir = script_dir / "input_PDF"
    output_dir = script_dir / "output_word"

    # Créer les répertoires si nécessaire
    input_dir.mkdir(exist_ok=True)
    output_dir.mkdir(exist_ok=True)

    # Lister les fichiers PDF
    pdf_files = list(input_dir.glob("*.pdf")) + list(input_dir.glob("*.PDF"))

    if not pdf_files:
        print(f"Aucun fichier PDF trouvé dans {input_dir}/")
        print("Placez vos fichiers PDF dans ce répertoire et relancez le script.")
        return

    print(f"Trouvé {len(pdf_files)} fichier(s) PDF à convertir\n")

    success = 0
    failed = 0

    for pdf_file in pdf_files:
        if convert_pdf_to_docx(pdf_file, output_dir):
            success += 1
        else:
            failed += 1

    print(f"\n--- Résumé ---")
    print(f"Convertis: {success}")
    print(f"Échecs: {failed}")
    print(f"Fichiers Word disponibles dans: {output_dir}/")


if __name__ == "__main__":
    main()
