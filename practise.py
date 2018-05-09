class Point:
    def __init__(self,x,y,z,h):
        self._x = x
        self._y = y
        self._z = z
        self._h = h
    def distanceFromOrigin(self):
        return ((self._x-self._z) **2 + (self._y-self._h) ** 2)**.5
