from abc import ABC,abstractmethod
from typing import List,Sequence

class Base:
    def __init__(self,id:int,type:str,letter:object) -> None:
        self.setId(id)
        self.setType(type)
        self.setLetter(letter)
    def setId(self,value):
        self._id=value
    def setType(self,value):
        self._type=value
    def getId(self):
        return self._id
    def getType(self):
        return self._type
    def getLetter(self):
        return self._letter
    def setLetter(self,value):
        self._letter=value

def defBase(className:str,idLabel:str,typeLabel:str,letterLabel:str):
    NewBase=type(className, (Base,), {})
    def getX(self):
        return self._id
    def setX(self,value):
        self.setId(value)
    def getY(self):
        return self._type
    def setY(self,value):
        self.setType(value)
    def getZ(self):
        return self._letter
    def setZ(self,value):
        self.setLetter(value)

    setattr(NewBase,idLabel,property(getX,setX))
    setattr(NewBase,typeLabel,property(getY,setY))
    setattr(NewBase,letterLabel,property(getZ,setZ))
    newBase=NewBase
    return newBase

class Codon:
    def __init__(self,id:int,type:str,basis: Sequence[Base]) -> None:
        self.setId(id)
        self.setType(type)
        self.setBasis(basis)
    def setId(self,value):
        self._id=value
    def setType(self,value):
        self._type=value
    def getId(self):
        return self._id
    def getType(self):
        return self._type
    def getBasis(self):
        return self._basis
    def setBasis(self,value):
        self._basis=value
        
def defCodon(className:str,idLabel,typeLabel,basisLabel) -> Codon:
    NewCodon=type(className, (Codon,), {})
    def getX(self):
        return self._id
    def setX(self,value):
        self.setId(value)
    def getY(self):
        return self._type
    def setY(self,value):
        self.setType(value)
    def getZ(self):
        return self._basis
    def setZ(self,value):
        self.setBasis(value)

    setattr(NewCodon,idLabel,property(getX,setX))
    setattr(NewCodon,typeLabel,property(getY,setY))
    setattr(NewCodon,basisLabel,property(getZ,setZ))
    newCodon=NewCodon
    return newCodon
        
class Individual(ABC):
    def __init__(self,id: int,gene,score: float):
        self.setId(id)
        self.setGene(gene)
        self.setScore(score)
    def setId(self,value):
        self._id=value
    def setGene(self,value):
        self._gene=value
    def getId(self):
        return self._id
    def getGene(self):
        return self._gene
    def getScore(self):
        return self._score
    def setScore(self,value):
        self._score=value    

def defIndividual(className:str,idLabel,geneLabel,scoreLabel) -> Codon:
    NewIndividual=type(className, (Individual,), {})
    def getX(self):
        return self._id
    def setX(self,value):
        self.setId(value)
    def getY(self):
        return self._gene
    def setY(self,value):
        self.setGene(value)
    def getZ(self):
        return self._score
    def setZ(self,value):
        self.setScore(value)

    setattr(NewIndividual,idLabel,property(getX,setX))
    setattr(NewIndividual,geneLabel,property(getY,setY))
    setattr(NewIndividual,scoreLabel,property(getZ,setZ))
    newIndividual=NewIndividual
    return newIndividual
  
class Population:
    def __init__(self,size:int,generation: int,individuals: List[Individual]):
        self.size=size
        self.generation=generation
        self.individuals=individuals

class Creator(ABC):
    @abstractmethod
    def create(self,popSize):
        raise NotImplementedError

class Evaluator(ABC):
    @abstractmethod
    def evaluate(individiaul:Individual):
        NotImplementedError
