import whisper

model = whisper.load_model("base")
result = model.transcribe("Alchimest.wav", fp16=False, language='ru')
print(result["text"])
print()
result = model.transcribe("Male.mp3", fp16=False, language='ru')
print(result["text"])
