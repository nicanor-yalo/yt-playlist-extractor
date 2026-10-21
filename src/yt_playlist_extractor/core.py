# src/yt_playlist_extractor/core.py
import yt_dlp
from yt_dlp.utils import DownloadError


def extraer_links(url_playlist: str) -> list[dict]:
    """
    Extrae los enlaces y títulos de una lista de reproducción de YouTube.

    Args:
        url_playlist: URL de la lista de reproducción.

    Returns:
        Lista de diccionarios con 'titulo' y 'url' de cada video.

    Raises:
        DownloadError: si yt-dlp no puede procesar la URL.
    """
    opciones = {
        'extract_flat': 'in_playlist',
        'quiet': True,
        'no_warnings': True,
    }

    resultados = []
    with yt_dlp.YoutubeDL(opciones) as ydl:
        info = ydl.extract_info(url_playlist, download=False)
        if 'entries' in info:
            for entrada in info['entries']:
                if entrada:
                    resultados.append({
                        'titulo': entrada.get('title', 'Título no disponible'),
                        'url': f"https://www.youtube.com/watch?v={entrada.get('id')}",
                    })
    return resultados