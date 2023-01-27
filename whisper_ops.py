import whisper

base_model = whisper.load_model("base")


def transcribe_to_text(file):
    result = base_model.transcribe(file.name, fp16=False, language='ru')
    transcribed_text = result.get("text")

    if transcribed_text is None:
        return "Audio could not be transcribed"

    if len(transcribed_text) == 0:
        return "Audio is emtpy"

    return transcribed_text
