from app.procesar_audio import transcribir_audio

ruta = r"C:\Users\josem\OneDrive\Escritorio\python\chat wsp\app\audios\prueba.mp3"
texto = transcribir_audio(ruta)
print("Texto transcrito:", texto)
