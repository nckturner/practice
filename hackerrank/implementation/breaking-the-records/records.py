#!/usr/bin/env python3

if __name__ == "__main__": 
    with open("input.txt") as f:
        num_games = f.readline()
        scores = [int(x) for x in f.readline().strip().split(' ')]

        print("Num games: {0}".format(num_games))
        print("Scores: {0}".format(scores))

        min_dec = 0
        max_inc = 0

        maxs = scores[0]
        mins = scores[0]

        for s in scores:
            if s > maxs:
                maxs = s
                max_inc += 1
            if s < mins:
                mins = s
                min_dec += 1

        print("max {0}".format(max_inc))
        print("min {0}".format(min_dec))


