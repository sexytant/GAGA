from gaga.general.component import Base,Codon,Individual
from typing import Sequence,List

class Param(Base):
    def __init__(self, id: int, type: str, letter: object) -> None:
        if self.check(type,object):
            super().__init__(id, type, letter)
        else:
            raise SystemError
    #TODO
    def check(type: str,letter: object) -> bool:
        if type=="x" or type=="y":
            if letter > 0.0 and letter < 1.0:
                return True
            else:
                return False
        elif type=="width" or type=="height":
            return True
        elif type in ("red","green","blue"):
            return True
        else:
            return False
        
class Shape(Codon):
    def __init__(self,id,type,params: Sequence[Param]):
        super().__init__(id,type,params)
    
class Image(Individual):
    def __init__(self,id,shapes: List[Shape],score:float,parent=None):
        super().__init__(id,shapes,score)
        self.parent=parent
        if self.parent==None:
            self.displayName=str(id)
        else:
            self.displayName="{}({})".format(id,parent)