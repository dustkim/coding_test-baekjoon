N = int(input())
times = list(map(int, input().split()))

Y = 0
M = 0

for i in range(len(times)):
    Y += 10 * (times[i]//30) + 10
    M += 15 * (times[i]//60) + 15

if Y > M:
    print(f"M {M}")
elif Y < M:
    print(f"Y {Y}")
else:
    print(f"Y M {M}")