# baekjoon no.3003

n = list(map(int, input().split()))

x = [1, 1, 2, 2, 2, 8]
for i in range(len(n)):
    if x[i] != n[i]:
        print(x[i] - n[i], end=" ")
    else:
        print(0, end=" ")