N, m, M, T, R = map(int, input().split())

sum = 0
hb = +m

while True:
    if N > 0:
        if (m+T) > M:
            sum -= 1
            N = 0
        elif (hb+T) <= M:
            hb += T
            N -= 1
            sum += 1
        elif (hb-R) <= m:
            hb = m
            sum += 1
        else:
            hb -= R
            sum += 1
    else:
        break

print(sum)
