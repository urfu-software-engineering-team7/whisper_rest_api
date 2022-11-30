[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org)

# Практическое занятие №3

Создание приложения, позволяющего получать перевод русскоязычного аудио-файла в текстовом виде
 - для перевода используется библиотека [Whisper](https://openai.com/blog/whisper)
 - для передачи ссылки на аудио-файл и получения результата перевода используется библиотека [Fastapi](https://github.com/tiangolo/fastapi)
 - ссылка на файл передается методом GET через параметр `url=`

## Установка whisper:

```bash
pip install git+https://github.com/openai/whisper.git
```

### Для Windows:
Установка scoop через PowerShell:

```bash
iwr -useb get.scoop.sh | iex
```

Установка ffmpeg 

```bash
scoop install ffmpeg
```

### Для Linux:

```bash
sudo apt install ffmpeg
```
