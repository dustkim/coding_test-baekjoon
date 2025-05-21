N, M, K = map(int, input().split())

def combination(num1, num2):
    if num2 > num1 or num2 < 0:
        return 0
    mul1 = 1
    mul2 = 1
    
    for i in range(num2):
        mul1 *= (num1-i)
        mul2 *= (num2-i)

    return mul1/mul2

deno = combination(N, M)
numer = 0
for i in range(K, M+1):
    set1 = combination(M, i)
    set2 = combination(N-M, M-i)

    numer += set1*set2

print(numer/deno)