# app.py
import gradio as gr
from yt_playlist_extractor.core import extraer_links

def procesar_playlist(url: str):
    """Función que conecta la interfaz con la lógica de extracción."""
    if not url or 'youtube.com/playlist' not in url:
        return "Por favor, introduce una URL válida de una lista de reproducción."
    try:
        resultados = extraer_links(url)
        if not resultados:
            return "No se encontraron videos en la lista."
        # Devuelve una lista de listas para que Gradio lo muestre como tabla
        return [[r['titulo'], r['url']] for r in resultados]
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Crear la interfaz de Gradio
interfaz = gr.Interface(
    fn=procesar_playlist,
    inputs=gr.Textbox(
        label="URL de la Lista de Reproducción de YouTube",
        placeholder="https://www.youtube.com/playlist?list=..."
    ),
    outputs=gr.Dataframe(
        headers=["Título del Video", "URL"],
        label="Resultados"
    ),
    title="Extractor de Enlaces de YouTube",
    description="Pega la URL de una lista de reproducción para obtener los enlaces de sus videos."
)

if __name__ == "__main__":
    interfaz.launch()