import webbrowser

def abrir_enlace(url):

    try:
        # Verificamos si la URL empieza con http, si no, se lo agregamos
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        
        # webbrowser.open devuelve True si se lanzó con éxito
        exito = webbrowser.open(url)
        
        if exito:
            resultado = f"Navegador abierto en: {url}"
            return True, resultado
        else:
            resultado = f"No se pudo abrir el navegador o el url es invalido."
            return False, resultado
            
    except Exception as e:
        resultado = f"[EXCEPCIÓN] Error en navegador.py: {e}"
        return False, resultado