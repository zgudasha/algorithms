def bubbleSort(array, n):
    count = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                count += 1
                array[j], array[j + 1] = array[j + 1], array[j]

    return count

n = int(input())
array = [int(i) for i in input().split()][:n]

print(bubbleSort(array, n))