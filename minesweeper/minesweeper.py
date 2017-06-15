import random

def randomCoord(a,b):
    return random.randrange(0,a), random.randrange(0,b)

def genField(width, height, nmines):
    f = []
    for i in range(width): 
        f.append([0 for x in range(height)])

    for m in range(nmines):
        x,y = randomCoord(width, height)
        while f[x][y] == 1:
            x,y = randomCoord(width, height)
        f[x][y] = 1
    return f

""" The coordinate plane increases downward (y) and to the right (x)
"""

def neighbors(x,y,width,height,f):
    n = []
    # Top Left
    if y > 0 and x > 0:
        n.append(f[x-1][y-1])
    else:
        n.append(None)
    # Top 
    if y > 0:
        n.append(f[x][y-1])
    else:
        n.append(None)
    # Top Right 
    if y > 0 and x < width-1:
        n.append(f[x+1][y-1])
    else:
        n.append(None)
    # Left 
    if x > 0:
        n.append(f[x-1][y])
    else:
        n.append(None)
    # Right
    if x < width-1:
        n.append(f[x+1][y])
    else:
        n.append(None)
    # Bottom Left
    if x > 0 and y < height-1:
        n.append(f[x-1][y+1])
    else:
        n.append(None)
    # Bottom
    if y < height-1:
        n.append(f[x][y+1])
    else:
        n.append(None)
    # Bottom Right
    if x < width-1 and y < height-1:
        n.append(f[x+1][y+1])
    else:
        n.append(None)
    return n


w = 8
h = 10

f = genField(w,h,20)

print()

f[0][0] = 4

print(neighbors(0,0,w,h,f))

for l in f:
    print(l)

