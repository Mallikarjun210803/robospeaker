import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)
engine.setProperty('volume', 1)

print("Hello, I am the RoboSpeaker! Created by Supreeth BH")

while text != "exit":
    text = input("Enter what you want me to speak:")
    engine.say(text, wait=False)

speak("goodbye friend it was pleasure talking to you")
