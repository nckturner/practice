#!/usr/bin/env python3

import argparse
import random
import time
from datetime import datetime

def filename():
    date = time.strftime("%Y%m%d%H%M")
    milli = int(datetime.now().microsecond/1000)
    return "input-{0}.{1}.txt".format(date,milli)

def generate(n, total_digits):

    if n == -1:
        n = random.randrange(1, 200000)
    
    if total_digits == -1:
        total_digits = random.randrange(200000, 1000000)

    unsorted = ['' for x in range(n)]
    
    # one digit for each entry in unsorted to start
    for x in range(n):
        unsorted[x] += str(random.randrange(1,10))

    # spread the rest of the digits out randomly
    for x in range(total_digits - n):
        i = random.randrange(n)
        unsorted[i] += str(random.randrange(0,10))

    fn = filename()
    with open(fn, 'w') as f:
        f.write(str(n)+'\n')
        for line in unsorted:
            f.write(line+'\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate an input file for "big-sorting" (https://www.hackerrank.com/challenges/big-sorting).  '
            +'The input file will be used to generate an array of numeric strings, "unsorted", where each string is a positive number with '
            +'anywhere from 1 to 10^6 digits.  The first line of the input file will contain N, which represents '
            +'the number of strings in "unsorted".  Each of the subsequent lines represents an integer contained in "unsorted".')
    parser.add_argument('-n', type=int, default=-1, help='The number of integers to generate.  Each will be written to a separate line, and N will '
            +'be written to the first line (resulting in N+1 lines). A value of -1 (the default) will result in a randomly generated N between MIN_N '
            +'and MAX_N.')
    parser.add_argument('--total_digits', type=int, default=-1, help='The total number of digits used in "unsorted"')
    args = parser.parse_args()
    
    generate(args.n, args.total_digits)


