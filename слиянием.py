def merge(array):
    if len(array) < 2:
        return array
    else:
        middle = len(array) // 2
        left = merge(array[:middle])
        right = merge(array[middle:])
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        return result

n = int(input())
array = [int(i) for i in input().split()]

print(*merge(array))