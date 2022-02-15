import pytest
import warnings
import numpy as np
from numpy.testing import assert_almost_equal

from .tst import get_attribute


class _TestDxx:
    name = NotImplemented
    module = "diffops.py"

    h_values = np.array([1e-3, 5e-3, 1e-2, 1e-1])

    @pytest.fixture(scope="class")
    def t_values(self):
        return np.array([-2.0, -1.0, -0.1, 0.0, 3.1e-3, 1.0, 4.2, 8.99e3])


    @staticmethod
    def op(f, x, dx):
        raise NotImplementedError

    @pytest.mark.parametrize("f", [np.sin,
                                   np.cos,
                                   np.exp,
                                   lambda t: 2*t**2 - 5*t + 0.2,
                                   lambda t: t,
                                   lambda t: 3*np.sin(10*t)/(10*t),
                                   ])
    @pytest.mark.parametrize("h", h_values)
    def test_func(self, f, t_values, h):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=RuntimeWarning)
            ref = self.op(f, t_values, h)
            value = get_attribute(self.name, self.module)(f, t_values, h)
        assert_almost_equal(value, ref,
                            decimal=5,
                            err_msg=f"{self.name}({f.__name__}, t, {h}) is not correct.")
