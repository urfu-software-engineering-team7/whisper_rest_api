
# Audio -> url -> API -> Whisper -> text -> Response 
[![Python](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org)
![Workflow](https://github.com/recycletechno/voice_to_text_urfu_project/actions/workflows/python-tests.yml/badge.svg)

Данное приложение получает на вход API "прямую" ссылку на mp3 аудио файл, в ответ с дилем приложение отправляет текст-расшифровку, что было сказано в этом аудио.

 - для перевода используется библиотека [Whisper](https://openai.com/blog/whisper)
 - для передачи ссылки на аудио-файл и получения результата перевода используется библиотека [Fastapi](https://github.com/tiangolo/fastapi)
 - ссылка на файл передается методом GET через параметр `url=`

Для преобразования аудио в текст используется библиотека [whisper](https://github.com/openai/whisper).  
Для работы whisper также нужен мультимедийный фреймворк FFmpeg.  

### Установка FFmpeg ###  
**Установка для Windows:**  
Для Windows можно установить по ссылке [download](https://ffmpeg.org/download.html#build-windows), после добавить в PATH.  
Или же поставить в Windows установщик scoop и через него прописать команду.  
В PowerShell прописать команду:  
```
iwr -useb get.scoop.sh | iex
```
Далее устанавливаем ffmpeg:
```
scoop install ffmpeg
```

**Установка для Linux и MacOS:**
```  
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on Arch Linux
sudo pacman -S ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg
```

### Установка Whisper ### 
Желательно установить whisper c помощью команды ниже, так как она значительно повышает скорость скачивания.
```
pip install git+https://github.com/openai/whisper.git
```
Обновление:
``` 
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
``` 

Библиотека whisper может анализировать множество языков, но в реализации был выбран русский язык для лучшего результата.  
В качестве модели была выбрана модель "base".

## Реализация API: ##  
Для реализации API используется библиотека **Fastapi**.
Чтобы обрабатывать ссылку, которую пользователь отправляет пользователь, используется библиотека **requests**.

Для их скачивания можно использовать файл *requirements.txt*

**Работа приложения:**  
Ссылка на файл передается методом GET через параметр `url=`

Ссылка должно быть прямой. Файл должен быть к примеру, на git (https://raw.githubusercontent.com/), Dropbox, или другие файлообменники.  
Однако ссылки на google disck не работают, так как они не дают доступ к файлу напрямую.

Чтобы обратиться к сервису необходимо обратиться к /translate/
