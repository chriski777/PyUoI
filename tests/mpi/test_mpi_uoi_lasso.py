import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal_nulp

from pyuoi import UoI_Lasso
from mpi4py import MPI


def test_variable_selection():
    """Test basic functionality of UoI_Lasso and that it finds right model"""
    from sklearn.datasets import make_regression
    X, y, w = make_regression(coef=True, random_state=1)
    lasso = UoI_Lasso(comm=MPI.COMM_WORLD, random_state=1)
    lasso.fit(X, y)
    true_coef = np.nonzero(w)[0]
    fit_coef = np.nonzero(lasso.coef_)[0]
    assert_array_equal(true_coef, fit_coef)
    assert_array_almost_equal_nulp(true_coef, fit_coef)


if __name__ == '__main__':
    test_variable_selection()
