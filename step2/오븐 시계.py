# baekjoon no.2525

h, m = map(int, input().split())
nm = int(input())

c = m + nm
d = (m + nm) % 60
e = (m + nm) // 60
if(c < 60):
    print("%d %d" % (h, d))
else:
    if (h + e >= 24):
        print("{} {}".format(h+e-24, d))
    else:
        print("{} {}".format(h+e, d))