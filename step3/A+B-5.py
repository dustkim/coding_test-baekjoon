# baekjoon no.10952

import sys

while True:
    x = sys.stdin.readline().strip()
    a, b = map(int, x.split())
    if (a == 0 and b == 0):
        break
    else:
        print("{}".format(a+b))