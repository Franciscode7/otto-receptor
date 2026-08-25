from yt_dlp import YoutubeDL
import webbrowser

def buscar_youtube(nombre_cancion: str) -> dict | None:
    """
    Busca una canción en YouTube y devuelve el título y el enlace del primer resultado.
    """
    # Configuración para extraer solo la información sin descargar el video
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch1',  # Busca y devuelve solo 1 resultado
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            # Realizamos la búsqueda
            info = ydl.extract_info(f"ytsearch1:{nombre_cancion}", download=False)
            
            if 'entries' in info and len(info['entries']) > 0:
                video = info['entries'][0]
                titulo = video.get('title')
                url = video.get('webpage_url')
                if titulo and url:
                    webbrowser.open(url)
                    return True, titulo
    except Exception as e:
        print(f"Error al realizar la búsqueda: {e}")
        return None

    return None

# --- Ejemplo de uso ---
if __name__ == "__main__":
    busqueda = "made you love me ariana grande"
    resultado = buscar_youtube(busqueda)

    if resultado:
        print("🎵 Canción encontrada:")
        print(f"Título: {resultado['titulo']}")
        print(f"URL: {resultado['url']}")
    else:
        print("No se encontraron resultados.")