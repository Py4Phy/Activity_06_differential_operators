import pytest
import numpy as np
from numpy.testing import assert_almost_equal

from ..tst import get_attribute

def quadratic_f(x):
    return 4*x**2 - 2*x + 1

def quadratic_dfdx(x):
    return 8*x - 2


class TestError:
    @staticmethod
    def D_bd(f, x, dx):
        return (f(x) - f(x-dx))/dx

    def _assert_error_function_Dbd(self, f, dfdx, x, h):
        ref = (self.D_bd(f, x, h) - dfdx(x))/dfdx(x)
        value = get_attribute("error", "diffops.py")(self.D_bd, f, dfdx, x, h)
        assert_almost_equal(value, ref,
                            err_msg=f"error() analysis function for y={f.__name__}, x={x}, and h={h} failed.")


    @pytest.mark.parametrize("h", 10.0**np.array([-10, -7, -5, -3, -2, -1]))
    @pytest.mark.parametrize("f,dfdx", [
        (np.sin, np.cos),
        (np.exp, np.exp),
        (quadratic_f, quadratic_dfdx),
    ])
    def test_error_fixed_h(self, h, f, dfdx):
        x_values = np.linspace(-20, 15, 25)
        self._assert_error_function_Dbd(f, dfdx, x_values, h)

    @pytest.mark.parametrize("t", np.linspace(-20, 15, 3))
    @pytest.mark.parametrize("f,dfdx", [
        (np.sin, np.cos),
        (np.exp, np.exp),
        (quadratic_f, quadratic_dfdx),
    ])
    def test_error_fixed_t(self, t, f, dfdx):
        h_values = 10.0**np.array([-10, -5, -3, -1])
        self._assert_error_function_Dbd(f, dfdx, t, h_values)

