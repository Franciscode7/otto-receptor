from AppOpener import open as app_open, close as app_close

def abrir_app(nombre):

    try:
        # match_closest=True ayuda si el nombre no es exacto
        # throw_error=True nos permite capturar el fallo en el except
        app_open(nombre.lower(), match_closest=True, throw_error=True)
        resultado = f"[APPS] Abriendo: {nombre}"
        return True, resultado
    
    except Exception as e:
        resultado = f"[ERROR] No se encontró la app '{nombre}': {e}"
        return False, resultado
