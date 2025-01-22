# baekjoon no.10810

n, m = map(int, input().split())

x = [0 for _ in range(n)]
for y in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        x[idx] = k

for val in x:
    print(val, end=" ")