import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
import httplib2
http = httplib2.Http()
import time
import datetime
                                
# Define URL's used when sending http requests
#url_on = 'http://192.168.43.254/gpio/1'
#url_off = 'http://192.168.43.254/gpio/0'
#response, content = http.request(url_off, 'GET')
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-2].id)

def speak(audio):
    print('haydel: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am haydel!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        audio = r.listen(source)
        print("Time over")
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif "who are you" in query or 'what is your name' in query:
            stMsgs = ['i am haydel, the ultimate power of universe at your service!', 'I am haydel']
            speak(random.choice(stMsgs))
        elif "who made you" in query or 'who is your father' in query:
            stMsgs = ['i am creation of name', 'i am creation of universe']
            speak(random.choice(stMsgs))
        elif "do you believe in god" in query or 'who is god' in query:
            stMsgs = ['simply ,i am bot creation of human so i believe in human', "god is something who has the power to create and destroy"]
            speak(random.choice(stMsgs))
        elif "i love you" in query or 'will you marry me' in query:
            stMsgs = ['i am feeling shy', 'oh my god, i love you too', 'i love you too', 'sorry i have a boyfriend']
            speak(random.choice(stMsgs))
        elif "do you have a boyfriend" in query or 'who is your boyfriend' in query:
            stMsgs = ['i am feeling shy', 'you are annoying']
            speak(random.choice(stMsgs))
        elif "who is prime minister of india" in query or 'prime minister' in query:
            stMsgs = ['mr. narender modi is the prime minister of india']
            speak(random.choice(stMsgs))

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')
        elif 'lights on' in query:
            #response, content = http.request(url_on, 'GET')
            speak('done your lights are on ')
            
        elif 'lights off' in query:
            #response, content = http.request(url_off, 'GET')
            speak('done, your lights are off ')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            os.startfile("music1.mp3")
                  
            speak('Okay, here is your music! Enjoy!')
            
        elif 'take attendance' in query:
            y="0"
            speak('to confirm, choose option either passcode or face detection')
            speak("1 for passcode and 2 for face detection")
            x=(input(""))
            if x=="1":
                speak('enter passcode ')
                y=(input("passcode = "))
                if y=="123":
                  #response, content = http.request(url_on, 'GET')
                  time.sleep(1)
                  #response, content = http.request(url_off, 'GET')
                  
                  speak("attendance done")
                else:
                  speak("try again, you have entered a wrong password")
                 

            elif x=="2":
                import face_recognition
                import cv2
                import sys
                USE_WEBCAM = True 
                
                # camera
                cv2.namedWindow('window_frame')
                video_capture = cv2.VideoCapture(0)
                
                
                # training picture 1
                known_image1 = face_recognition.load_image_file("first image.jpg")
                known_face_encoding1 = face_recognition.face_encodings(known_image1)[0]
                
                # training picture 2
                known_image2 = face_recognition.load_image_file("second face.jpg")
                known_face_encoding2 = face_recognition.face_encodings(known_image2)[0]
                
                # Create arrays of known face encodings and their names
                known_face_encodings = [
                    known_face_encoding1,
                    known_face_encoding2
                ]
                known_face_names = [
                    "first image name",
                    "second image name"
                ]
                
                # Initialize some variables
                face_locations = []
                face_encodings = []
                face_names = []
                process_this_frame = True
                count=0
                while True:
                    # Grab a single frame of video
                    ret, frame = video_capture.read()
                
                    # Resize frame of video to 1/4 size for faster face recognition processing
                    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                
                    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
                    rgb_small_frame = small_frame[:, :, ::-1]
                
                    # Only process every other frame of video to save time
                    if process_this_frame:
                        # Find all the faces and face encodings in the current frame of video
                        face_locations = face_recognition.face_locations(rgb_small_frame)
                        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                
                        face_names = []
                        for face_encoding in face_encodings:
                            # See if the face is a match for the known face(s)
                            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                            name = "Unknown"
                
                            # If a match was found in known_face_encodings, just use the first one.
                            if True in matches:
                                first_match_index = matches.index(True)
                                name = known_face_names[first_match_index]
                                    
                                    # Make sure light is off at startup

                                   
                                if name=="name of candidate":
                                   print("\rname of candidate :"+str(count),end=""),
                                   count=count+1    
                                if count>=5:
                                   response, content = http.request(url_on, 'GET')
                                   time.sleep(1)
                                   #response, content = http.request(url_off, 'GET')    
                                    
                                    # Function for checking address balance on the IOTA tangle. 
                            face_names.append(name)
                
                    process_this_frame = not process_this_frame
                
                
                    # Display the results
                    for (top, right, bottom, left), name in zip(face_locations, face_names):
                        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4
                
                        # Draw a box around the face
                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                
                        # Draw a label with a name below the face
                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                
                    # Display the resulting image
                    cv2.imshow('Video', frame)
                
                    # Hit 'q' on the keyboard to quit!
                    if cv2.waitKey(1) & 0xFF == ord('q') or count>5:
                        break
                
                # Release handle to the webcam
                video_capture.release()
                cv2.destroyAllWindows()
                print("\n")
                speak("face recognised attendance done")
            else :
                speak('Errorrrr')
                print("ERROR")

        else:
            query = query
            speak('Searching...')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak(' - ')
                speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
        
        
