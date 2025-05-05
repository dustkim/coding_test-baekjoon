from collections import defaultdict

N = int(input())

dic = defaultdict(int)
for _ in range(N):
    name = input().strip()
    first = name[0]
    dic[first] += 1

result = [i for i in sorted(dic) if dic[i] >= 5]

if result:
    print("".join(result))
else:
    print("PREDAJA")