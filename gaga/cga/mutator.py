from abc import ABC,abstractmethod
from gaga.cga.component import Codon

from typing import List

class Mutator(ABC):
    #def __init__(self,probability: Probability):
    #    self.probability=probability
    @abstractmethod
    def mutateGene(self,Gene: List[Codon]) -> List[Codon]:
        raise NotImplementedError