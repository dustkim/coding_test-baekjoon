# baekjoon no.25304

x = int(input())
n = int(input())

total = 0
for i in range(n):
    product, number = map(int, input().split())
    total += product * number
    i += 1
if (total == x):
    print("Yes")
else:
    print("No")