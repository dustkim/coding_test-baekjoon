# baekjoon no.10807

import sys
n = int(input())
x = sys.stdin.readline().strip()
v = int(input())

number = list(map(int, x.split()))

total = 0
for i in range(n):
    if (number[i] == v):
        total += 1
    i += 1
    
print(total)