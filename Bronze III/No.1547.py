N = int(input())

flag = 1
for i in range(N):
    n, m = map(int, input().split())
    if n == flag:
        flag = m
    elif m == flag:
        flag = n

print(flag)