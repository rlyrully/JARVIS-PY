from ui.reactor import Reactor
import tkinter as tk

from core.brain import JarvisBrain


class JarvisGUI:


    def __init__(self):

        self.jarvis = JarvisBrain()


        self.window = tk.Tk()

        self.window.title(
            "JARVIS AI"
        )


        self.window.geometry(
            "600x500"
        )



        self.title = tk.Label(
            self.window,
            text="J.A.R.V.I.S",
            font=(
                "Arial",
                30
            )
        )


        self.title.pack(
            pady=20
        )

        self.reactor = Reactor(
        self.window
        )

        self.chat = tk.Text(
            self.window,
            height=15
        )


        self.chat.pack(
            padx=20
        )



        self.input = tk.Entry(
            self.window,
            width=50
        )


        self.input.pack(
            pady=10
        )



        self.button = tk.Button(
            self.window,
            text="SEND",
            command=self.send
        )


        self.button.pack()



        self.window.mainloop()



    def send(self):

        text = self.input.get()


        self.chat.insert(
            tk.END,
            "\nYOU : "
            + text
        )


        answer = self.jarvis.think(
            text
        )


        self.chat.insert(
            tk.END,
            "\n\nJARVIS : "
            + answer
        )


        self.input.delete(
            0,
            tk.END
        )
