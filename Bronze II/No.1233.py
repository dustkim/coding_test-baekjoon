from collections import defaultdict
S1, S2, S3 = input().split()

S1 = [i for i in range(1, int(S1)+1)]
S2 = [i for i in range(1, int(S2)+1)]
S3 = [i for i in range(1, int(S3)+1)]

dic = defaultdict(int)

for i in S1:
    for j in S2:
        for k in S3:
            n = str(int(i) + int(j) + int(k))
            dic[n] += 1

max_value = max(dic.values())

result = [k for k, v in dic.items() if v == max_value]

print(min(result, key=int))
