# import all the modules from your computer
import datetime
import time
import webbrowser
import pyttsx3
import speech_recognition as sr
import psutil

# it is use your computers voice
def defult_voice(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

# it is use your computers voice
def mail_voice(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

# it is use your computers voice
def femail_voice(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

# it is a string which is used for checking battery level in percentage
def battery():
    psutil.sensors_battery().percent

# wishme function use your computer's defult voice
def wish_by_time():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        defult_voice("good morning")
    elif 12 <= hour < 18:
        defult_voice("good afternoon")
    else:
        defult_voice("good evening")

# used for listening your queries from your microphone
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        defult_voice("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        defult_voice("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        defult_voice(f"user said: {query}")
    except Exception as e:
        print("say that again please")
        defult_voice("say that again please")
        return "None"
    return query

# to know the current time in Hour, Minute and seconds from your computer
def now():
    str(time.strftime("%H:%M:%S"))

# you can search any thing like URL using your defult webbrowser
def web(URL):
    webbrowser.open(URL)
