n = int(input())
# a, b = 1, 1
# for i in range(2, n):
#     a = a + b
#     b = a - b
# print(a)
if n == 1:
    print(1)
else:
    f = [0] * n
    f[0] = f[1] = 1
    for i in range(2, n):
        f[i] = f[i-1] + f[i-2]
    print(f[n - 1])
