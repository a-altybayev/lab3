numheads=int(input())
numlegs=int(input())
def solve(numheads, numlegs):
    x = (numlegs - 2 * numheads) // 2
    y = numheads - x
    print(x,y)

solve(numheads,numlegs)