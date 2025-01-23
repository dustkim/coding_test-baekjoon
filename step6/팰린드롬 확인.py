# baekjoon no.10988

n = str(input().strip())

x = len(n)-1
y = len(n)//2
judge = True
for i in range(y):
    if n[i] != n[x-i]:
        judge = False
        break
if judge == True:
    print(1)
else:
    print(0)