import whisper
import requests

model = whisper.load_model("base")

url = 'https://raw.githubusercontent.com/Maksembek/urfu_soft_eng_3/main/Female.mp3'
doc = requests.get(url)
with open('voice.mp3', 'wb') as f:
    f.write(doc.content)
    result = model.transcribe("voice.mp3", fp16=False, language='ru')
    print(result["text"])
