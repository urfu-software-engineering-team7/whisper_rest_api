from whisper_ops import transcribe_to_text


class TestTranscribeToText:
    def test_male_mp3(self):
        with open('./mp3_samples/Male.mp3', 'r') as f:
            res = transcribe_to_text(f)

        assert res == " Натратно спать, от родней камням быть, в этот век преступный, постижный, ни жить не чувствовать уделзовидный. Прошу, молчи, не смею меня будить."

    def test_female_mp3(self):
        with open('./mp3_samples/Female.mp3', 'r') as f:
            res = transcribe_to_text(f)

        assert res == " Камесыт не будешь, Мать-дество говорил о мне, хотя нарисовой бумаге вполне."
