import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

speak("Hello. I am Jarvis.")

while True:
    command = input("You: ").lower()

    if "hello" in command:
        speak("Hello. How can I help you?")

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "exit" in command:
        speak("Goodbye.")
        break

    else:
        speak("I do not understand.")