A, B = map(str, input().split())

count = 0
if len(A) < len(B):
    find = [0]*len(B)
    for i in range((len(B)-len(A))+1):
            for j in range(len(A)):
                if A[j] == B[i+j]:
                     find[i] += 1
    count = len(A) - max(find)
    print(count)
else:
    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1
    print(count)