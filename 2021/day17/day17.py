from re import findall
import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "day17-input.txt"

ll = open(filename).read().strip()

x1,x2,y1,y2 = map(int, findall(r'-?\d+', ll))

def sim(vx, vy, px=0, py=0):
    if px > x2 or py < y1: return 0
    if px >= x1 and py <= y2: return 1
    return sim(vx-(vx>0), vy-1 , px+vx, py+vy)

hits = [sim(x,y) for x in range(1, 1+x2)
                 for y in range(y1, -y1)]

print(y1*(y1+1)//2, sum(hits))