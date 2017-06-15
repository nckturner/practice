#!/usr/bin/env python3

#https://www.hackerrank.com/challenges/big-sorting

import argparse
import sys
import line_profiler

def setup(filename):
    unsorted = []
    with open(filename, 'r') as f:
        
        n_str = f.readline()
        try:
            n = int(n_str)
        except ValueError as e:
            print('File not properly formatted')
            sys.exit(1)

        for line in f:
            unsorted.append(line.strip())

    return unsorted

@profile
def sort(a):
    a.sort(key=lambda x: int(x))
    return a

@profile
def write_out(sorted_list):
    with open('sorted.txt', 'w') as s:
        for line in sorted_list:
            s.write(line+'\n')

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Name of file used for input.  It will hold the unsorted array (see https://www.hackerrank.com/challenges/big-sorting)')
    args = parser.parse_args()

    unsorted = setup(args.filename)

    
    sorted_list = sort(unsorted)

    write_out(sorted_list)
    
    #import timeit
    #print(timeit.timeit("sort(unsorted)", setup='from __main__ import sort', globals={"unsorted": unsorted}))

    

