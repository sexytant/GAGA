from abc import ABC,abstractmethod
from gaga.cga.component import Codon,Individual,Population

class Express(ABC):
    @abstractmethod
    def expressCodon(self,codon:Codon):
        raise NotImplementedError
    @abstractmethod
    def expressIndividual(self,individual:Individual):
        raise NotImplementedError
    @abstractmethod
    def expressPopulation(self,population:Population):
        raise NotImplementedError