import whisper

base_model = whisper.load_model("base")


def transcribe_to_text(file):
    result = base_model.transcribe(file.name, fp16=False, language='ru')
    return result["text"]