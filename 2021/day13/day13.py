import numpy as np
from parse import findall

with open("day13-example.txt") as f:
    input = f.read().strip()

coords = findall("{:d},{:d}", input)
folds = findall("{:l}={:d}", input)

P = np.zeros((9999, 9999), bool)

for x, y in coords:
    P[y, x] = True

for axis, a in folds:
    if axis == "x":
        P = P[:,:a] | P[:,2*a:a:-1]
    if axis == "y":
        P = P[:a,:] | P[2*a:a:-1,:]
    print(P.sum())

print(np.array2string(P, separator="",
    formatter = {"bool":{0:" ",1:"█"}.get}))