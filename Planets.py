import random as rnd
from tkinter import Canvas

X = 'x'
Y = 'y'
_planets = []

class _Telo:
    def __init__(self, x, y, r, color, canvas:Canvas):
        _planets.append(self)
        self.pos = {X: x, Y: y}
        self.size = [x, y, x + r, x + y]
        self.radius = r
        self.canvas = canvas
        self.__create_color(color)

    def move(self, x, y):
        self.pos[X] += x
        self.pos[Y] += y

    def moveTo(self, x, y):
        self.pos[X] = x
        self.pos[Y] = y


    def __create_color(self, color):
        if color == '':
            r = hex(rnd.randrange(0, 80))[2:]
            g = hex(rnd.randrange(0, 256))[2:]
            b = hex(rnd.randrange(0, 256))[2:]
            if len(r) < 2:
                r = '0' + r
            if len(g) < 2:
                g = '0' + g
            if len(b) < 2:
                b = '0' + b

            self.color = f'#{r}{g}{b}'
        else:
            self.color = color

        self.object = self.canvas.create_oval(self.size, fill=self.color)


class _Fiz:
    def __init__(self, mass, velocity, isPhysic):
        self.mass = mass
        self.velocity = {X: velocity[0], Y: velocity[1]}
        self.isPhysic = isPhysic

    def setVelocity(self, x, y):
        self.velocity = {X: x, Y: y}

    def addVelocity(self, x, y):
        self.velocity[X] += x
        self.velocity[Y] += y

    def tick(self):
        self.move(self.velocity[X], self.velocity[Y])
        self.canvas.move(self.object, self.velocity[X], self.velocity[Y])



class Planet(_Telo, _Fiz):
    def __init__(self, x, y, r, mass, canvas:Canvas, color='', velocity=[0, 0], isPhysic=False):
        _Telo.__init__(self, x, y, r, color, canvas)
        _Fiz.__init__(self, mass, velocity, isPhysic)






def tick():
    for i in _planets:
        i.tick()
