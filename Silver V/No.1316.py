N = int(input())

check = 0
for _ in range(N):
    word = input()
    count = 0
    for j in range(len(word)):
        for k in range(j+1, len(word)):
            if word[j] == word[k] and (k - j) > 1:
                count += 1
                break
            elif word[j] == word[k]:
                break
    if count == 0:
        check += 1

print(check)