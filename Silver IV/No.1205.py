N, Score, P = map(int, input().split())
if N > 0:
    Lank = list(map(int, input().split()))
else:
    Lank = []

Lank.append(Score)
Lank.sort(reverse=True)

index = Lank.index(Score)
count = 0
for i in Lank:
    if i == Score:
        count += 1
if (index + count - 1) > (P - 1):
    print(-1)
else:
    print(index+1)