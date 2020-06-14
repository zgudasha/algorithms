n = int(input())
count = 0
a = [[int(j) for j in input().split()][:n] for i in range(n)]

for i in a:
    for j in i:
        if j == 1:
            count += 1

count = int(count/2)
print(count)