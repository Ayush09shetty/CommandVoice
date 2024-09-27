import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi I am Jarvis ,how may I help You Sir")  

def takeCommand():
    #It take microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query    

if __name__ == "__main__":
    wishme()
    if 1:
        query = takeCommand().lower()

    # Logic for executing task based on query
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)
            
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
        speak("Opening Youtube")

    elif 'open google' in query:
        webbrowser.open("google.com")
        speak("Opening Google")

    elif 'open gmail' in query:
        webbrowser.open("gmail.com")
        speak("Opening Gmail")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'open code' in query:
        codePath = "C:\\Users\\AYUSH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak("Opening Visual Code")

    elif 'open microsoft edge' in query:
        edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(edgePath)
        speak("Opening Microsoft Edge")
  
    elif 'open microsoft teams' in query:
        teamsPath = "C:\\Users\\AYUSH\\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart 'Teams.exe'"
        os.startfile(teamsPath)
        speak("Opening Microsoft Edge")

    elif 'open zoom' in query:
        zoomPath = "C:\\Users\\AYUSH\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(zoomPath)
        speak("Opening Zoom")

    elif 'open wardwiz' in query:
        wardwizPath = "C:\\Program Files\\WARDWIZ\\WRDWIZUI.EXE"
        os.startfile(wardwiz)
        speak("Opening WardWiz")

    elif 'open streamlabs' in query:
        streamlabsPath = "C:\\Users\\AYUSH\\Desktop\\Video Editting Software\\Streamlabs OBS\\Streamlabs OBS.exe"
        os.startfile(streamlabsPath)
        speak("Opening Stream labs")       
               
    elif 'open obs' in query:
        obsPath = "C:\\Users\\AYUSH\\Desktop\\obs-studio\\bin\\64bit\\obs64.exe"
        os.startfile(obsPath)
        speak("Opening Obs Studio")       

    elif 'open shotcut' in query:
        shotcutPath = "C:\\Users\\AYUSH\\Desktop\\Shotcut\\shotcut.exe"
        os.startfile(shotcutPath)
        speak("Opening shotcut")

    elif 'open notepad' in query:
        notepadPath = "%windir%\\system32\\notepad.exe"
        os.startfile(notepadPath)
        speak("Opening Notepad")    
        
                 







                     

