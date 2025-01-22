# baekjoon no.1546

import sys
n = int(input())
m = sys.stdin.readline()
x = list(map(int, m.split()))

y = max(x)
avg = 0
for val in x:
    avg += (val/y)*100

print("{}".format(avg/n))