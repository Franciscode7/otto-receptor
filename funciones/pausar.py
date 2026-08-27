import keyboard


def pausar_youtube():
  try:
    keyboard.send("play/pause media")
    resultado = "Accion de pausa/reproducir aplicada"
      
    return True, resultado  
  
  except:
    resultado = "Error accion en la pausa/reproduccion"
    
    return True, resultado
    


def siguiente_cancion():
  # En YouTube, 'Shift + n' pasa a la siguiente canción si es una lista/álbum,
  # o puedes simular las teclas multimedia de 'next track'
  keyboard.send("next track")
  print("Siguiente canción.")


# Asignar atajos globales
keyboard.add_hotkey("ctrl+alt+space", pausar_youtube)
keyboard.add_hotkey("ctrl+alt+right", siguiente_cancion)
