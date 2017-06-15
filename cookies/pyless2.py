import sys
import mmap
from collections import deque

NEWLINE = 10

if len(sys.argv) != 3:
    print("Usage: \n\t{0} FILENAME LINES".format(sys.argv[0]))
    sys.exit(1)

filename, n = sys.argv[1], int(sys.argv[2])

print("Taking last {0} lines from {1}.".format(n, filename))

d = deque()
with open(filename, 'rb') as f:
    mm = mmap.mmap(f.fileno(), 0, mmap.MAP_SHARED, mmap.PROT_READ)
   
    i = j = len(mm)-1
    while i > 0 and n > 0: 
        if mm[i] == NEWLINE:
            d.append(mm[i+1:j])
            j=i
            n=n-1
        i=i-1
    
r = len(d)
for i in range(r):
    print(d.pop().decode('ascii'))


