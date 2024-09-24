from itertools import permutations
def func(st):
    a = list(permutations(st))
    for i in a:
        print(i)
func(input())