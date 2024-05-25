from gaga.cga.component import Population
from gaga.cga.genetic import unsupervisedGenetic
from gaga.cga.crossover import Crossover
from gaga.cga.mutator import Mutator
from gaga.cga.selector import Selector,NaiveSelector
from gaga.visual.component import Image
from gaga.visual.plot import Plot
from gaga.visual.mutator import NaiveMutatorDraw
 
class unsupervisedGeneticDraw(unsupervisedGenetic):
    def __init__(self,
                 mutator: Mutator,
                 population: Population,
                 plot: Plot,
                 selector: Selector = NaiveSelector,
                 crossover: Crossover = None) -> None:
        super().__init__(mutator, population, selector, crossover)
        self.plot=plot
        print("generation:%s" % self.population.generation)
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
