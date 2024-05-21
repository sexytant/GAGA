from abc import ABC,abstractmethod
from gaga.general.component import Individual

class Fitness(ABC):
    @abstractmethod
    def evaluate(individual: Individual) -> float:
        raise NotImplementedError

