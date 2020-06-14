from itertools import combinations

n, k = (int(i) for i in input().split())

for comb in combinations(range(1, n + 1), k):
    print(*comb)
