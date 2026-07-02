import tempfile
from pathlib import Path
from file_organizer import organizar


def test_organizar_creates_folders():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "foto.jpg").write_text("test")
        (d / "doc.pdf").write_text("test")
        (d / "script.py").write_text("test")
        (d / "video.mp4").write_text("test")

        movidos = organizar(str(d))

        assert movidos == 4
        assert (d / "imagenes" / "foto.jpg").exists()
        assert (d / "documentos" / "doc.pdf").exists()
        assert (d / "codigo" / "script.py").exists()
        assert (d / "videos" / "video.mp4").exists()


def test_organizar_simular_no_mueve():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "foto.jpg").write_text("test")
        movidos = organizar(str(d), simular=True)
        assert movidos == 1
        assert not (d / "imagenes" / "foto.jpg").exists()


def test_organizar_unknown_extension():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "archivo.xyz").write_text("test")
        movidos = organizar(str(d))
        assert movidos == 1
        assert (d / "otros" / "archivo.xyz").exists()


def test_organizar_empty_directory():
    with tempfile.TemporaryDirectory() as tmp:
        movidos = organizar(str(tmp))
        assert movidos == 0


def test_organizar_hidden_files_ignored():
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / ".hidden").write_text("test")
        movidos = organizar(str(d))
        assert movidos == 0
