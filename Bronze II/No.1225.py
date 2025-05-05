# 시간초과
# A, B = map(int, input().split())

# sum = 0
# price_A = +A
# price_B = +B

# while A > 0:
#     n = A%10
#     while price_B > 0:
#         sum += n * (price_B%10)
#         price_B //= 10
#     A //= 10
#     price_B = +B

# print(sum)


# python3는 시간초과, pypy3는 정답
A, B = input().split()

sum = 0
for i in A:
    for j in B:
        sum += int(i) * int(j)

print(sum)