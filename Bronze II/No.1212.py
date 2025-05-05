# 시간초과
# N = int(input())

# length = 0
# price_e = +N
# price_t = 0
# List = []

# if N == 0:
#     print(0)
# else:
#     while N > 0:
#         N = N//10
#         length += 1
#     for i in range(length):
#         price_t += price_e%10 *(8**i)
#         price_e //= 10
#     while price_t > 0:
#         List.append(str(price_t%2))
#         price_t = price_t//2
#     print(''.join(reversed(List)))


# 시간초과
# N = int(input())

# length = 0
# price_e = N
# price_t = 0

# while price_e > 0:
#     div = price_e%10
#     price_t += div * (8**length)
#     length += 1
#     price_e = price_e//10

# if price_t == 0:
#     print(0)
# else:
#     List = []
#     while price_t > 0:
#         List.append(str(price_t%2))
#         price_t //=2
#     print("".join(reversed(List)))


# 시간초과
# N = input().strip()

# price = bin(int(N[0]))[2:]

# for i in N[1:]:
#     price += format(int(i), "03b")

# print(price)



N = input().strip()
price_t = int(N, 8)
price = bin(price_t)[2:]
print(price)