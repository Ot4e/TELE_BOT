import pyttsx3
import random
import string
import subprocess
import os

engine = pyttsx3.init()
voice_id = "TTS_MS_RU-RU_IRINA_11.0"
engine.setProperty('voice', voice_id)

def text_to_file(text):
    '''Generate voice message from input text'''
    #get the all simbols + digits from string module
    set_of_simbols = string.ascii_letters + string.digits
    #generate unique f/n of 6 characters
    tmp_file_name = ''.join(random.sample (set_of_simbols, 6))
    mp3_fn = f'data/{tmp_file_name}.mp3'
    ogg_fn = f'data/{tmp_file_name}.ogg'
    engine.save_to_file(text , mp3_fn)
    engine.runAndWait()
    #do .ogg from .mp3
    subprocess.run(["ffmpeg", '-i', mp3_fn, '-acodec', 'libopus', ogg_fn, '-y'])
    os.remove(mp3_fn)
    return ogg_fn
