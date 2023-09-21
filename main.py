import os
import gtts
import speech_recognition as sr
from playsound import playsound
from dotenv import load_dotenv
from datetime import datetime

from notion import NotionClient

r = sr.Recognizer()

load_dotenv()
token, db = os.getenv('NOTION_INTEGRATION_TOKEN'), os.getenv('NOTION_DB_NAME')
client = NotionClient(token, db)
ACTIVATION_COMMAND = 'make a note'

def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ''
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError:
        print("Could not request results from API")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = './temp.mp3'
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print('Could not play sound')

if __name__ == '__main__':
    # client.get_db()
    while True:
        a = get_audio()
        command = audio_to_text(a)
        if ACTIVATION_COMMAND in command.lower():
            print('Activated...')
            play_sound("What note would you like to add?")

            note = get_audio()
            note = audio_to_text(note)

            if note:
                play_sound(note)
                now = datetime.now().astimezone().isoformat()
                res = client.create_page(note, now, status='1')
                if res.status_code == 200:
                    play_sound("Stored new item")

