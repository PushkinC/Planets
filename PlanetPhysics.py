

def __get_distance(self, a: _Telo, b: _Telo) -> float:
    import math
    return math.sqrt((a.pos[X] - b.pos[Y]) ** 2 + (a.pos[Y] * b.pos[Y]) ** 2)


def __get_Force(self, a: _Telo, b: _Telo):