def find(element, array, start, end):
    if start <= end:
        mid = (start + end) // 2
        if element > array[mid]:
            return find(element, array, start=mid + 1, end=end)
        elif element < array[mid]:
            return find(element, array, start=start, end=mid - 1)
        else:
            return True
    return False


n, k = [int(i) for i in input().split()]
array1 = [int(i) for i in input().split()][:n]
array2 = [int(i) for i in input().split()][:k]


for i in range(k):
    if find(array2[i], array1, 0, n - 1):
        print('YES')
    else:
        print('NO')