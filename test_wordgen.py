from wordgen import process_args
import pytest
import unittest

@pytest.mark.parametrize('args, expected_tuple', [
                        (['-n', '20'], (20, 10, 20)),
                        (['-n', '4', '--max', '17'], (4, 10, 17)), 
                        (['-n', '12', '--min', '12'], (12, 12, 20))
                        ])
def test_wordgen(args, expected_tuple):
    """
    Tests proper working of the `process_args` function
    """
    program_parameters = process_args(args)
    assert program_parameters == expected_tuple
    