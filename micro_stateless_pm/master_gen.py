from argparse import ArgumentParser
import csv
import math
import os
import unicodedata
from .__main__ import clear_screen
from .password import CHARACTER_SUBSETS


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('--number-of-words', '-n', type=int, default=3)
    parser.add_argument('--dictionary', '-d', type=str, required=True, help='Recommended dictionary: https://sjp.pl/sl/odmiany/')
    parser.add_argument('--compute-entropy-without-diacritics', '-c', action='store_true')
    parser.add_argument('--add-number', '-a', action='store_true')
    parser.add_argument('--add-symbol', '-s', action='store_true')
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


def random_int():
    return int(''.join([ '%02x' % x for x in os.urandom(32) ]), 16) 


def compute_entropy(word_selection, args):
    entropy = math.log2(len(word_selection)) * args.number_of_words
    if args.add_symbol:
        entropy += math.log2(len(CHARACTER_SUBSETS['symbols']))
    if args.add_number:
        entropy += math.log2(2 * 9)
    return entropy


def main():
    parser = create_parser()
    args = parser.parse_args()
    word_selection = load_words(args.dictionary)
    print('Size of word selection:', len(word_selection))
    print('Entropy:', compute_entropy(word_selection, args))
    if args.compute_entropy_without_diacritics:
        word_selection_no_diacritics = set([ strip_diacritics(w) for w in word_selection ])
        print('Size of word selection (no diacritics):', len(word_selection_no_diacritics))
        print('Entropy (no diacritics):', compute_entropy(word_selection_no_diacritics, args))
    word_selection = list(word_selection)
    # print(word_selection[:4])
    res = []
    for _ in range(args.number_of_words):
        random_index = random_int() % len(word_selection)
        res.append(word_selection[random_index])
    if args.add_symbol:
        res.append(CHARACTER_SUBSETS['symbols'][random_int() % len(CHARACTER_SUBSETS['symbols'])])
    if args.add_number:
        for _ in range(2):
            res.append(str(1 + random_int() % 9))
    # res = ' '.join(res)
    print('Result:', ' '.join(res))
    print('Without diacritics:', strip_diacritics(' '.join(res)))
    print('Without spaces:', strip_diacritics(''.join(res)))
    input()
    clear_screen()

    # int()


if __name__ == '__main__':
    main()
