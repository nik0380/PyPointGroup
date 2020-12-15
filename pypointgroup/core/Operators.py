import numpy as np
from collections.abc import Iterable
from itertools import product

class Operator:

    def __init__(self, name:str=None, m:np.ndarray=None):
        self.m = m
        self.name = name
        self.hash = None

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return np.array_equal(self.m, other.m)

    def __ne__(self, other):
        return not np.array_equal(self.m, other.m)

    def __mul__(self, other):
        return Operator(name = "%s %s" % (self.name, other.name), m = np.matmul(self.m, other.m))

    def __hash__(self):
        if self.hash is None:
            p = np.array([3**i for i in range(9)])
            self.hash = int(((self.m.reshape(9) + 1) * p).sum())
        return self.hash


#========================================================================

class SymmetryGroup(set):

    def __init__(self, items=None):

        super().__init__()

        if items:
            if isinstance(items, Iterable):
                self.update(items)
            elif isinstance(items, Operator):
                self.add(items)

    def GenerateGroup(self):

        flag = True
        while flag:
            new = [o1 * o2 for o1, o2 in product(self,self)]
            lx1 = len(self)
            self.update(new)
            flag = len(self) > lx1

        return self
