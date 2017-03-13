__author__ = 'gkannappan'

'''
Call By Reference

'''
from Rect import Rect

class Shape():

    def FindArea(self, r):
        self.ar = r.leng * r.brdt
        print "Area of the Rect is :", self.ar

if __name__ == "__main__":
    s = Shape()
    a = s.FindArea(Rect(30, 40))