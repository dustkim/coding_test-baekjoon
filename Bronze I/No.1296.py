from collections import defaultdict
name_y = input()
N = int(input())

dic_t = defaultdict(int)

def find(name, dic):
    for i in name:
        if i in 'LOVE':
            dic[i] += 1

for _ in range(N):
    dic = defaultdict(int)
    name_t = input()
    full_name = name_y + name_t
    find(full_name, dic)
    score = ((dic['L'] + dic['O']) * (dic['L'] + dic['V']) * (dic['L'] + dic['E']) * (dic['O'] + dic['V']) * (dic['O'] + dic['E']) * (dic['V'] + dic['E']))%100

    dic_t[name_t] = score

max_value = max(dic_t.values())

result = [i for i, v in dic_t.items() if v == max_value]

print(sorted(result)[0])