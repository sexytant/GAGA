from gaga.general.component import Population
from gaga.general.genetic import unsupervisedGenetic
from gaga.general.crossover import Crossover
from gaga.general.mutator import Mutator
from gaga.general.selector import Selector,NaiveSelector
from gaga.visual.component import Image
from gaga.visual.plot import Plot
from gaga.visual.mutator import NaiveMutatorDraw
 
class unsupervisedGeneticDraw(unsupervisedGenetic):
    def __init__(self,
                 mutator: Mutator,
                 population: Population,
                 selector: Selector = NaiveSelector,
                 crossover: Crossover = None) -> None:
        super().__init__(mutator, population, selector, crossover)
        self.plot=Plot()
        self.plot.expressPopulation(self.population)
        self.elect()

    def step(self):
        elite=self.selector.select(self.population)
        self.population.generation=self.population.generation+1
        self.population.individuals[0]=elite
        gene=elite.gene
        mutator=NaiveMutatorDraw()
        for i in range(1,self.population.size):
            child=Image((self.population.size-1)*self.population.generation+i,
                             mutator.mutateGene(gene),
                             None)
            self.population.individuals[i]=child
        self.plot.expressPopulation(self.population)
        self.elect()
