import screen_brightness_control as sbc

def ajustar_brillo(nivel):
    try:
        # 1. Limpiamos el valor por si llega con espacios o formato extraño
        nivel_limpio = int(float(str(nivel).strip())) 
        
        # 2. Intentamos cambiar el brillo
        sbc.set_brightness(nivel_limpio)
        resultado = f"Brillo al {nivel}%"

        return True, resultado
    
    except Exception as e:
        resultado = f"No se pudo ajustar el brillo al {nivel}%"
        
        return False, resultado