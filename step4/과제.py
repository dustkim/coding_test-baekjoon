# baekjoon no.5597

x = [i for i in range(1, 31)]
y = []
for i in range(28):
    n = int(input())
    y.append(n)

for val in x:
    if val not in y:
        print(val)