# File Organizer

Paquete Python para organizar archivos en carpetas segun su extension. Instalable via pip.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![PyPI](https://img.shields.io/badge/PyPI-file--organizer--cli-yellow?logo=pypi)](https://pypi.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![CLI](https://img.shields.io/badge/CLI-ready-7C3AED)]()

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

El comando crea carpetas por categoria y mueve los archivos automaticamente.

## Categorias soportadas

| Categoria | Extensiones |
|---|---|
| imagenes | jpg, jpeg, png, gif, bmp, svg, webp, ico |
| documentos | pdf, doc, docx, xls, xlsx, ppt, pptx, txt, md, csv, json, xml, odt, ods |
| archivos | zip, rar, tar, gz, 7z, bz2 |
| videos | mp4, avi, mkv, mov, wmv, flv, webm |
| audios | mp3, wav, ogg, flac, m4a, aac |
| programas | exe, msi, deb, rpm, apk, dmg, AppImage |
| codigo | py, js, ts, java, cpp, c, h, hpp, html, css, scss, swift, go, rs, rb, php, sh, bash, sql, yaml, yml, toml, ini |
| otros | Cualquier extension no listada |

## Uso como libreria

```python
from file_organizer import organizar

# Organizar Downloads
organizar("~/Downloads")

# Simulacion
organizar("~/Downloads", simular=True)
```

## Desarrollo

```bash
git clone https://github.com/Litios0912/file-organizer.git
cd file-organizer
pip install -e .
file-organizer ~/Downloads --simular
```

## Publicar en PyPI

```bash
pip install build twine
python -m build
python -m twine upload dist/*
```

## Licencia

MIT
