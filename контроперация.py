temp = [int(i) for i in input().split()]
n, array = temp[0], temp[1:]
m = min(array)
ma = max(array)
for i in range(n):
    if array[i] == ma:
        array[i] = m

array = [m if i == ma else i for i in array]
print(*array)
