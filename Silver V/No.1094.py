X = int(input())

List = [64, 32, 16, 8, 4, 2, 1]

sum = X
count = 0
while True:
    if X in List:
        print('1')
        break
    elif sum == 0:
        print(count)
        break
    else:
        for i in range(len(List)):
            if sum >= List[i]:
                sum -= List[i]
                count += 1
        print(count)
        break