# baekjoon no.2444

n = int(input())

for i in range(n):
    print(" "*(n-i-1)+"*"*(i*2+1))

for i in range(n-1):
    print(" "*(i+1)+"*"*(2*(n-i-1)-1))