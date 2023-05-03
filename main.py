import tkinter
import Planets
from Planets import *
import PlanetPhysics

FPS = 1000
print(400000000 / PlanetPhysics.PIXEL)

tk = tkinter.Tk()
tk.geometry('2000x2000')
canvas = tkinter.Canvas(tk, width=2000, height=2000)


Planet(1000, 100, 50, 6 * 10 ** 24, canvas, velocity=[30000 * 1000 / PlanetPhysics.PIXEL, 0], isPhysic=True)
Planet(1000, 100, 15, 7.35 * 10 ** 22, canvas, velocity=[30000 * 1000 / PlanetPhysics.PIXEL, -1000 * 1000 / 60 / 60 * 1060 / PlanetPhysics.PIXEL], isPhysic=True)

Star(1000, 1000, 100, 2 * 10 ** 30, canvas)


canvas.pack()


def game():
    Planets.tick()
    PlanetPhysics.tick(Planets._planets)
    tk.after(1000 // FPS, game)

game()
tk.mainloop()


# Земля Cолнце 1.5 * 10 ** 11
