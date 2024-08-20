from wordgen import process_args, generate_words
import sys

argument_list = sys.argv[1:]
n, min_words, max_words = process_args(argument_list)
print(generate_words(n, min_words, max_words))