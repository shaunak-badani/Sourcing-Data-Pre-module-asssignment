from wordgen import process_args
import pytest
import unittest

@pytest.mark.parametrize('args, expected_tuple', [
                        (['-n', '20'], (20, 150, 200)),
                        (['-n', '4', '--max', '170'], (4, 150, 170)), 
                        (['-n', '12', '--min', '160'], (12, 160, 200))
                        ])
def test_wordgen(args, expected_tuple):
    """
    Tests proper working of the `process_args` function
    """
    program_parameters = process_args(args)
    assert program_parameters == expected_tuple
    