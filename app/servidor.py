from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensaje": "Servidor funcionando 🚀"}

@app.post("/whatsapp")
async def recibir_mensaje(request: Request):
    datos = await request.json()
    print("Mensaje recibido:", datos)
    return {"status": "Mensaje recibido"}