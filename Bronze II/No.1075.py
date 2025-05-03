N = int(input())
F= int(input())

NN = (N//100) * 100

for i in range(100):
    if (NN+i)%F == 0:
        print(f"{i:02d}")
        break

# 문제의 핵심은 마지막 두 자리 중 나누어지는 가장 작은 수
# 따라서 1~99까지 더해서 가장 먼저 나누어지는 값이 가장 작은 수가 됨됨