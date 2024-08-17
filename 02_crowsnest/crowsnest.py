#!/usr/bin/env python3
"""
Author : Eric Grembocki <egrembocki@gmail.com>
Date   : 2024-07-18
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crow\'s Nest -- choose the correct article',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    parser.add_argument('-s',
                        '--side',
                        metavar='side',
                        default='larboard',
                        help='Side of boat')

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    side = args.side
    word = args.word

    if word[0] in 'AEIOU':
        article = 'An'
    elif word[0] in 'aeiou':
        article = 'an'
    elif word[0].isupper():
        article = 'A'
    else:
        article = 'a'

    print(f'Ahoy, Captain, {article} {word} off the {side} bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
