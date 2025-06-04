S = list(map(int, input().strip()))

def check(number):
    length = len(number)//2
    sum1 = sum(number[:length])
    sum2 = sum(number[length:])

    if sum1 == sum2:
        return True
    else:
        return False
        
final = [0]
for i in range(len(S)):
    for j in range(i+2, len(S)+1, 2):
        num = S[i:j]
        result = check(num)
        if result:
            final.append(j-i)

final.sort(reverse=True)
print(final[0])