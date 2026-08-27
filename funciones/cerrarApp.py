import psutil
from AppOpener import close as app_close

def cerrar_app(nombre):
    nombre = nombre.lower()
    try:
        # PLAN A: Intentar cierre limpio con AppOpener
        app_close(nombre, match_closest=True, throw_error=True)
        resultado = f"App cerrada correctamente: {nombre}"
        
        return True, resultado
    
    except:
        # PLAN B: Cierre forzado buscando en los procesos del sistema
        print(f"[APPS] AppOpener falló, intentando cierre forzado para: {nombre}")
        encontrado = False
        for proc in psutil.process_iter(['name']):
            try:
                # Comprobamos si el nombre de la app está en el nombre del proceso
                # Ej: si buscas "excel", encontrará "EXCEL.EXE"
                if nombre in proc.info['name'].lower():
                    proc.kill()
                    encontrado = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        if encontrado:
            resultado = f"[APPS] Proceso {nombre} terminado por la fuerza."
            return True, resultado
        
        else:
            resultado = f"[ERROR] No se encontró ningún proceso con el nombre: {nombre}"
            return False, resultado