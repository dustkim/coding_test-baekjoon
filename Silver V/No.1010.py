T = int(input())

def Fatorial(number):
    if number <= 1:
        return 1
    else:
        return number * Fatorial(number - 1)

for i in range(T):
    N, M = map(int, input().split())
    
    result = Fatorial(M)//((Fatorial(N) * Fatorial(M-N)))
    print(result)