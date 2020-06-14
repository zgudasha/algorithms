def insertion_sort(array):  
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i - 1
        while j >= 0 and array[j] > item_to_insert:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = item_to_insert

n = int(input())
array = [int(i) for i in input().split()]
insertion_sort(array)
print(*array)
