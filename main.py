from core.brain import JarvisBrain
from core.speaker import speak


jarvis = JarvisBrain()


def start_text_mode():

    speak(
        "Jarvis text mode activated"
    )


    while True:


        command = input(
            "YOU : "
        )


        if command.lower() == "exit":

            speak(
                "Jarvis shutting down"
            )

            break



        response = jarvis.think(
            command
        )


        print(
            "JARVIS :",
            response
        )



start_text_mode()
