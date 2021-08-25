# TELE_BOT

Проект содержит код шуточного Telegram бота, который отвечает на текстовые собщения фрагментами "политической" речи в виде голосового сообщения.

Для разворачивания на своей платформе требуются:
 - установленный python 3;
 - библиотеки python-telegram-bot и pyttsx3;
 - устновленный ffmpeg.
Так же необхордимо создать в корне проекта пустую директорию data и файл token.txt. 
В файле token.txt должен быть записан токен, выданный при регистрации бота в Telegram без дополнительных символов и строк до и после него.

Значение параметра voice_id в модуле voice.py зависит от настроек вашей операционной системы и ваших предпочтений.

python 3 можно скачать тут: https://www.python.org/downloads/

установка библиотек: pip install -r requirements.txt

ffmpeg можно скачать тут: https://www.ffmpeg.org/

регистрация Telegram бота: @BotFather

    выполнить команду /newbot
    
    ответить на вопрос о наименовании бота
    
    ответить на вопрос о username бота, с окончанием на "bot"
    
    записать набор символов, следующий после строки: "Use this token to access the HTTP API:" в файл token.txt
    

вывод списка доступных голосов (параметр voice_id):

import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for voice in voices:

    print(voice_id)
