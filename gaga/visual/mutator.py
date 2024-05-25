from typing import List
from gaga.cga.mutator import Mutator
from gaga.visual.component import Shape
from random import randint
from copy import deepcopy
class NaiveMutatorDraw(Mutator):
    def mutateGene(self, gene: List[Shape]) -> List[Shape]:
        length=len(gene)
        mutated=[deepcopy(shape) for shape in gene]
        for i in range(int(length*0.8)):
            id=randint(0,len(gene)-1)
            mutated[id]=deepcopy(mutated[id]).mutate()
        return mutated
