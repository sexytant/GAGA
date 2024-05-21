from gaga.general.component import Base,Codon,Individual
from typing import Sequence,List

class Shape(Codon):
    def __init__(self,id,type,params: Sequence[Base]):
        super().__init__(id,type,params)
    
class Image(Individual):
    def __init__(self,id,shapes: List[Shape],score:float):
        super().__init__(id,shapes,score)