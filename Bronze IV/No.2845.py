import sys

L, P = map(int, input().split())
Number = list(map(int, input().split()))

flag = L * P

for i in range(len(Number)):
    Number[i] = Number[i] - flag

print(*Number)