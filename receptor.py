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
    
    if accion == "abrir_url":
        if valor: # Verificamos que el usuario envió una URL
            exito = abrir_enlace(valor)
            if exito:
                return jsonify({"status": "ok", "msg": f"Abriendo {valor}"}), 200
            else:
                return jsonify({"status": "error", "msg": "No se pudo abrir el navegador"}), 500
        else:
            return jsonify({"status": "error", "msg": "Falta el valor (URL)"}), 400

    elif accion == "youtube":
        if valor: # Verificamos que el usuario envió una URL
            if valor == "pausar":
                exito = pausar_youtube() 
                print(f"Pausando reproducción de YouTube: {exito}")
                if exito:
                    return jsonify({"status": "ok", "msg": "Reproducción pausada"}), 200
                else:
                    return jsonify({"status": "error", "msg": "No se pudo pausar la reproducción"}), 404
                
            else:
                exito, detalle = buscar_youtube(valor)
                print('exito')
                print(exito)
                print('detalle')
                print(detalle)
                time.sleep(0.5)  # Espera un segundo antes de intentar poner la canción
                pausar_youtube()  # Pausa cualquier reproducción actual
                time.sleep(0.5)  # Espera un segundo antes de poner la nueva
                if exito:
                    return jsonify({"status": "ok", "msg": f"Reproduciendo: {detalle}"}), 200
                else:
                    return jsonify({"status": "error", "msg": detalle}), 404
        else:
            return jsonify({"status": "error", "msg": "Falta el nombre del video"}), 400

    
    elif accion == "brillo":
        if valor: 
            exito = ajustar_brillo(valor)
            if exito:
                return jsonify({"status": "ok", "msg": f"Brillo al {valor}%"}), 200
            else:
                return jsonify({"status": "error", "msg": f"No se pudo ajustar el brillo al {valor}%"}), 500
        else:
            return jsonify({"status": "error", "msg": "Valor incorrecto"}), 400

    if accion == "volumen":
        if valor: # Verificamos que el usuario envió una URL
            exito = ajustar_volumen(valor)
            # if exito:
            return jsonify({"status": "ok", "msg": f"Volumen al {valor}%"}), 200
            # else:
            #     return jsonify({"status": "error", "msg": "No se pudo ajustar el volumen"}), 500
        else:
            return jsonify({"status": "error", "msg": "Falta el valor (URL)"}), 400


    elif accion == "nota":
        if valor: # Verificamos que el usuario envió una URL
            exito, nota_escrita = escribir_nota(valor)
            if exito:
                return jsonify({"status": "ok", "msg": f"Nota guardada: {nota_escrita}"}), 200
            else:
                return jsonify({"status": "error", "msg": "No se pudo escribir la nota"}), 500
        else:
            return jsonify({"status": "error", "msg": "Falta el valor"}), 400


    elif accion == "abrir_app":
        if valor: # Verificamos que el usuario envió una URL
            exito = abrir_app(valor)
            if exito:
                return jsonify({"status": "ok", "msg": f"App abierta: {valor}"}), 200
            else:
                return jsonify({"status": "error", "msg": "No se pudo abrir la app"}), 500
        else:
            return jsonify({"status": "error", "msg": "Falta el valor (URL)"}), 400
        
        
    elif accion == "cerrar_app":
        if valor: # Verificamos que el usuario envió una URL
            exito = cerrar_app(valor)
            if exito:
                return jsonify({"status": "ok", "msg": f"App cerrada: {valor}"}), 200
            else:
                return jsonify({"status": "error", "msg": "No se pudo cerrar la app"}), 500
        else:
            return jsonify({"status": "error", "msg": "Falta el valor (URL)"}), 400
        
        
        
    elif accion == "trabajar":
            if valor: # Verificamos que el usuario envió un valor
                buscar_youtube("safety net live ariana grande")
                time.sleep(1)
                exito = vscode(valor)
                if exito:
                    return jsonify({"status": "ok", "msg": f"🤖 Todo preparado, Se abrió: D:/developer/{valor}"}), 200
                else:
                    return jsonify({"status": "error", "msg": "No se pudo procesar"}), 500
            else:
                return jsonify({"status": "error", "msg": "Falta el valor"}), 400
            
            
            
    elif accion == "crear_py":
        if valor: # Verificamos que el usuario envió un valor
            exito = crear_python(valor)
            if exito:
                print ("logrado")
                return jsonify({"status": "ok", "msg": f"Scrpt creado: {valor}"}), 200
            else:
                return jsonify({"status": "error", "msg": "No se pudo crear el archivo"}), 500
        else:
            return jsonify({"status": "error", "msg": "Falta el valor"}), 400
            
            
    elif accion == "screenshot":
        if valor: # Verificamos que el usuario envió un valor
            exito, img_base64 = capturar_pantalla()
        
            if exito:
                return jsonify({
                    "status": "ok",
                    "type": "image_base64",
                    "image_base64": img_base64,
                    "msg": "Captura realizada correctamente"
                }), 200
            
            else:
                return jsonify({"status": "error", "msg": "No se pudo realizar la captura de pantalla"}), 500         
        
        else:
            return jsonify({"status": "error", "msg": "Falta el valor"}), 400    

if __name__ == '__main__':
    # Ejecuta la terminal como ADMINISTRADOR para que te deje usar el puerto 7777
    app.run(host=os.getenv('HOST'), port=7777)
