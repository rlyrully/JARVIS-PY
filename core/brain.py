from core.memory import Memory


class JarvisBrain:

    def __init__(self):

        self.name = "JARVIS"

        self.memory = Memory()


    def think(self,text):


        text = text.lower()


        if text.startswith("ingat"):

            data = text.replace(
                "ingat",
                ""
            )

            key,value = data.split(
                "adalah"
            )

            self.memory.save(
                key.strip(),
                value.strip()
            )

            return "Baik, saya sudah menyimpannya."


        if text.startswith("apa"):

            key = text.replace(
                "apa",
                ""
            ).strip()


            result = self.memory.get(key)


            if result:

                return result


        return (
            "Saya belum memahami perintah itu."
        )
