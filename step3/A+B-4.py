# baekjoon no.10951

import sys

while True:
    try:
        x = sys.stdin.readline().strip()
        a, b = map(int, x.split())
        print("{}".format(a+b))
    except:
        break