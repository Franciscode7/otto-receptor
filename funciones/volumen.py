import os

def ajustar_volumen(valor):
    try: # Ajustar volumen con PowerShell (requiere módulo AudioDeviceCmdlets)
        cmd = f"powershell Set-AudioDevice -PlaybackVolume {valor}"
        os.system(cmd)
        resultado = f"Volumen ajustado correctamente al {valor}%"
        return True, resultado
    
    except:
        resultado = f"No se pudo ajustar el volumen"
        return False, resultado