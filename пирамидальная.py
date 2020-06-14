import heapq

n = int(input())
array = [int(i) for i in input().split()]
heapq.heapify(array) # делаем кучу на минимум

while n:
    # берем минимум и просеиваем вверх
    # сохраняя свойство кучи
    print(heapq.heappop(array), end=' ')
    n -= 1
