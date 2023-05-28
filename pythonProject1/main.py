import pyttsx3

def speak(text):
    engine.say(text)
    engine.runAndWait()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.setProperty('volume',1)
print("Hello, I am the RoboSpeaker! Created by Supreeth BH")
while True:
    text = input("Enter what you want me to speak:")
    speak(text)
    if text == "exit":
        speak("goodbye friend it was pleasure talking to you")
        break



