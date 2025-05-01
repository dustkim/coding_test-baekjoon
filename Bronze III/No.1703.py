while True:
    N = list(map(int, input().split()))

    if N[0] == 0:
        break

    sum = 1
    for i in range(1, (N[0]*2+1)):
        if i%2 != 0:
            sum *= N[i]
        else:
            sum -=N[i]
    
    print(sum)