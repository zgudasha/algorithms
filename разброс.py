def quick_sort(array):
    if array:
        left = quick_sort([x for x in array if x < array[0]]) 
        mid = [x for x in array if x == array[0]]
        right   = quick_sort([x for x in array if x > array[0]])
        return left + mid + right
    return []

n = int(input())
array = [int(i) for i in input().split()][:n]
print(*quick_sort(array))
