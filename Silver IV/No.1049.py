N, M = map(int, input().split())

setlist = []
eachlist = []
resultlist = []
for i in range(M):
    set, each = map(int, input().split())
    setlist.append(set)
    eachlist.append(each)

if N <= 6:
    resultlist.append(min(setlist))
    resultlist.append(min(eachlist) * N)
else:
    resultlist.append((N//6+1)*min(setlist))
    resultlist.append((N//6)*min(setlist) + (N%6)*min(eachlist))
    resultlist.append(N*min(eachlist))

result = min(resultlist)

print(result)