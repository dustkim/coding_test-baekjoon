N, M = map(int, input().split())

List = [input() for _ in range(N)]
row_empty = 0
col_empty = 0

for row in List:
    if 'X' not in row:
        row_empty += 1

for j in range(M):
    flag = False
    for i in range(N):
        if List[i][j] == 'X':
            flag = True
            break
    if not flag:
        col_empty += 1

print(max(row_empty, col_empty))