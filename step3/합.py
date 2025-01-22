# baekjoon no.8393

n = int(input())

total = 0
for i in range(n+1):
    total += i
    i += 1
    
print(total)