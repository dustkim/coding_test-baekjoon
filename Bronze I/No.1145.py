number = list(map(int, input().split()))

price = 1

while True:
    sum = 0
    for i in range(5):
        if price%number[i] == 0:
            sum += 1
    if sum >= 3:
        print(price)
        break
    else:
        price += 1