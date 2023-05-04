import tkinter
import Planets
from Planets import *
import PlanetPhysics

FPS = 1000

tk = tkinter.Tk()
tk.geometry('2000x2000')
canvas = tkinter.Canvas(tk, width=2000, height=2000)


Planet(1000, 100, 1 * 3.66, 6 * 10 ** 24, canvas, velocity=[30000 * 1000 / PlanetPhysics.PIXEL, 0], isPhysic=True, color='#0000FF')
Planet(1000 - 4, 100, 1, 7.35 * 10 ** 22, canvas, velocity=[30000 * 1005 / PlanetPhysics.PIXEL, -1000 * 1000 / 60 / 60 * 1000 / PlanetPhysics.PIXEL], isPhysic=True, color='#A0A0A0')

Star(1000, 1000, 1 * 3.66 * 109, 2 * 10 ** 30, canvas, isPhysic=True)


canvas.pack()


def game():
    Planets.tick()
    PlanetPhysics.tick(Planets._planets)
    tk.after(1000 // FPS, game)

game()
tk.mainloop()


# Земля Cолнце 1.5 * 10 ** 11
# 1737
# 6371
# 700000

