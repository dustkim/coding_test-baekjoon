from collections import defaultdict
N = int(input())

bookList = defaultdict(int)

for i in range(N):
    book = input()
    bookList[book] += 1

max_score = max(bookList.values())
result = [i for i, v in bookList.items() if v == max_score]
result.sort()

print(result[0])