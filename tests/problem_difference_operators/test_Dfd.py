from ..base import _TestDxx

class TestDfd(_TestDxx):
    name = "D_fd"

    @staticmethod
    def op(f, x, dx):
        return (f(x+dx) - f(x))/dx
