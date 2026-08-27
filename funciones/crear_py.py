import os
import json
import re
from datetime import datetime


# Definición de rutas base
disco = r"D:\developer"
carpeta_proyecto = "propuestas_otto"
directorio_destino = os.path.join(disco, carpeta_proyecto)

def obtener_nombre_dinamico(codigo):
    # 1. Busca clases: 'class NombreClase'
    match_clase = re.search(r"class\s+([A-Za-z0-9_]+)", codigo)
    if match_clase:
        return f"{match_clase.group(1).lower()}.py"

    # 2. Busca funciones: 'def nombre_funcion'
    match_def = re.search(r"def\s+([A-Za-z0-9_]+)", codigo)
    if match_def:
        return f"{match_def.group(1)}.py"

    # 3. Respaldo por fecha/hora si es un script plano sin funciones ni clases
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombrescript =  f"script_{timestamp}.py"
    
    return nombrescript


def crear_python(codigo):
    """Recibe la cadena de texto con el código Python y la guarda en un archivo .py"""
    nombre_archivo=obtener_nombre_dinamico(codigo)
    try:
        # Asegura que la carpeta de destino exista
        os.makedirs(directorio_destino, exist_ok=True)

        # Asegura que el nombre termine en .py
        if not nombre_archivo.endswith(".py"):
            nombre_archivo += ".py"

        # Ruta completa donde se guardará el archivo
        ruta_completa = os.path.join(directorio_destino, nombre_archivo)

        # Escribe el archivo en UTF-8
        with open(ruta_completa, "w", encoding="utf-8") as archivo:
            archivo.write(codigo)

        resultado = f"✅ Archivo guardado en: {ruta_completa}"
        
        return True, resultado

    except Exception as e:
        resultado = f"❌ Error al guardar el archivo: {e}"
        
        return False, resultado
