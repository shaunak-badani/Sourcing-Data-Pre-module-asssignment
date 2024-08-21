import argparse
import random


def process_args(args):
    """
    Processes a list of arguments:
      - n: Number of paragraphs, type int, required
      - min: Minimum number of words required per paragraph, optional, default - 10
      - max: Maximum number of words required per paragraph, optional, default - 20

      Returns:
      A 3-tuple (Number of paragraphs, min. no of words / paragraph, max. no of words / paragraph)
    """
    parser = argparse.ArgumentParser(description = 'Generate paragraphs of random words.')

    parser.add_argument('-n', required = True, type = int)

    parser.add_argument('--min', default = 10, type = int)
    parser.add_argument('--max', default = 20, type = int)

    args = parser.parse_args(args)
    if args.max < args.min:
        raise RuntimeError("Min can't be greater than max!")
    return args.n, args.min, args.max


def generate_words(no_of_paragraphs, min_words_per_para, max_words_per_para):
    """
    Generates a list of paragraphs. Each paragraph is a list of words
    """
    from random_word import RandomWords
    r = RandomWords()

    word = r.get_random_word()

    paragraphs = []

    for paragraph_no in range(no_of_paragraphs):
        words = []
        no_of_words = random.randint(min_words_per_para, max_words_per_para)
        for _ in range(no_of_words):
            words.append(r.get_random_word())
        paragraphs.append(words)

    return paragraphs
