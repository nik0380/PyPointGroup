from ._opers import POINT_OPERATORS
import numpy as np
from pypointgroup.core.Operators import Operator, SymmetryGroup

class Symmetry(dict):

    def __init__(self) -> None:
        super().__init__()
        self.update(POINT_OPERATORS)

    @property
    def Count(self):
        return len(self)

    def GetOperator(self, name:str):
        return Operator(name, self[name])

    def GetOperatorOfNumber(self, number: int):
        keys = list(self.keys())
        return Operator(keys[number], self[keys[number]])

    def GetName(self, oper)->str:

        if isinstance(oper, Operator): oper = oper.m

        for key, opr in self.items():
            if np.array_equal(oper, opr):
                return key

        return None

    def Add(self, name:str, Operator):
        self[name] = Operator

    def Delete(self, name:str):
        if name in self:
            del self[name]

    def GenGroup(self, gens:list):

        def __do(opr):
            name = self.GetName(opr)
            opr.name = name
            return name

        def __get_opr(opr):
            if isinstance(opr, str):
                return self.GetOperator(opr)
            elif isinstance(opr, Operator):
                return opr
            else:
                raise Exception('Invalid operator type: ', type(opr))

        g = SymmetryGroup([__get_opr(opr) for opr in gens])
        g.GenerateGroup()
        ng = [__do(opr) for opr in g]

        return ng, g
