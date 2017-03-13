__author__ = 'gkannappan'
'''
This is the first program for the following requirement
Create a Class named Rectangle that should take two values as input and return area as output
This should be assigned to another variable and be executed
'''


class Rect():

    def __init__(self,l,b):
        self.len=l
        self.br=b

    def FindArea(self):
        Area = (self.len * self.br)
        return Area

    def FindPerimeter(self):
        Peri = 2*(self.len + self.br)
        return Peri

if __name__ == "__main__":
    # execute only if run as a script
    r = Rect(4,6)
    a = r.FindArea()
    print "area is :", a

    p = r.FindPerimeter()
    print "peri is :", p
