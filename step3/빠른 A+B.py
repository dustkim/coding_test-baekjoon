# baekjoon no.15552

import sys
T = int(input())

for i in range(T):
    x = sys.stdin.readline().strip()
    a, b = map(int, x.split())
    print("{}".format(a+b))
    i += 1