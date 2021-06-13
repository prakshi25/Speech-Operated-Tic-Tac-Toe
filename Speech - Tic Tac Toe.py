import speech_recognition as sr
import pyttsx3
import datetime
import time
import webbrowser
r=sr.Recognizer()
text=""
l1=[1,2,3,4,5,6,7,8,9]

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[17].id)
text = ""

def speak(audio):
    engine.setProperty("rate", 180)
    engine.say(audio)
    engine.runAndWait()

speak("I am a Tic Tac Toe Bot")
p1=""
p2=""
while p1!="no" or p2!="no" or text!="no":
    print("Please talk or say no to stop")
    with sr.Microphone() as source:

        if text=="no" or p1=="no" or p2=="no":
            print("ByE")
            speak("Bye")
            break

        speak("Who is player one?")
        print("Getting")
        audio_data=r.record(source,duration=6)
        p1=r.recognize_google(audio_data)
        print(p1)

        speak("And who is the opponent?"+ p1)
        print("Getting")
        audio_data = r.record(source, duration=6)
        p2=r.recognize_google(audio_data)
        print(p2)

        speak("Okay")
        speak(p1+", your symbol is criss")
        speak("and "+p2+", your symbol is cross")
        speak("Let the game begin")
        print(l1[0], l1[1], l1[2])
        print(l1[3], l1[4], l1[5])
        print(l1[6], l1[7], l1[8])
        print(p1,"-> 0")
        print(p2,"-> X")
        for i in range(1, 11):
            if i == 2 or i == 4 or i == 6 or i == 8:
                speak(p2+" now your turn")
                print("Getting")
                audio_data = r.record(source, duration=6)
                text = r.recognize_google(audio_data)
                print("Position: "+text)
                if text.isnumeric():
                    a = int(text)
                l1[a - 1] = 'X'
                print(l1[0], l1[1], l1[2])
                print(l1[3], l1[4], l1[5])
                print(l1[6], l1[7], l1[8])
                if l1[0] == 'X' and l1[1] == 'X' and l1[2] == 'X' or l1[0] == '0' and l1[1] == '0' and l1[2] == '0':
                    speak(p2+", you won")
                    break
                elif l1[3] == 'X' and l1[4] == 'X' and l1[5] == 'X' or l1[3] == '0' and l1[4] == '0' and l1[5] == '0':
                    speak(p2+", you won")
                    break
                elif l1[6] == 'X' and l1[7] == 'X' and l1[8] == 'X' or l1[6] == '0' and l1[7] == '0' and l1[8] == '0':
                    speak(p2+", you won")
                    break
                elif l1[0] == 'X' and l1[4] == 'X' and l1[8] == 'X' or l1[0] == '0' and l1[4] == '0' and l1[8] == '0':
                    speak(p2+", you won")
                    break
                elif l1[2] == 'X' and l1[4] == 'X' and l1[6] == 'X' or l1[2] == '0' and l1[4] == '0' and l1[6] == '0':
                    speak(p2+", you won")
                    break
                elif l1[0] == 'X' and l1[3] == 'X' and l1[6] == 'X' or l1[0] == '0' and l1[3] == '0' and l1[6] == '0':
                    speak(p2+", you won")
                    break
                elif l1[1] == 'X' and l1[4] == 'X' and l1[7] == 'X' or l1[1] == '0' and l1[4] == '0' and l1[7] == '0':
                    speak(p2+", you won")
                    break
                elif l1[2] == 'X' and l1[5] == 'X' and l1[8] == 'X' or l1[2] == '0' and l1[5] == '0' and l1[8] == '0':
                    speak(p2+", you won")
                    break
            elif i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
                speak(p1+" its your turn")
                print("Getting")
                audio_data = r.record(source, duration=6)
                text = r.recognize_google(audio_data)
                print("Position: "+text)
                if text.isnumeric():
                    b = int(text)
                l1[b - 1] = '0'
                print(l1[0], l1[1], l1[-7])
                print(l1[3], l1[4], l1[5])
                print(l1[6], l1[7], l1[8])
                if l1[0] == 'X' and l1[1] == 'X' and l1[2] == 'X' or l1[0] == '0' and l1[1] == '0' and l1[2] == '0':
                    speak(p1+", you won")
                    exit()
                elif l1[3] == 'X' and l1[4] == 'X' and l1[5] == 'X' or l1[3] == '0' and l1[4] == '0' and l1[5] == '0':
                    speak(p1+", you won")
                    break
                elif l1[6] == 'X' and l1[7] == 'X' and l1[8] == 'X' or l1[6] == '0' and l1[7] == '0' and l1[8] == '0':
                    speak(p1+", you won")
                    break
                elif l1[0] == 'X' and l1[4] == 'X' and l1[8] == 'X' or l1[0] == '0' and l1[4] == '0' and l1[8] == '0':
                    speak(p1+", you won")
                    break
                elif l1[2] == 'X' and l1[4] == 'X' and l1[6] == 'X' or l1[2] == '0' and l1[4] == '0' and l1[6] == '0':
                    speak(p1+", you won")
                    break
                elif l1[0] == 'X' and l1[3] == 'X' and l1[6] == 'X' or l1[0] == '0' and l1[3] == '0' and l1[6] == '0':
                    speak(p1+", you won")
                    break
                elif l1[1] == 'X' and l1[4] == 'X' and l1[7] == 'X' or l1[1] == '0' and l1[4] == '0' and l1[7] == '0':
                    speak(p1+", you won")
                    break
                elif l1[2] == 'X' and l1[5] == 'X' and l1[8] == 'X' or l1[2] == '0' and l1[5] == '0' and l1[8] == '0':
                    speak(p1+", you won")
                    break
            else:
                speak("It's a Tie!")
                break
