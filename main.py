import whisper
import requests as rq
from fastapi import FastAPI

app = FastAPI()


def transcribe_to_text(file):
    model = whisper.load_model("base")
    result = model.transcribe(file.name, fp16=False, language='ru')
    return result["text"]


@app.get("/translate/")
async def create_file(url: str = None):
    model = whisper.load_model("base")

    doc = rq.get(url)
    with open('voice.mp3', 'wb') as f:
        f.write(doc.content)
        transcribe_result = transcribe_to_text(model, f)

    return {"result": transcribe_result}
