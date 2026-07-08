from core.brain import JarvisBrain
from core.speaker import speak
from core.listener import listen


jarvis = JarvisBrain()


speak(
    "Initializing Jarvis System"
)

speak(
    "Voice interface online"
)


while True:


    command = listen()


    if command == "":
        continue


    if "shutdown" in command.lower():

        speak(
            "Shutdown sequence activated"
        )

        break



    response = jarvis.think(
        command
    )


    speak(
        response
    )
