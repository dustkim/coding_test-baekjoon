from collections import defaultdict
N = int(input())

List = []
dic = defaultdict(int)

for i in range(N):
    List.append(input().split())

for i in range(N-1):
    for j in range(i+1, N):
        for k in range(5):
            if List[i][k] == List[j][k]:
                dic[i+1] += 1
                dic[j+1] += 1
                break

if dic:
    max_value = max(dic.values())

    result = [i for i, v in dic.items() if v == max_value]

    result.sort(key=lambda x:x)
    print(result[0])
else:
    print('1')