import requests

class JarvisBrain:

    def __init__(self):
        self.name = "JARVIS"
        self.memory = []

    def think(self, text):

        self.memory.append({
            "user": text
        })

        # sementara AI simulasi
        # nanti diganti model AI open source
        
        if "nama kamu" in text.lower():
            return "Saya JARVIS, asisten AI pribadi anda."

        if "siapa saya" in text.lower():
            return "Anda adalah pengguna utama sistem ini."

        return (
            "Saya sedang menganalisa: "
            + text
        )
