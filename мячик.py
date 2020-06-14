n = int(input())
array = [0] * n

if n == 1:
    print(1)
elif n == 2:
    print(2)
elif n == 3:
    print(4)
else:
    array[0], array[1], array[2] = 1, 2, 4
    for i in range(3, n):
        array[i] = array[i - 3] + array[i - 2] + array[i - 1]
    print(array[n - 1])
