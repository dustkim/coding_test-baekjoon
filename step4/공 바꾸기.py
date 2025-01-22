# baekjoon no.10813

n, m = map(int, input().split())

x = [c for c in range(1, n+1)]
y = 0
for _ in range(m):
    i, j = map(int, input().split())
    y = x[j-1]
    x[j-1] = x[i-1]
    x[i-1] = y

for val in x:
    print(val, end=" ")