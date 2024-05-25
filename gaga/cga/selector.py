from abc import ABC,abstractmethod
from gaga.general.component import Individual, Population
from random import random
from typing import List

"""
 * Selectorは関数selectをもつ.
 * 関数Selectorは個体群を引数
"""
class Selector(ABC):
    @abstractmethod
    def select(population: Population) -> List[Individual]:
        raise NotImplemented

class NaiveSelector(Selector):
    def select(population: Population) -> Individual:
        for i in range(population.size):
            print(population.individuals[i].id,population.individuals[i].score)
        elite=sorted(population.individuals,key=lambda individual: individual.score)[0]
        print("selected {}".format(elite.id))
        return elite
"""
確率的な淘汰
"""
class StochasticSelector(Selector):
    def __init__(self,biasRate: float):
        self.biasRate=biasRate
    """
    // given a sorted list of individuals select individuals with a decreasing probability of
    // rand(0, 1) < (n - i)/(n + 1) where n is the size of the population and i is the ith individual.
    // i = 0 is the most fit
    // always leave at least one individual
    /**
     * ここでのselect関数は, 
     * 
     * すくなくとも, 1つの個体は生き残る.
     */
    """
    def select(self,population: Population) -> Individual:
        bias = population.size * self.biasRate
        i=0
        for individual in population:
            if i > 0:
                if (random() <= (population.size - i) / (population.size + bias)):
                    return individual
            i=i+1
        return population.first()

"""
 * トーナメント式の選択
 * @param トーナメントサイズ
"""
class TournamentSelector(Selector):
    def __init__(self,tournamentSize: int) : 
        self.tournamentSize=tournamentSize
    """
     * ここでの淘汰は次のようにして行われる.
     * 個体群の中から, トーナメントサイズだけ個体をとりだした上で
     * もっとも適合している(fitnessの値が小さい)個体をとりだす.
    """
    def select(self,population: Population) -> Individual :
        tournament = []
        for i in range(self.tournamentSize):
            tournament.add(population.get(random.nextInt(population.size)))
        #TODO tournamentのindividualをそれぞれのfitnessに基づいてソート
        return tournament.first()