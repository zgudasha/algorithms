n, m = [int(i) for i in input().split()]
a = [[0 for i in range(m + 1)] for i in range(n + 1)]
a[1][1] = 1
for i in range(2, n + 1):
    for j in range(2, m + 1):
        a[i][j] = a[i - 1][j - 2] + a[i - 2][j - 1]

print(a[n][m])
