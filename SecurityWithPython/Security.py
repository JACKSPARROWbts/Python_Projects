import face_recognition,smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import pyttsx3 as tts ,cv2
import pyautogui as gui,time
engine=tts.init()
engine.setProperty("rate",200)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ref,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(frame,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,240),3,cv2.LINE_AA)
        cv2.putText(frame,"captain",(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3,cv2.LINE_AA)
    cv2.imshow("image",frame)
    cv2.imwrite("C:\\Users\\ADMIN\\Music\\Python\\personimg.jpg",gray)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break 
    
imageofbill=face_recognition.load_image_file('C:\\Users\\ADMIN\\Music\\Python\\personimg.jpg')
billfaceencoding=face_recognition.face_encodings(imageofbill)[0]
unknownimage=face_recognition.load_image_file('C:\\Users\\ADMIN\\Music\\Python\\yourImage.jpg')
unknownencoding=face_recognition.face_encodings(unknownimage)[0]
results=face_recognition.compare_faces([billfaceencoding],unknownencoding)
print(results)
if results[0]:
    engine.say("hello sir")
    time.sleep(2)
    engine.say("How are you ")
else:
    engine.say("sorry sir i don't know who you are")
    time.sleep(3)
    fromaddr = "youraddress@gmail.com"
    toaddr = "youraddress@gmail.com"
   
    msg = MIMEMultipart() 
  
    msg['From'] = fromaddr 
  
    msg['To'] = toaddr 
  
    msg['Subject'] = "Sir, Your account has been breached...!!!"
  
    body = "Sir,kindly secure your laptop which was opended by someone...!!!"
  
    msg.attach(MIMEText(body, 'plain')) 
  
    filename = "personimg.jpg"
    attachment = open("C:\\Users\\ADMIN\\Music\\Python\\web\\personimg.jpg", "rb") 
  
    p = MIMEBase('application', 'octet-stream') 
  
    p.set_payload((attachment).read()) 
  
    encoders.encode_base64(p) 
   
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
    msg.attach(p) 
  
    s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    s.starttls() 
  
 
    s.login(fromaddr, "your password") 
  
    text = msg.as_string() 
  
    s.sendmail(fromaddr, toaddr, text) 
    s.quit()
    print(gui.position())
    gui.click(19,1039)
    time.sleep(2)
    gui.click(25,994)
    time.sleep(2)
    gui.doubleClick(116,880)
engine.runAndWait()
cv2.waitKey()
cv2.destroyAllWindows()
#enable allow less secure apps in your mail account