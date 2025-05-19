A, B = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

result = len(setA - setB) + len(setB - setA)

print(result)