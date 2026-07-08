from core.brain import JarvisBrain
from core.speaker import speak


jarvis = JarvisBrain()


speak("Initializing Jarvis System")
speak("Artificial intelligence online")


while True:

    command = input("YOU : ")

    if command.lower() == "exit":
        speak("Shutdown sequence activated")
        break


    response = jarvis.think(command)

    speak(response)
