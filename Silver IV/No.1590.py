N, T = map(int, input().split())

Bus = []

for _ in range(N):
    start, gap, count = map(int, input().split())
    for i in range(count):
        if start == T:
            Bus.append(0)
            break
        elif start < T:
            start += gap
        else:
            Bus.append(start - T)

if Bus:
    Bus.sort()
    print(Bus[0])
else:
    print(-1)