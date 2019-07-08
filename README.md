# personal-chatbot-with-face recognition-and-home-automation
A speech recognition chat-bot with face recognition and some home automation skills using python and arduino ide software (arduino wifi module esp8266)

## Requirement for this project:
1. anaconda software with installed spyder and installed vscode given in anaconda navigator(sufficient for chatbot, face recognition and task automation of pc)
2. require only catbot.py program file

### Home automation:
1. all above requirements
2. arduino wifi module(wemos d1 esp8266)
3. relay
4. arduino program file

## How to use:

### install following libraries in spyder using anaconda prompt:
1. pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-  win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
2. pip install opencv-contrib-python   
3. pip install pyttsx3
4. pip install webbrowser
5. pip install smtplib
6. pip install SpeechRecognition
7. pip install pyaudio
8. pip install wikipedia
9. pip install httplib2
10. pip install cmake
11. pip install face_recognition

> some might be pre installed

### Setup:

after installing all the above  just run the chatbot.py file from either spyder or anaconda prompt.The chatbot.py file could take some time in response as it is dependent on your network speed for speech to text cnversion and then again text to speed conversion.if want some quick response just run textchatbot.py, it takes text input rather than speech.

now for home automation purpose i am using wifi module(wemos d1 esp8266) whose program is given in arduino program file. just upload that program into your board and join the wire from D2 pin(in my case) to your relay input pin.This is all the hardware wiring part.

After all this just uncomment all the url code line like(#url_on = 'http://192.168.43.254/gpio/1', 
#url_off = 'http://192.168.43.254/gpio/0', 
#response, content = http.request(url_off, 'GET')) from your chatbot.py or textchatbot.py file and also don't forget to update ssid and password of the arduino program file as per common hotspot connecting both pc and wifi module.


