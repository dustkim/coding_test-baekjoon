N = int(input())

word_list = [input() for i in range(N)]

result = list(set(word_list))

result.sort(key=lambda x:(len(x), x))

for i in result:
    print(i)