import tkinter as tk
import math


class Reactor:


    def __init__(
        self,
        window
    ):

        self.canvas = tk.Canvas(
            window,
            width=200,
            height=200
        )

        self.canvas.pack()


        self.angle = 0


        self.animate()



    def animate(self):

        self.canvas.delete(
            "all"
        )


        cx = 100
        cy = 100


        # lingkaran utama

        self.canvas.create_oval(
            40,
            40,
            160,
            160
        )


        self.canvas.create_oval(
            70,
            70,
            130,
            130
        )


        # titik mutar

        for i in range(8):

            a = (
                self.angle
                + i * 45
            )


            x = (
                cx
                + math.cos(
                    math.radians(a)
                )
                * 80
            )

            y = (
                cy
                + math.sin(
                    math.radians(a)
                )
                * 80
            )


            self.canvas.create_oval(
                x-5,
                y-5,
                x+5,
                y+5
            )



        self.angle += 5


        self.canvas.after(
            50,
            self.animate
        )
