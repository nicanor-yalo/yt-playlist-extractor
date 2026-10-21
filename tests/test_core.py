# tests/test_core.py
import pytest
from yt_dlp.utils import DownloadError
from yt_playlist_extractor.core import extraer_links


def test_extraer_links_url_invalida():
    """Una URL truncada debe lanzar DownloadError (no tragársela)."""
    with pytest.raises(DownloadError):
        extraer_links("https://www.youtube.com/watch?v=invalido")


def test_extraer_links_input_vacio():
    """Una cadena vacía también debe fallar de forma explícita."""
    with pytest.raises(Exception):
        extraer_links("")