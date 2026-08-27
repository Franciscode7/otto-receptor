from datetime import datetime
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
            
        resultado = f"Nota guardado {texto}"
        return True, resultado
    
    except Exception as e:
        resultado = f"Error al crear nota {e}"
        return False, resultado
    
if __name__ == "__main__":
    texto = "webhu"
    resultado = escribir_nota(texto) 