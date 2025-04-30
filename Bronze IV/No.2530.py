A = list(map(int, input().split()))
D = int(input())

Answer = (A[0] * 3600) + (A[1] * 60) + A[2] + D

S = Answer%60
M = (Answer//60)%60
H = ((Answer//60)//60)%24

print(f"{H} {M} {S}")