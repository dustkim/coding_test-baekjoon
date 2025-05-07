from collections import defaultdict
N = int(input())

List = []
dic = defaultdict(int)

for i in range(N):
    List.append(input().split())

for i in range(N-1):
    for j in List[i]:
        for k in range(i, N):
            if j in List[k]:
                dic[i+1] += 1
                dic[k+1] += 1

max_value = max(dic.values())

result = [i for i, v in dic.items() if v == max_value]

result.sort(key=lambda x:x)

print(result[0])