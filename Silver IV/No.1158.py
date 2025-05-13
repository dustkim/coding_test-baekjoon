N, K = map(int, input().split())

Number = [i for i in range(1, N+1)]
Turn = []
index = 0

for i in range(1, N+1):
    index = (index + K - 1)%len(Number)
    Turn.append(Number[index])
    Number.remove(Number[index])

print('<' + ', '.join(map(str, Turn)) + '>')



# pop 사용하여 코드 줄임
# N, K = map(int, input().split())

# Number = [i for i in range(1, N+1)]
# Turn = []
# index = 0

# for i in range(1, N+1):
#     index = (index + K - 1)%len(Number)
#     Turn.append(Number.pop(index))

# print('<' + ', '.join(map(str, Turn)) + '>')