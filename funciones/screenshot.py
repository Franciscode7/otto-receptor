import pyautogui
import time
import io
import base64
import sys

# Captura toda la pantalla y la guarda
def capturar_pantalla():
    # Captura la pantalla completa
    screenshot = pyautogui.screenshot()
    
    # Guardar la captura en un objeto BytesIO
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    
    # Convertir directamente a string Base64
    img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
    
    print("Captura de pantalla realizada con éxito\n")
    # --- CÁLCULO DE PESO ---
    longitud_caracteres = len(img_base64) # Cantidad de letras/caracteres
    peso_en_bytes = sys.getsizeof(img_base64) # Memoria que consume el string en RAM
    peso_en_kb = len(img_base64.encode('utf-8')) / 1024 # Peso real en KB de la cadena
    
    print(f"--- ESTADÍSTICAS DE LA CAPTURA ---")
    print(f"Caracteres del Base64: {longitud_caracteres}")
    print(f"Peso del string Base64: {peso_en_kb:.2f} KB")
    print(f"-----------------------------------")
    
    return True, img_base64

if __name__ == "__main__":
    capturar_pantalla()
    