from flask import Flask, request, jsonify, send_file
import os
import subprocess
import datetime
import time
from dotenv import load_dotenv
from funciones import *

load_dotenv()  # Cargar variables de entorno desde el archivo .env

app = Flask(__name__)

with open("bot.log", "a") as f:
    f.write(f"Bot iniciado: {datetime.datetime.now()}\n")


# Contraseña simple para seguridad
API_KEY = os.getenv("HEADER_KEY")  # Cámbiala por algo más seguro en producción

@app.route('/orden', methods=['POST'])
def recibir_orden():
    # Validar seguridad
    auth = request.headers.get("X-API-KEY")
    if auth != API_KEY:
        return jsonify({"status": "error", "msg": "No autorizado"}), 401

    data = request.json
    accion = data.get("accion")
    valor = data.get("valor")  # Puede ser URL, ruta, número, etc.

    print(f"Comando recibido del servidor: {accion} -> {valor}")
    
    match accion:
        case "abrir_url":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el valor (URL)"}), 400
            
            exito, resultado = abrir_enlace(valor)
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500
    
    
        case "youtube":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el nombre del video"}), 400
            
            if valor == "pausar":
                exito, resultado = pausar_youtube() 
                if exito:
                    return jsonify({"status": "ok", "msg": resultado}), 200
                else:
                    return jsonify({"status": "error", "msg": resultado}), 404
           
            else:
                exito, resultado = buscar_youtube(valor)
                if exito:
                    return jsonify({"status": "ok", "msg": resultado}), 200
                else:
                    return jsonify({"status": "error", "msg": resultado}), 404

    
        case "brillo":
            if not valor:
                return jsonify({"status": "error", "msg": "Valor inexistente o invalido"}), 400
                
            exito, resultado = ajustar_brillo(valor)
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500


        case "volumen":
            if not valor:
                return jsonify({"status": "error", "msg": "Valor inexistente o invalido"}), 400
                
            exito, resultado = ajustar_volumen(valor)
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500


        case "nota":
            if not valor:
                return jsonify({"status": "error", "msg": "No hay ningun valor para anotar"}), 400
                
            exito, resultado = escribir_nota(valor)
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500


        case "abrir_app":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el nombre de la app a abrir"}), 400
                
            exito, resultado = abrir_app(valor)
            if exito:
                return jsonify({"status": "ok", "msg": {resultado}}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500


        case "cerrar_app":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el nombre de la app a abrir"}), 400
                
            exito, resultado = cerrar_app(valor)
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500


        case "trabajar":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el nombre de la carpeta a abrir"}), 400
            
            exito, resultado = vscode(valor)
            time.sleep(1)
            buscar_youtube("pov de ariana grande")
            
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500
            
            
        case "crear_py":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el script"}), 400
            
            exito, resultado = crear_python(valor)
            if exito:
                return jsonify({"status": "ok", "msg": resultado}), 200
            else:
                return jsonify({"status": "error", "msg": resultado}), 500
        
        
        case "screenshot":
            if not valor:
                return jsonify({"status": "error", "msg": "Falta el parametro valor"}), 400
            
            exito, img_base64, resultado = capturar_pantalla()
            if exito:
                return jsonify({
                    "status": "ok",
                    "type": "image_base64",
                    "image_base64": img_base64,
                    "msg": resultado
                }), 200
            
            else:
                return jsonify({"status": "error", "msg": resultado}), 500         

        case _:
            return jsonify({"status": "error", "msg": f"Acción desconocida: {accion}"}), 400
        
        
if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=7777)
