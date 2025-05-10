N =int(input())
Array = list(map(int, input().split()))
New_Array = [0 for _ in range(N)] # or [0]*N

for i in range(N):
    index = Array.index(min(Array))
    New_Array[index] = i
    Array[index] = 1001

print(' '.join(map(str, New_Array)))