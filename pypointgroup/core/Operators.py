import numpy as np
from collections.abc import Iterable
from itertools import product
from io import StringIO

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

    def toHTML(self, name=None)->str:
        if not name: name = self.name
        tab = f"""
        <table>
        <tr><td colspan=3>{name}</td></tr>
        <tr> <td>{self.m[0,0]}</td> <td>{self.m[0,1]}</td> <td>{self.m[0,2]}</td></tr>
        <tr> <td>{self.m[1,0]}</td> <td>{self.m[1,1]}</td> <td>{self.m[1,2]}</td></tr>
        <tr> <td>{self.m[2,0]}</td> <td>{self.m[2,1]}</td> <td>{self.m[2,2]}</td></tr>
        </table>
        """
        return tab
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

            if lx1 > 48:
                raise Exception("Group generators are set incorrectly!")

        return self

    def toHTML(self)->str:

        buf = StringIO()

        buf.write("<html><head></head><body>")

        buf.write("<h1 align=center>Cayley table</h1>")

        buf.write(self.getCayleyTabAsHTML())

        buf.write("\n<hr>\n")

        buf.write("<h1 align=center>Operators</h1>")

        for i, opr in enumerate(self):
            buf.write(opr.toHTML(name=f"Q<sub>{i+1}<sub>"))
            #buf.write("<br>")

        buf.write("</body></html>")

        return buf.getvalue()

    def getCayleyTabAsHTML(self)->str:

        data, n = self.getCayleyTab()

        buf = StringIO()

        buf.write(f'<table cellspacing="2" border="1" cellpadding="5" width="{n*60}">\n')

        for row in data:
            buf.write("<tr>")
            for item in row:
                buf.write(f"<td>{item}</td>")
            buf.write("</tr>\n")

        buf.write("</table>")

        return buf.getvalue()

    def getCayleyTab(self):

        opers = list(self)
        n = len(opers)
        data = [["-" for j in range(n+1)] for i in range(n+1)]

        for i, o in enumerate(opers):
            data[0][i+1] = data[i+1][0] = f"<b>Q<sub>{i+1}<sub></b>"#o.name


        for i, o1 in enumerate(opers):
            for j, o2 in enumerate(opers):
                o = o1*o2
                ix = opers.index(o)
                data[i+1][j+1] = f"Q<sub>{ix+1}<sub>"#opers[ix].name

        return data, n