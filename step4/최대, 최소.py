# baekjoon no.10818

import sys
n = int(input())
x = sys.stdin.readline().strip()

listNumber = list(map(int, x.split()))

listNumber.sort()

print("{} {}".format(listNumber[0], listNumber[n-1]))