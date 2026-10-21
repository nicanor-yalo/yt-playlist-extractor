# app.py
import gradio as gr
from yt_playlist_extractor.core import extraer_links


def procesar_playlist(url: str, modo: str):
    if not url or 'list=' not in url:
        return "Por favor, introduce una URL válida de una lista de reproducción."
    try:
        videos = extraer_links(url)
        if not videos:
            return "No se encontraron videos en la lista."

        if modo == "Solo títulos":
            return "\n".join(v['titulo'] for v in videos)
        elif modo == "Solo enlaces":
            return "\n".join(v['url'] for v in videos)
        else:  # "Ambos"
            # Título + TAB + URL: se copia bien y se pega ordenado en cualquier editor
            return "\n".join(f"{v['titulo']}\t{v['url']}" for v in videos)

    except Exception as e:
        return f"Ocurrió un error: {e}"


interfaz = gr.Interface(
    fn=procesar_playlist,
    inputs=[
        gr.Textbox(
            label="URL de la Lista de Reproducción de YouTube",
            placeholder="https://www.youtube.com/playlist?list=..."
        ),
        gr.Radio(
            choices=["Solo títulos", "Solo enlaces", "Ambos"],
            value="Ambos",
            label="¿Qué quieres ver?",
        ),
    ],
    outputs=gr.Textbox(
    label="Resultado (uno por línea)",
    lines=15,
    buttons=["copy"],        
),
    title="Extractor de Playlists de YouTube",
    description="Pega una playlist, elige qué ver y copia el resultado con un solo clic.",
)


if __name__ == "__main__":
    interfaz.launch()