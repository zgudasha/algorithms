word = input()
pattern = input()

word_len = len(word)
pattern_len = len(pattern)

for i in range(0, word_len - pattern_len + 1):
    if word[i:i + pattern_len] == pattern:
        print(i, end=' ')
