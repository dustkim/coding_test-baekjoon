N, K, I = map(int, input().split())

round = 0
while K != I:
    if K%2 != 0 and I%2 != 0:
        K = (K+1)//2
        I = (I+1)//2
    elif K%2 != 0 and I%2 == 0:
        K = (K+1)//2
        I = I//2
    elif I%2 != 0 and K%2 == 0:
        K = K//2
        I = (I+1)//2
    else:
        K = K//2
        I = I//2
    round += 1

print(round)


# round = 0
# while K != I:
#     K = (K+1)//2
#     I = (I+1)//2
#     round += 1
# print(round)