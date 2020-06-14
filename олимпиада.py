number = 0 #порядковый номер
cost = 1 #баллы

def bubbleSort(array, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if array[j][cost] < array[j + 1][cost]:
                array[j], array[j + 1] = array[j + 1], array[j]
            elif array[j][cost] == array[j + 1][cost]:
                if array[j][number] > array[j + 1][number]:
                    array[j], array[j + 1] = array[j + 1], array[j]

    return array

n = int(input())
array = []
for i in range(n):
    num, c = [int(i) for i in input().split()]
    array.append((num, c))

array = bubbleSort(array, n)
for i in array:
    print(*i)
