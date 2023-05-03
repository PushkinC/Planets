import math
from Planets import _Fiz, _Telo

X = 'x'
Y = 'y'
G = 6.7 * 10 ** -11
PIXEL = (1.5 * 10 ** 11) / 900



def tick(planets):
    for i in range(len(planets)):
        if planets[i].isPhysic:
            for j in range(i + 1, len(planets)):
                a = __get_Force(planets[j], planets[i]) / planets[i].mass * 1000000
                s = math.atan2(planets[j].pos[Y] - planets[i].pos[Y], planets[j].pos[X] - planets[i].pos[X])
                ax = a * math.cos(s) / PIXEL
                ay = a * math.sin(s) / PIXEL

                planets[i].addVelocity(ax, ay)





def __get_Distance(a: _Telo, b: _Telo) -> float:
    import math
    return math.sqrt(((a.pos[X] - b.pos[X]) ** 2 + (a.pos[Y] - b.pos[Y]) ** 2)) * PIXEL

def __get_Force(a: _Fiz, b: _Fiz) -> float:
    return G * (a.mass * b.mass) / __get_Distance(a, b) ** 2