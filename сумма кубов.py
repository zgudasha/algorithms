CUBE = lambda x: x ** 3

n = int(input())

dp = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    dp[i] = dp[i - 1] + 1
    j = 2
    while CUBE(j) <= i:
        if dp[i - CUBE(j)] < dp[i]:
            dp[i] = dp[i - CUBE(j)] + 1
        j += 1

print(dp[n])
