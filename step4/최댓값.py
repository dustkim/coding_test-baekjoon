# baekjoon no.2562

x = []
for i in range(9):
    number = int(input())
    x.append(number)
        
maxValue = max(x)
findIndex = x.index(maxValue)
print(maxValue)
print(findIndex+1)