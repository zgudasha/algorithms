n = int(input())
array = [int(i) for i in input().split()]

while n > 0:
    m = 0
    for j in range(n):
        if array[j] > array[m]:
            m = j
    array[n - 1], array[m] = array[m], array[n - 1]
    n -= 1


print(*array)