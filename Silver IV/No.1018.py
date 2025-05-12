N, M = map(int, input().split())
chess = [input() for _ in range(N)]

count = 64
for i in range(N-7):
    for j in range(M-7):
        countB = 0
        countW = 0
        for x in range(8):
            for y in range(8):
                location = chess[i+x][j+y]
                if (x+y)%2 == 0:
                    if location != 'B':
                        countB += 1
                    if location != 'W':
                        countW += 1
                else:
                    if location !='B':
                        countW += 1
                    if location != 'W':
                        countB += 1
        count = min(count, countB, countW)

print(count)