from main import transcribe_to_text
import whisper


class TestTranscribeToText:
    def test_male_mp3(self):
        model = whisper.load_model("base")

        with open('./tests/Male.mp3', 'r') as f:
            res = transcribe_to_text(model, f)

        assert res == "Натратно спать, от родней камням быть, в этот век преступный, постижный, ни жить не чувствовать уделзовидный. Прошу молчи, не смея меня будите."
