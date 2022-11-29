import whisper
import requests as rq

from fastapi import FastAPI

app = FastAPI()


@app.get("/translate/")
async def create_file(url: str = None):
    model = whisper.load_model("base")

    doc = rq.get(url)
    with open('voice.mp3', 'wb') as f:
        f.write(doc.content)
        result = model.transcribe("voice.mp3", fp16=False, language='ru')

    return {"result": result["text"]}
