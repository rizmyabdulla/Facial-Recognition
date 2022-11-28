# Facial-Recognition

## Packages Used

- [face-recognition](https://pypi.org/project/face-recognition/)

> pip install face-recognition

- [OpenCV](https://pypi.org/project/opencv-python/)

> pip install opencv-python

- simple_facerec (No Need To insstall)

- [playsound](https://pypi.org/project/playsound/)

  > pip install playsound

- [speech_recognition](https://pypi.org/project/SpeechRecognition/)

  > pip install SpeechRecognition

- [gtts](https://pypi.org/project/gTTS/)

  > pip install gTTS

## Features

- when Face Recognized,Speaking That Face Name (Need Internet Connection).

- Loading a Group images From a Folder.

- Support ESP32 cam IP Camera

- Very Fast Facial Recognition(Without Speech Recognition)

## Bugs

- Stucking When Speaking(Speech Recognition)

## ESP32 cam With Face Recognition (Using IP)

- Comment these lines Of Code

  >cap = cv2.VideoCapture(0)

  >ret, frame = cap.read()

- And unComment these lines Of Code

  >  imgResponse = urllib.request.urlopen ('http://192.168.1.1:80/capture')#camera IP

  >  imgNp = np.array(bytearray(imgResponse.read()),dtype=np.uint8)

  >  frame= cv2.imdecode(imgNp,-1)

  >  RGB_Frame = frame[:, :, ::-1]

- You Need To Upload This Code, ESP32 Camera Web Server/


## HappyCoding :heart_on_fire: :speak_no_evil:


