import os
import subprocess


def vscode(carpeta_proyecto):
    # --- Definición de tus rutas ---
    base_dir = r"D:\developer"  # Tu carpeta base
    
    # 'os.path.join' unifica la ruta según el sistema operativo automáticamente
    ruta_completa = os.path.join(base_dir, carpeta_proyecto)

    try:
        # shell=True permite que Windows ejecute 'code.cmd' sin fallar
        subprocess.Popen(["code", ruta_completa], shell=True)
        print(f"VS Code abierto correctamente en: {ruta_completa}")
        return True
    except Exception as e:
        print(f"Error al abrir VS Code: {e}")