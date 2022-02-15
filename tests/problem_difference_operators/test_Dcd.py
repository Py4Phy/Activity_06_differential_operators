from ..base import _TestDxx

class TestDcd(_TestDxx):
    name = "D_cd"

    @staticmethod
    def op(f, x, dx):
        dx2 = dx/2
        return (f(x + dx2) - f(x - dx2))/dx
