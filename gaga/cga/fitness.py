from abc import ABC,abstractmethod
from gaga.cga.component import Individual

class Fitness(ABC):
    @abstractmethod
    def evaluate(individual: Individual) -> float:
        raise NotImplementedError

