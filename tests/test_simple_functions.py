import pytest
import numpy as np

from simple_functions import my_sum, factorial, trig_function

class TestSimpleFunctions(object):
    '''Class to test our simple functions are working correctly'''

    @pytest.mark.parametrize('iterable, expected', [
        ([8, 7, 5], 20),
        ((10, -2, 5, -10, 1), 4)
    ])
    def test_my_add(self, iterable, expected):
        '''Test our add function'''
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize('number, expected', [
        (5, 120),
        (3, 6),
        (1, 1)
    ])
    def test_factorial(self, number, expected):
        '''Test our factorial function'''
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize('number, expected', [
        (8, 0.989),
        (12, -0.537),
        (25, -0.132)
    ])
    def test_trig_function(self, number, expected):
        '''Test our factorial function'''
        answer = round(np.sin(number), 3)
        assert answer == expected
