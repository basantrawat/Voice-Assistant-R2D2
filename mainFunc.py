import smtplib
import datetime
import speech_recognition as sr
import pyttsx3


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<17:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    
    speak("I'm R2-D2, How can i help you Sir") #c3-po


def takeCommand():
    '''
    It takes microphone input from the user
    and returns string as output
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')
    
    except Exception:
        # print(e)
        print("Say that again please...")
        return 'None'
    
    return query

def sendEmail(to, content):
    yourMailId = "yourmail@gmail.com"
    yourPassword = 'yourPassword'
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(yourMailId, yourPassword)
    server.sendmail(yourMailId, to, content)
    server.close()