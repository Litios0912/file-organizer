# File Organizer

Organiza archivos en carpetas segun su extension.

## Instalacion

```bash
pip install file-organizer-cli
```

## Uso

```bash
# Organizar el directorio actual
file-organizer

# Organizar un directorio especifico
file-organizer ~/Downloads

# Simular (ver que se moveria sin mover nada)
file-organizer ~/Downloads --simular
```

## Categorias

- imagenes: jpg, png, gif, svg, webp, etc.
- documentos: pdf, docx, xlsx, txt, md, csv, etc.
- archivos: zip, rar, tar, gz, 7z
- videos: mp4, avi, mkv, mov
- audios: mp3, wav, ogg, flac
- programas: exe, deb, apk, dmg
- codigo: py, js, ts, java, cpp, html, css, swift, etc.
- otros: cualquier otra extension

## Publicar en PyPI

```bash
pip install build twine
python -m build
python -m twine upload dist/*
```
