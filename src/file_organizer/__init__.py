#!/usr/bin/env python3
"""
File Organizer
Organiza archivos en carpetas segun su extension.
Uso: file-organizer [directorio] [--simular]
"""

import os
import shutil
from pathlib import Path

CATEGORIAS = {
    "imagenes": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "documentos": [".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx",
                   ".txt", ".md", ".csv", ".json", ".xml", ".odt", ".ods"],
    "archivos": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "audios": [".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac"],
    "programas": [".exe", ".msi", ".deb", ".rpm", ".apk", ".dmg", ".AppImage"],
    "codigo": [".py", ".js", ".ts", ".java", ".cpp", ".c", ".h", ".hpp",
               ".html", ".css", ".scss", ".swift", ".go", ".rs", ".rb", ".php",
               ".sh", ".bash", ".sql", ".yaml", ".yml", ".toml", ".ini"],
}


def organizar(directorio: str, simular: bool = False) -> int:
    """
    Organiza archivos en el directorio dado.

    Args:
        directorio: Ruta al directorio a organizar
        simular: Si es True, solo muestra lo que haria

    Returns:
        Numero de archivos organizados
    """
    directorio = Path(directorio).expanduser().resolve()
    if not directorio.exists():
        raise FileNotFoundError(f"Directorio no encontrado: {directorio}")
    if not directorio.is_dir():
        raise NotADirectoryError(f"No es un directorio: {directorio}")

    movidos = 0
    for archivo in sorted(directorio.iterdir()):
        if archivo.is_file() and not archivo.name.startswith("."):
            extension = archivo.suffix.lower()
            destino = None

            for categoria, extensiones in CATEGORIAS.items():
                if extension in extensiones:
                    destino = directorio / categoria
                    break

            if destino is None:
                destino = directorio / "otros"

            if simular:
                print(f"  [{destino.name}] {archivo.name}")
            else:
                destino.mkdir(exist_ok=True)
                shutil.move(str(archivo), str(destino / archivo.name))

            movidos += 1

    if simular:
        print(f"\nSimulacion: {movidos} archivos serian organizados")
    else:
        print(f"Organizados: {movidos} archivos")

    return movidos


def main():
    import sys
    args = sys.argv[1:]
    simular = "--simular" in args or "-s" in args
    directorio = args[0] if args and not args[0].startswith("-") else "."

    try:
        organizar(directorio, simular)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
