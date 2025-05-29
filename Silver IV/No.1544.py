N = int(input())

wordList = [input() for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        length = len(wordList[j])
        for k in range(length):
            if wordList[i] == wordList[j]:
                break
            else:
                rotate = wordList[j][length-1] + wordList[j][:length-1]
                wordList[j] = rotate

result = list(set(wordList))
print(len(result))