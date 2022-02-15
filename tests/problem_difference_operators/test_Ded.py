from ..base import _TestDxx

class TestDed(_TestDxx):
    name = "D_ed"

    @staticmethod
    def op(f, x, dx):
        dx2 = dx/2
        dx4 = dx/4
        return (8*(f(x + dx4) - f(x - dx4)) - (f(x + dx2) - f(x - dx2)))/(3*dx)
