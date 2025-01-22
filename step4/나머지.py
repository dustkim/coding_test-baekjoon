# baekjoon no.3052

x = []
B = 42
for i in range(10):
    A = int(input())
    C = A % B
    if C not in x:
        x.append(C)

print(len(x))