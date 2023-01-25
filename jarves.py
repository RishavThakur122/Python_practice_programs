import pyttsx3
import datetime
import pyaudio
import speech_recognition as R
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_commands():
    s = R.Recognizer()
    with R.Microphone() as source:
        print("i am Listing sir....")
        s.pause_threshold = 1
        audio = s.listen(source)
    try:
        print("Recognizing...")
        query = s.recognize_google(audio,Language='en-in')
        print("user said :",query)
    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good Evenning")
    speak("hello I am anya how can i  help you sir")    

if __name__=="__main__":
    wishme()
    take_commands()
      
    
