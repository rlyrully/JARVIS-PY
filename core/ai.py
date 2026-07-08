import requests


class AI:

    def __init__(self):

        self.model = "llama3"


    def ask(self, prompt):

        try:

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )


            data = response.json()

            return data["response"]


        except:

            return (
                "AI core belum aktif. "
                "Jalankan model AI terlebih dahulu."
            )
