from abc import ABC
from gaga.cga.mutator import Mutator
from gaga.cga.component import Population, Individual
from gaga.cga.selector import Selector, NaiveSelector
from gaga.cga.crossover import Crossover


class Genetic(ABC):
    def __init__(self,mutator:Mutator,
                 population: Population,
                 selector:Selector =NaiveSelector,
                 crossover:Crossover=None) -> None:
        self.mutator=mutator
        self.population=population
        self.mostfit=population.individuals[0]
        self.selector=selector
        self.crossover=crossover

    def step(self):
        raise NotImplementedError
    
    def run(self,iter):
        while(self.population.generation<iter):
            self.step()

class unsupervisedGenetic(Genetic):
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