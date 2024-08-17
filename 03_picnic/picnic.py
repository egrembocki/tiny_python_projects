#!/usr/bin/env python3
"""
Author : Eric Grembocki <egrembocki@gmail.com>
Date   : 2024-07-25
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')
    
    parser.add_argument('-o',
                        '--oxford',
                        help='Remove the oxford comma',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Let's go on a picnic"""

    args = get_args()
    items = args.positional
    sortbool = args.sorted
    oxford = args.oxford

    if not sortbool:
        if len(items) == 1:
            print('You are bringing ' + items[0] + '.')
        if len(items) == 2:
            print('You are bringing ' + ' and '.join(items) + '.')
        if len(items) > 2:
            if oxford:
                print('You are bringing ' + ', '.join(items[:-1]) + ' and ' + items[-1] + '.')
            else:
                print('You are bringing ' + ', '.join(items[:-1]) + ', and ' + items[-1] + '.')
    if sortbool:
        sorteditems = sorted(items)
        if len(items) == 2:
            print('You are bringing ' + ' and '.join(sorteditems) + '.')
        if len(items) > 2:
            if oxford:
                print('You are bringing ' + ', '.join(sorteditems[:-1]) + ' and ' + sorteditems[-1] + '.')
            else:
                print('You are bringing ' + ', '.join(sorteditems[:-1]) + ', and ' + sorteditems[-1] + '.')
# --------------------------------------------------
if __name__ == '__main__':
    main()
