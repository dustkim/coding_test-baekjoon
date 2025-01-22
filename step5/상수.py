# baekjoon no.2908

a, b = list(map(int, input().split()))

x = int(str(a)[::-1])
y = int(str(b)[::-1])

if x > y:
    print(x)
else:
    print(y)