# baekjoon no.5622

s = list(str(input()))
x = 0
for i in range(len(s)):
    if ord(s[i]) == 83:
        x += 8
    elif ord(s[i]) == 86:
        x += 9
    elif ord(s[i]) in [89, 90]:
        x += 10
    else:
        y = (ord(s[i]) - 65)//3
        x += (y+3)
    
print(x)