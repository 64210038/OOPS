from unittest.util import _count_diff_hashable

class Area:
    def __init__(self) -> None:
        self.__base = 0
        self.__high = 0

    @property #getter base
    def base(self):
        return self.__base

    @base.setter
    def base(self,value):
        self.__base = value

    @property #getter high
    def high(self):
        return self.__high

    @high.setter
    def high(self,value):
        self.__high = value

    def compute_area(self):
        return 0.5 * self.base * self.high
        