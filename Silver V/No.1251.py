word = input().strip()

word_list = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first = word[:i][::-1]
        second = word[i:j][::-1]
        final = word[j:][::-1]
        word_list.append(first + second + final)

word_list.sort()

print(word_list[0])