from abc import ABC,abstractmethod
from typing import List,Sequence

class Base(ABC):
    def __init__(self,id:int,type:str,letter:object) -> None:
        self.id=id
        self.type=type
        self.letter=letter

class Codon(ABC):
    def __init__(self,id:int,type:str,basis: Sequence[Base]) -> None:
        self.id=id
        self.type=type
        self.basis=basis
        
class Individual(ABC):
    def __init__(self,id: int,gene: List[Codon],score: float):
        self.id=id
        self.gene=gene
        self.score=score
  
class Population:
    def __init__(self,size:int,generation: int,individuals: List[Individual]):
        self.size=size
        self.generation=generation
        self.individuals=individuals




