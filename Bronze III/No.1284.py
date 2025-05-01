while True:
    N = input()

    if N[0] == "0":
        break

    sum = len(N) + 1
    for i in range(len(N)):
        if N[i] == "1":
            sum += 2
        elif N[i] == "0":
            sum += 4
        else:
            sum += 3

    print(sum)