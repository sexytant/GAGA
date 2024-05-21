from gaga.visual.component import Shape
from typing import Sequence
from gaga.general.component import Base
from random import randint,random

class Ellipse(Shape):
    def __init__(self,id,params: Sequence[Base],ellipseSize):
        if(self.check(params)):
            super().__init__(id,"Ellipse",params)
            self.ellipseSize=ellipseSize
    def check(self,params:Sequence[Base]) -> bool:
        if len(params)==7:
            #TODO
            return True
        else:
            return False
    def mutate(self):
        mutateType=randint(0,6)
        if mutateType==0:
            self.basis["x"].letter=random()
        elif mutateType==1:
            self.basis["y"].letter=random()
        elif mutateType==2:
            self.basis["width"].letter=random()*self.ellipseSize
        elif mutateType==3:
            self.basis["height"].letter=random()*self.ellipseSize
        elif mutateType==4:
            self.basis["red"].letter=0
        elif mutateType==5:
            self.basis["green"].leter=0
        elif mutateType==6:
            self.basis["blue"].letter=0
        return self
