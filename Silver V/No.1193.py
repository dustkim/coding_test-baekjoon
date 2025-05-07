X = int(input())

count = 0
sum = 0
i = 1

while True:
    if sum >= X:
        break
    else:
        sum += i
        count += 1
        i += 1

if count%2 == 0:
    N = X - (sum-count)
    numerator = 0
    denominator = count + 1
    for _ in range(N):
        numerator += 1
        denominator -= 1
    print(f"{numerator}/{denominator}")
else:
    N = X - (sum-count)
    numerator = count+1
    denominator = 0
    for _ in range(N):
        numerator -= 1
        denominator += 1
    print(f"{numerator}/{denominator}")