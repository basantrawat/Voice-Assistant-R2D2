import datetime
import wikipedia
import webbrowser
import os
import subprocess
from sys import exit

import mainFunc


if __name__ == "__main__":
    mainFunc.wishMe()
    while True:
        query = mainFunc.takeCommand().lower()
        
        #logic for executing tasks based on query
        if 'open google' in query:
            webbrowser.open("https://google.com")

        elif 'open youtube' in query:
            webbrowser.open("https://youtube.com")
        
        elif 'open github' in query:
            webbrowser.open("https://github.com")
        
        # Search about anythin on wikipedia just by saying "Search about 'anything' on wikipedia"
        elif 'wikipedia' in query:
            mainFunc.speak('Searching Wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=2)
            mainFunc.speak("According to wikipedia")
            print(results)
            mainFunc.speak(results)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music\\Sample Music'
            PlayerPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"

            files = os.listdir(music_dir)
            songs = []
            for f in files:
                if f.endswith('.mp3'):
                    songs.append(f)

            print(songs)
            FilePath = os.path.join(music_dir, songs[0])
            subprocess.call([PlayerPath, FilePath])

        elif 'what\'s the time in query':
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            mainFunc.speak(f"The time is {strTime}")

        elif 'open code' in query:
            fileLocation = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(fileLocation)

        elif 'send mail' in query:
            try:
                mainFunc.speak("What should i write in mail")
                content = mainFunc.takeCommand()
                to = "samplemail@gmail.com"
                mainFunc.sendEmail(to, content)
                mainFunc.speak("Mail Sent to Mr. XYZ!")

            except Exception:
                mainFunc.speak("Sorry, i'm not able to send your mail")
        
        elif 'quit' in query:
            mainFunc.speak('Thank You, will meet you very soon. Bye Bye.')
            exit()
        