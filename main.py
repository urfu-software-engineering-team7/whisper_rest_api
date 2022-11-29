import whisper
import requests as rq

from fastapi import FastAPI, File

app = FastAPI()


@app.get("/")
def read_root():
    return "Hello World"


@app.get("/items/{item_id}")
def read_item(item_id: int, q):
    return {"item_id": item_id, "q": q}


@app.post("/translate/")
async def create_file(file: bytes = File()):
    model = whisper.load_model("base")

    url = 'https://raw.githubusercontent.com/Maksembek/urfu_soft_eng_3/main/Female.mp3'
    doc = rq.get(url)
    with open('voice.mp3', 'wb') as f:
        f.write(doc.content)
        result = model.transcribe("voice.mp3", fp16=False, language='ru')

    return {"result": result["text"]}

