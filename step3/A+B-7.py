# baekjoon no.11021

import sys
T = int(input())

for i in range(T):
    x = sys.stdin.readline().strip()
    a, b = map(int, x.split())
    print("Case #{}: {}".format(i+1, a+b))