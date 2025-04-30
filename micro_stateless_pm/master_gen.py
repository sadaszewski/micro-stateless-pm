from argparse import ArgumentParser
import csv
import math
import os
import unicodedata
from .__main__ import clear_screen


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('--number-of-words', '-n', type=int, default=3)
    parser.add_argument('--dictionary', '-d', type=str, required=True, help='Recommended dictionary: https://sjp.pl/sl/odmiany/')
    parser.add_argument('--compute-entropy-without-diacritics', '-c', action='store_true')
    return parser


def load_words(filename):
    res = []
    with open(filename, "r", encoding='utf8') as f:
        for row in csv.reader(f):
            res.extend([ s.strip() for s in row ])
    res = set(res)
    return res


def strip_diacritics(s):
    res = ''.join([ c for c in unicodedata.normalize('NFD', s) if not unicodedata.combining(c) ])
    res = res.replace('ł', 'l').replace('Ł', 'L')
    return res


def main():
    parser = create_parser()
    args = parser.parse_args()
    word_selection = load_words(args.dictionary)
    print('Size of word selection:', len(word_selection))
    entropy = math.log2(len(word_selection)) * args.number_of_words
    print('Entropy:', entropy)
    if args.compute_entropy_without_diacritics:
        word_selection_no_diacritics = set([ strip_diacritics(w) for w in word_selection ])
        print('Size of word selection (no diacritics):', len(word_selection_no_diacritics))
        entropy = math.log2(len(word_selection_no_diacritics)) * args.number_of_words
        print('Entropy (no diacritics):', entropy)
    word_selection = list(word_selection)
    # print(word_selection[:4])
    res = []
    for _ in range(args.number_of_words):
        random_index = int(''.join([ '%02x' % x for x in os.urandom(32) ]), 16) % len(word_selection)
        res.append(word_selection[random_index])
    res = ' '.join(res)
    print('Result:', res)
    print('Without diacritics:', strip_diacritics(res))
    input()
    clear_screen()

    # int()


if __name__ == '__main__':
    main()
