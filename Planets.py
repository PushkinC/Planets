import random as rnd
from tkinter import Canvas


X = 'x'
Y = 'y'
_planets = []

class _Telo:
    def __init__(self, x, y, r, color, canvas:Canvas):
        _planets.append(self)
        self.pos = {X: x, Y: y}
        self.size = [x - r / 2, y  - r / 2, x + r / 2, y + r / 2]
        self.radius = r
        self.canvas = canvas
        self.color = color

        self.object = self.canvas.create_oval(self.size, fill=self.color)

    def move(self, x, y):
        self.pos[X] += x
        self.pos[Y] += y

    def moveTo(self, x, y):
        self.pos[X] = x
        self.pos[Y] = y




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




class _Track:
    def __init__(self):
        self.ti = 0
        self.last_pos = 0
        self.track = []


    def tick(self):
        _Fiz.tick(self)
        self.ti += 1
        if self.last_pos == 0:
            self.last_pos = self.pos.copy()
            return
        if self.ti % 100 == 0:
            self.track.append(self.canvas.create_line(self.last_pos[X], self.last_pos[Y], self.pos[X], self.pos[Y], fill=self.color, width=2))
            self.last_pos = self.pos.copy()
        if len(self.track) > 10:
            self.canvas.delete(self.track[0])
            del self.track[0]








class Planet(_Track, _Telo, _Fiz):
    def __init__(self, x, y, rad, mass, canvas:Canvas, color='', velocity=[0, 0], isPhysic=False):
        if color == '':
            r = hex(rnd.randrange(0, 80))[2:]
            if rnd.randint(1, 2) == 1:
                g = hex(rnd.randrange(200, 256))[2:]
            else:
                g = hex(rnd.randrange(0, 120))[2:]
            b = hex(256 - int(g, 16))[2:]
            if len(r) < 2:
                r = '0' + r
            if len(g) < 2:
                g = '0' + g
            if len(b) < 2:
                b = '0' + b

            color = f'#{r}{g}{b}'

        _Track.__init__(self)
        _Telo.__init__(self, x, y, rad, color, canvas)
        _Fiz.__init__(self, mass, velocity, isPhysic)





class Star(_Track, _Telo, _Fiz):
    def __init__(self, x:int, y:int, rad:int, mass:int, canvas:Canvas, color='', velocity=[0, 0], isPhysic=False):
        if color == '':
            r = hex(rnd.randrange(200, 256))[2:]
            g = hex(rnd.randrange(200, 256))[2:]
            b = hex(rnd.randrange(0, 100))[2:]
            if len(r) < 2:
                r = '0' + r
            if len(g) < 2:
                g = '0' + g
            if len(b) < 2:
                b = '0' + b

            color = f'#{r}{g}{b}'

        _Track.__init__(self)
        _Telo.__init__(self, x, y, rad, color, canvas)
        _Fiz.__init__(self, mass, velocity, isPhysic)



def tick():
    for i in _planets:
        i.tick()
