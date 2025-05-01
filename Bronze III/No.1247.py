for i in range(3):
    N = int(input())
    sum = 0
    for i in range(N):
        number = int(input())
        sum += number
    if sum > 0:
        print("+")
    elif sum == 0:
        print("0")
    else:
        print("-")