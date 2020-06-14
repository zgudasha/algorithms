n, m = (int(i) for i in input().split())
array1 = [int(i) for i in input().split()]
array2 = [int(i) for i in input().split()]

for x in array2:
    left = -1
    right = len(array1)
    while right - left > 1:
        middle = (right + left) // 2
        if array1[middle] < x:
            left = middle
        else:
            right = middle

    left_1 = -1
    right_1 = len(array1)
    while right_1 - left_1 > 1:
        middle = (right_1 + left_1) // 2
        if array1[middle] <= x:
            left_1 = middle
        else:
            right_1 = middle

    if left == left_1 and right == right_1:
        print(0)
        continue
    if right == left_1:
        print(right + 1, right + 1)
    else:
        print(right + 1, left_1 + 1)