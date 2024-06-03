from abc import ABC,abstractmethod
from gaga.cga.mutator import Mutator
from gaga.cga.component import Creator,Evaluator
from gaga.cga.selector import Selector, NaiveSelector
from gaga.cga.crossover import Crossover

class GA(ABC):
    def __init__(self,
                 creator:Creator,
                 mutator:Mutator,
                 selector:Selector,
                 crossover:Crossover,
                 evaluator:Evaluator,
                 populationSize:int) -> None:
        self.creator=creator
        self.mutator=mutator
        self.selector=selector
        self.crossover=crossover
        self.evaluator=evaluator
        self.population=self.creator.create(popSize=populationSize)
        self.generation=0
    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def step(self):
        pass
    
    def run(self,iter):
        while(self.generation<iter):
            self.evaluate()
            self.step()
            self.generation=self.generation+1


"""
class unsupervisedGenetic(GA):
    def step(self):
        elite=self.selector.select(self.population)
        self.population.generation=self.population.generation+1
        self.population.individuals[0]=elite
        gene=elite.gene
        for i in range(1,self.population.size):
            child=Individual((self.population.size-1)*self.population.generation+i,
                             gene.copy(),
                             None)
            self.population.individuals[i]=child

    def elect(self):
        vote=[]
        for i in range(self.population.size):
            vote.append(int(input(prompt="id {}:".format(self.population.individuals[i].id))))
        total=sum(vote)
        for i in range(self.population.size):
            self.population.individuals[i].score=1.0-vote[i]/total
"""