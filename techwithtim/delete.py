import datetime
import speech_recognition as sr 
import pyttsx3 as tts 
engine=tts.init()
date=str(input('Enter the date(for example:09 02 2019):'))
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
day = datetime. datetime. strptime(date, '%d %m %Y'). weekday()
print(day_name[day])
print(day)
def get_audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""
        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)
    return said
text=get_audio()
print(datetime.datetime.now().today())

engine.runAndWait()