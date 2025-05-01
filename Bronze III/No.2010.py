import sys
N = int(input())

sum = 1
for _ in range(N):
    number = int(sys.stdin.readline())      # 시간초과 나와서 사용
    sum += (number - 1)

print(sum)