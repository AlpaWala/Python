import pyttsx3
import webbrowser
import datetime
import os

engine = pyttsx3.init("sapi5")

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Hey Siri")

while True:
    command = input("\nEnter command: ").lower()

    if "exit" in command or "quit" in command:
        speak("Goodbye")
        break

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "open folder" in command:
        speak("Opening your project folder")
        os.startfile(os.getcwd())

    else:
        speak("Command not recognized")
