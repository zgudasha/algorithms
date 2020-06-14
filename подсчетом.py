RANGE = 10001

n = int(input())
array = [int(i) for i in input().split()]
counters = [0 for i in range(2 * RANGE)]

for element in array:
    counters[element + RANGE] += 1

for i in range(2 * RANGE):
    while counters[i]:
        print(i - RANGE, end=' ')
        counters[i] -= 1
       