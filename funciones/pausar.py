import keyboard


def pausar_youtube():
  # Simula la tecla 'k' o la tecla multimedia de pausa/reproducción
  # Nota: si usas la tecla multimedia de play/pause global, suele funcionar directo con YouTube en Chrome/Firefox
  keyboard.send("play/pause media")
  return True  # Indica que la acción se ejecutó (aunque no podemos verificar si YouTube estaba reproduciendo)


def siguiente_cancion():
  # En YouTube, 'Shift + n' pasa a la siguiente canción si es una lista/álbum,
  # o puedes simular las teclas multimedia de 'next track'
  keyboard.send("next track")
  print("Siguiente canción.")


# Asignar atajos globales
keyboard.add_hotkey("ctrl+alt+space", pausar_youtube)
keyboard.add_hotkey("ctrl+alt+right", siguiente_cancion)
