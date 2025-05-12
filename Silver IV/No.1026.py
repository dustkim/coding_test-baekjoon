N = int(input())
arrayA = list(map(int, input().split()))
arrayB = list(map(int, input().split()))

sum = 0
for i in range(N):
    A = min(arrayA)
    indexA = arrayA.index(A)
    B = max(arrayB)
    indexB = arrayB.index(B)

    sum += A*B
    arrayA[indexA] = 101
    arrayB[indexB] = 0

print(sum)