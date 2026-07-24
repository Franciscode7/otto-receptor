from datetime import datetime, date
from pywinauto import Application, Desktop
import pyautogui
import time
import os
from dotenv import load_dotenv

load_dotenv()

NOTA_PATH = os.getenv("NOTA_PATH")

def escribir_nota(texto):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    linea = f"{fecha} - {texto}\n\n"
    
    try:
        # Abre el archivo en modo append ('a') para añadir al final sin borrar nada
        with open(NOTA_PATH, "a", encoding="utf-8") as f:
            f.write(linea)
            
        print(f"[NOTA GUARDADA] {linea.strip()}")
        return True, texto
    
    except Exception as e:
        print(f"[ERROR NOTA] {e}")
        return False
    
if __name__ == "__main__":
    texto = "webhu"
    resultado = escribir_nota(texto) 