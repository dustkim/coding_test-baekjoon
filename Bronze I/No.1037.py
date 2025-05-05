N = int(input())

divisor = list(map(int, input().split()))

divisor.sort(reverse=True)

number = divisor[0] * divisor[-1]

print(number)