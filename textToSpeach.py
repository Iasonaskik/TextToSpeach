import pyttsx3
import time

def speak(text,speed,voiceIndex):
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate',speed)


    fones = engine.getProperty('voices')
    if 0 <= voiceIndex < len(fones):
        engine.setProperty('voice',fones[voiceIndex].id)

    engine.setProperty('volume',0.9)

    engine.say(text)
    engine.runAndWait()

usertext = input("Type something: ")


speed = int(input("Enter speed: "))

speak(usertext,speed,0)





