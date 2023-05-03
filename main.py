import tkinter
import Planets
from Planets import *

FPS = 30

tk = tkinter.Tk()
tk.geometry('1000x1000')
canvas = tkinter.Canvas(tk, width=1000, height=1000)


canvas.create_oval(10, 10, 50, 50, fill='#00FF89')

Planet(100, 100, 100, 20, canvas, velocity=[10, 0])
Planet(200, 200, 100, 20, canvas)
Planet(300, 300, 100, 20, canvas)

canvas.pack()


def game():
    Planets.tick()
    tk.after(1000 // FPS, game)

game()
tk.mainloop()