__author__ = 'gkannappan'

'''
Defining a class called shape that ll just print the area
Two more classes (Rectangle and Circle) ll calculate the area
'''

class Shape():

    def __init__(self, a):
        self.ar = a

    def printArea(self):
        print "Calculated Area is : ", self.ar

class Rect(Shape):

    def __init__(self, l, b):
        self.leng = l
        self.brdt = b

    def FindArea(self):
        self.ar = (self.leng * self.brdt)
        self.printArea()

class Cir(Shape):

    def __init__(self, r):
        self.rad = r

    def FindArea(self):
        self.ar = (self.rad * self.rad)
        self.printArea()


if __name__ == "__main__":
    #r = Rect(2,3)
    c = Cir(5)
    a = c.FindArea()