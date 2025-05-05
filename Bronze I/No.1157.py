from collections import defaultdict
sentence = input()
dic = defaultdict(int)

for i in sentence:
    dic[i.upper()] += 1

max_value = max(dic.values())
result = [i for i, v in dic.items() if v == max_value]

if len(result) >= 2:
    print('?')
else:
    print(''.join(result))