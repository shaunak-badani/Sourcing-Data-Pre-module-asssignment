from wordgen import process_args
from wordgen import generate_words
import pytest
import unittest

@pytest.mark.parametrize('args, expected_tuple', [
                        (['-n', '20'], (20, 10, 20)),
                        (['-n', '4', '--max', '17'], (4, 10, 17)), 
                        (['-n', '12', '--min', '12'], (12, 12, 20))
                        ])
def test_arguments_parse(args, expected_tuple):
    """
    Tests proper working of the `process_args` function
    """
    program_parameters = process_args(args)
    assert program_parameters == expected_tuple


@pytest.mark.parametrize('n, min_words_per_para, max_words_per_para', [
                        (2, 10, 19),
                        (4, 10, 17), 
                        (6, 12, 20)
                        ])
def test_wordgen(n, min_words_per_para, max_words_per_para):
    """
    Sanity test for the number of paragraphs, and that each paragraph has number of words in given range
    """
    paragraph = generate_words(n, min_words_per_para, max_words_per_para)
    assert len(paragraph) == n

    for words in paragraph:
        assert(len(words) >= min_words_per_para and len(words) <= max_words_per_para)
    