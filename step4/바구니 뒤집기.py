# baekjoon no.10811

n, m = map(int, input().split())

x = [y for y in range(1, n+1)]

for idx in range(m):
    i, j = map(int, input().split())
    x[i-1:j] = x[i-1:j][::-1]
    
for val in x:
    print(val, end=" ")