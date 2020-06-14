from itertools import permutations

n = int(input())

for perm in permutations(range(1, n + 1), n):
    print(*perm, sep='')
