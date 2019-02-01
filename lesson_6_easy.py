
__author__ = 'Шонтукова Арина Артуровна'

# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

class Triangle():
    def __init__(self, xa, ya, xb, yb, xc, yc):
        self.xa = xa
        self.ya = ya
        self.xb = xb
        self.yb = yb
        self.xc = xc
        self.yc = yc
        self.AB = math.sqrt(int((xb - xa)**2) + (yb - ya)**2)
        self.BC = math.sqrt(int((xc - xb)**2) + (yc - yb)**2)
        self.CA = math.sqrt(int((xa - xc)**2) + (ya - yc)**2)
        
    def perimeter(self):
        self.perimeter = (self.AB + self.BC + self.CA)
        return (self.perimeter)

    def square(self):
        self.perimeter /=2
        self.square =  math.sqrt(self.perimeter*(self.perimeter - self.AB)*(
                              self.perimeter - self.BC)* (self.perimeter - self.CA))
        return (self.square)

    def height(self):
        self.square *=2
        self.height =  self.square / self.CA
        return (self.height)
    