# baekjoon no.9086

t = int(input())

for idx in range(t):
    s = str(input())
    if len(s) == 1:
        print("{}{}".format(s[0], s[0]))
    else:
        print("{}{}".format(s[0], s[len(s)-1]))