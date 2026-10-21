# YT Playlist Extractor (Gradio Web UI)

Herramienta para extraer los títulos y enlaces de los videos de una lista de
reproducción pública de **YouTube**. Interfaz web minimalista con Gradio: pegas la
URL de la playlist, eliges qué quieres ver (títulos, enlaces o ambos) y copias
el resultado con un *clic*.

## Origen del Proyecto
Esta herramienta **nació de una necesidad real: el fastidio de copiar y pegar enlaces uno por uno para entrenar o alimentar Gemini Notebooks y otros LLMs**. En lugar de perder tiempo en tareas repetitivas, este extractor automatiza el proceso en segundos. Pegas la **URL de la playlist**, eliges qué formato necesitas (títulos, enlaces o ambos) y copias todo el resultado al portapapeles de inmediato.
## Requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (gestor de paquetes y entornos)

## Instalación

```bash
git clone https://github.com/nicanor-yalo/yt-playlist-extractor.git
cd yt-playlist-extractor
uv sync
```

## Uso

```bash
uv run python app.py
```
Se abre una interfaz en `http://127.0.0.1:7860`. Pega la URL de una playlist
(`https://www.youtube.com/playlist?list=...`), elige el formato de salida y
copia el resultado con el botón de copiar.
## Uso desde Python

```bash
from yt_playlist_extractor.core import extraer_links

videos = extraer_links("https://www.youtube.com/playlist?list=...")
for v in videos:
    print(v["titulo"], v["url"])
```
## Tests

```bash
uv run pytest -v
```
## Notas

* Solo funciona con playlists públicas (o no listadas) de YouTube.

* `extraer_links()` propaga `DownloadError` si la URL es inválida; la interfaz
captura ese error y muestra un mensaje al usuario.

* No descarga videos ni audio: solo extrae metadatos (título + URL).