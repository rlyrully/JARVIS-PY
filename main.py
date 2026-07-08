import time

def speak(text):
    print("JARVIS :", text)

def brain(command):

    if "hello" in command.lower():
        return "Hello sir, Jarvis system online."

    if "status" in command.lower():
        return "All systems are running normally."

    if "time" in command.lower():
        return time.strftime(
            "Current time is %H:%M"
        )

    return "I am processing your request."


speak("Initializing Jarvis...")
speak("Loading AI Core...")
speak("System Online")

while True:

    command = input("YOU : ")

    if command.lower() == "exit":
        speak("Goodbye sir.")
        break

    answer = brain(command)

    speak(answer)
