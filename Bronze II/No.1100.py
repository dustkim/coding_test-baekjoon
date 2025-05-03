import sys

sum = 0
for i in range(8):
    chess = list(map(str, sys.stdin.readline().strip()))
    for j in range(8):
        if i%2 == 0 and j%2 == 0:
            if chess[j] == 'F':
                sum += 1
        elif i%2 != 0 and j%2 != 0:
            if chess[j] == 'F':
                sum += 1
print(sum)