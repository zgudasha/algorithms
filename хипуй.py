# LEFT    = lambda i: 2 * i + 1
# RIGHT   = lambda i: 2 * i + 2
# PARRENT = lambda i: (i - 1) // 2

# def siftUp(array, i):
#     if i: # 0 - корень
#         while array[i] > array[PARRENT(i)]:
#             array[i], array[PARRENT(i)] = array[PARRENT(i)], array[i]
#             i = PARRENT(i)

# def siftDown(array, i):
#     while LEFT(i) < len(array):
#         l = LEFT(i)
#         r = RIGHT(i)
#         m = l
#         if r < len(array) and array[r] > array[l]:
#             m = r
#         if array[i] >= array[m]:
#             break
#         array[i], array[m] = array[m], array[i]

# def pop(array):
#     m = array[0]  # берем корень
#     array[0] = array[-1] # меняем с последним элементом
#     array = array[0:len(array) - 1] # убираем бывший корень из кучи
#     siftDown(array, 0) # просеиваем вниз 
#     return m

# def insert(array, value):
#     array.append(value)
#     siftUp(array, len(array) - 1) # просеиваем вверх
import heapq

n = int(input())

heap = []

for i in range(n):
    command = [int(j) for j in input().split()]
    if len(command) == 2:
        command, value = command
        heap.append(value)
        heapq._heapify_max(heap)
    else:
        print(heapq._heappop_max(heap))
