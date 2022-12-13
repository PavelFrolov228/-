class FigureColor:

def __init__(self, r=1, g=0, b=0):
self.__R = R
self.__B = B
self.__G = G

def get_color(self):
return (self.__R, self.__B,self.__G)

def set_color(self,R,G,B):
self.__R = R
self.__B = B
self.__G = G

def __repr__(self):
return f"R:{self.__R}, B:{self.__B}, G:{self.__G}"
