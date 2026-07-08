from core.brain import JarvisBrain
from core.speaker import speak
from core.listener import listen
from core.wakeword import detect


jarvis = JarvisBrain()


speak(
    "Jarvis system online"
)


while True:


    command = listen()


    if command == "":
        continue



    if detect(command):


        speak(
            "Yes sir?"
        )


        request = listen()


        response = jarvis.think(
            request
        )


        speak(
            response
        )



    if "shutdown jarvis" in command.lower():

        speak(
            "Goodbye sir"
        )

        break
