# baekjoon no.2884

h, m = map(int, input().split())

if (m >= 45):
    c = m - 45
    print("%d %d" % (h, c))
else:
    c = 45 - m
    d = 60 - c
    if (h != 0):
        print("{0} {1}".format(h-1, d))
    else:
        print("{0} {1}".format(23, d))