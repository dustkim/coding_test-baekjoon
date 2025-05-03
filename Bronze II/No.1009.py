import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    data = pow(a, b, 10)
    if data == 0:
        print(10)
    else:
        print(data)