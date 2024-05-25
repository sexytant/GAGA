from abc import ABC,abstractmethod
import random
"""
確率
StaticProbabilityとDynamicRangeProbability
"""
class Probability(ABC):
    @abstractmethod
    def next() -> float:
        raise NotImplemented

"""
なんの変哲もない確率
"""
class StaticProbability(Probability):
    def __init__(self,const: float) -> None:
        self.const=const
    def next(self) -> float:
        return self.const

"""
範囲が変化する確率
@param min 最小値
@param max 最大値
"""
class DynamicRangeProbability(Probability):
    def __init__(self,min: float,max:float) -> None:
        self.min=min
        self.max=max
    def next() -> float:
        return min + random.random() * (max - min)
