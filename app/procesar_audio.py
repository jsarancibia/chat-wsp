import whisper

modelo = whisper.load_model("small")

def transcribir_audio(ruta_audio: str) -> str:
    """
    Recibe la ruta de un archivo de audio y devuelve el texto transcrito.
    """
    resultado = modelo.transcribe(ruta_audio, fp16=False)
    return resultado["text"]
    