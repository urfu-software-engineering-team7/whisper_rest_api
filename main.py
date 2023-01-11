import requests as rq

from fastapi import FastAPI
from whisper_ops import transcribe_to_text

app = FastAPI()


@app.get("/translate/")
async def create_file(url: str = None):
    doc = rq.get(url)
    with open('voice.mp3', 'wb') as f:
        f.write(doc.content)
        transcribe_result = transcribe_to_text(f)

    return {"result": transcribe_result}
