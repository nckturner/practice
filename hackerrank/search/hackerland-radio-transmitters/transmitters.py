#!/usr/bin/env python3

def in_range(house1, house2, t_range):
    print("{0} {1} {2}".format(house1, house2, t_range))
    return abs(house1 - house2) <= t_range


if __name__ == '__main__':

    transmitters = []
    
    with open('input.txt', 'r') as f:
        n, k = tuple([int(x) for x in f.readline().strip().split(' ')])
        h = [int(x) for x in f.readline().strip().split()]

        # last represents last covered house
        # current is house we are checking
        h.sort()
        print(h)

        last = h[0]
    
        for house in h[1:]:
            if in_range(house, last, k):
                continue
            else:
                transmitters.append(last)
                print("t {0}".format(transmitters))
                last = house


        print(transmitters) 
                

