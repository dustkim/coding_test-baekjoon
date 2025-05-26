from collections import defaultdict
N = int(input())

product = []
finddic = defaultdict(int)

for _ in range(N):
    price, drive = map(int, input().split())
    product.append((price, drive))

for i in product:
    sum = 0
    for j in product:
        if i[0] <= j[0] and (i[0]-j[1]) > 0:
            sum += i[0]-j[1]
    finddic[i[0]] = sum

max_value = max(finddic.values())
result = [k for k, v in finddic.items() if v == max_value]
result.sort()

if max_value <= 0:
    print(0)
else:
    print(result[0])