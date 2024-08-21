import argparse
import sys


def process_args(args):
    """
    Processes a list of arguments:
      - n: Number of paragraphs, type int, required
      - min: Minimum number of words required per paragraph, optional, default - 150
      - max: Maximum number of words required per paragraph, optional, default - 200

      Returns:
      A 3-tuple (Number of paragraphs, min. no of words / paragraph, max. no of words / paragraph)
    """
    parser = argparse.ArgumentParser(description = 'Generate paragraphs of random words.')

    parser.add_argument('-n', required = True, type = int)

    parser.add_argument('--min', default = 150, type = int)
    parser.add_argument('--max', default = 200, type = int)

    args = parser.parse_args(args)
    if args.max < args.min:
        raise RuntimeError("Min can't be greater than max!")
    return args.n, args.min, args.max

