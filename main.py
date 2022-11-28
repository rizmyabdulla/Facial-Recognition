import cv2
import face_recognition
import urllib.request
import numpy as np
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
from simple_facerec import SimpleFacerec
import random

#author = Abdulla
################## Speak ###################
r1 = random.randint(1,10000000)
r2 = random.randint(1,10000000)

def speak(text):
    
    tts = gTTS(text=text,lang="en")
    filename = str(r2)+"voice"+str(r1) +".mp3"
    tts.save(filename)
    playsound.playsound(filename)
    print(filename)
    os.remove(filename)
   
################## Facial Recognition ###################

##### Encode faces from a folder #####

sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
print("Succeeded")

cap = cv2.VideoCapture(0)

while True:

    #### Load Camera ####
    ret, frame = cap.read()

    #For ESP32 cam(IP Camera)
    
    #imgResponse = urllib.request.urlopen ('http://192.168.1.1:80/capture')
    #imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)
    #frame= cv2.imdecode(imgNp,-1)
    #RGB_Frame = frame[:, :, ::-1]

    #### Drawing Rectangle ####
    
    face_locations, face_names = sfr.detect_known_faces(frame)
    
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
        speak(f"{name} is Here")

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
