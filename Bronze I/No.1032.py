N = int(input())

List = []
for i in range(N):
    text = list(map(str, input()))
    List.append(text)
if N == 1:
    print("".join(List[0]))
else:
    for i in range(N-1):
        for j in range(len(List[0])):
            if List[0][j] != List[i+1][j]:
                List[0][j] = '?'

    print("".join(List[0]))
        