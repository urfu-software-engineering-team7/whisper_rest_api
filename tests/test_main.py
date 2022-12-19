import whisper


def transcribe_to_text(model, file):
    result = model.transcribe(file.name, fp16=False, language='ru')
    return result["text"]


class TestTranscribeToText:
    def test_male_mp3(self):
        model = whisper.load_model("base")

        with open('./tests/Male.mp3', 'r') as f:
            res = transcribe_to_text(model, f)

        assert res == " Натратно спать, от родней камням быть, в этот век преступный, постижный, ни жить не чувствовать уделзовидный. Прошу молчи, не смея меня будите."

    def test_female_mp3(self):
        model = whisper.load_model("base")

        with open('./tests/Female.mp3', 'r') as f:
            res = transcribe_to_text(model, f)

        assert res == " Камесыт не будешь, Мать-дество говорил о мне, хотя нарисовой бумаги вполне."
        
    def test_error(self):
        assert 1 == 2, "Test error print"