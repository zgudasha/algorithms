n = int(input())
summ = [0] * n
price = [int(i) for i in input().split()][:n]

summ[0] = price[0]
if n > 1:
    summ[1] = price[1]
    for i in range(3, n + 1): 
        summ[i-1] = price[i-1] + min(summ[i-2], summ[i-3])
print(summ[n-1])
