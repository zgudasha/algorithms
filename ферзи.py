from itertools import permutations

n = int(input())
col = range(n)
answer = 0
answers = []
# перестановка не дает ходить ферзю по гор. и верт.
for perm in permutations(col): 
    # если перевернутая перестановка была ответом   
    if perm[::-1] in answers:
        answer += 1
        continue
    # множество отсекает повторяющиеся диагонали
    # если кол-во диагоналей равно размерности
    # то перестановка подходит
    if (n == len(set(perm[i] + i for i in col)) and n == len(set(perm[i] - i for i in col))):
        answers.append(perm)
        answer += 1

print(answer)