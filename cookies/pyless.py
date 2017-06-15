import sys
from collections import deque

if len(sys.argv) != 3:
    print("Usage: \n\t{0} FILENAME LINES".format(sys.argv[0]))
    sys.exit(1)

filename, n = sys.argv[1], int(sys.argv[2])

print("Taking last {0} lines from {1}.".format(n, filename))

f = open(filename, 'r')
d = deque(f, n)
for l in d:
    print(l, end="")
