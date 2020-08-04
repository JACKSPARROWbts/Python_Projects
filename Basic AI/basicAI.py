from __future__ import print_function
import datetime
import subprocess,pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time 
import playsound
import speech_recognition as sr
import pyttsx3 as tts

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

engine=tts.init()
date=datetime.datetime.now().date()
date=str(date)
months=['january','february','march','april','may','june','july','august','september','october','november','december']
day_name=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
day_extensions=['rd','th','st']
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)
engine.setProperty('rate',120) 
def speak(text):
    engine.say(text=text)


def note(text):
    date=datetime.datetime.now()
    file_name=str(date).replace(':','-')+"-note.txt"
    with open(file_name,"w") as f:
        f.write(text)
    vscode='C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    subprocess.Popen(['notepad.exe',file_name])


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
    return said.lower()
WAKE="hey sparrow "
while True:
    speak("I am Listening sir")
    text=get_audio()
    if "hello" in text:
        speak("hello sir")
    if "make event" in text:
        speak("Yes sir your event is now creating in the notepad")
        note_text=get_audio()
        note(note_text)
        speak("i have made your note sir")

    if "my event" in text:

        def main():
   
            creds = None
    
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                    "C:\\Users\\ADMIN\\Music\\Python\\techwithtim\\credentials.json", SCOPES)
                    creds = flow.run_local_server(port=0)
       
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

            service = build('calendar', 'v3', credentials=creds)

            now = datetime.datetime.utcnow().isoformat() + 'Z' 
            print('now',now)
            speak('Getting the upcoming 10 events')
            events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                speak("Sorry Sir")
                speak('No upcoming events found.')
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                speak(start)
                speak(event['summary'])


        if __name__ == '__main__':
            main()

engine.runAndWait()


# def get_date(text):
#     text=text.lower()
#     today=datetime.date.today()
#     if text.count('today')>0:
#         return today
#     day=-1
#     day_of_week=-1
#     month=-1
#     year=today.year
#     for word in text.split():
#         if word in months:
#             month=months.index(month)+1
#         elif word in day_name:
#             day_of_week=day_name.index(word)
#         elif word.isdigit():
#             day=int(word)
#         else:
#             for ext in day_extensions:
#                 found=word.find(ext)
#                 if found>0:
#                     try:
#                         day=int(word[:found])
#                     except:
#                         pass
#     if month<today.month and month!=-1:
#         year=year+1
#     if day<today.day and month==-1 and day!=-1:
#         month=month+1
#     if month==-1 and day==-1 and day_of_week!=-1:
#         current_day_of_week=today.weekday()
#         dif=day_of_week-current_day_of_week
