# baekjoon no.2675

t = int(input())

for idx in range(t):
    result = ""
    r, s = map(str, input().split())
    for idxx in range(len(s)):
        result += s[idxx] * int(r)
        
    print(result)