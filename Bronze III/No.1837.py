P, K = map(int, input().split())

def eratosthenes(K):        # 에라토스테네스의 체 -> 자연수 1을 제거하고, 각 수의 배수들을 제거하는 방법
    number = [True] * K
    number[0:2] = [False, False]

    for i in range(2, int(K ** 0.5) + 1):       # 어떤 수 K의 배수를 제거할 때 소수는 루트K까지 확인하면 됨
        if number[i]:
            for j in range(i*i, K, i):
                number[j] = False
    
    return [i for i, val in enumerate(number) if val]

arr = eratosthenes(K)

for i in arr:
    if P%i == 0:
        print(f"BAD {i}")
        break
else:
    print("GOOD")