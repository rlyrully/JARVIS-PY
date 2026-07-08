def detect(text):

    wake_words = [
        "hey jarvis",
        "hai jarvis",
        "jarvis"
    ]


    text = text.lower()


    for word in wake_words:

        if word in text:

            return True


    return False
