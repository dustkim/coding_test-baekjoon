# baekjoon no.10871

import sys
n, x = map(int, input().split())

y = sys.stdin.readline().strip()
listNumber = list(map(int, y.split()))

for i in range(n):
    if(listNumber[i] < x):
        print(listNumber[i], end=" ")