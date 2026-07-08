from core.memory import Memory
from core.ai import AI


class JarvisBrain:


    def __init__(self):

        self.memory = Memory()

        self.ai = AI()


    def think(self,text):


        if text.lower().startswith("ingat"):


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


            return (
                "Baik, saya akan mengingatnya."
            )



        answer = self.ai.ask(
            text
        )


        return answer
