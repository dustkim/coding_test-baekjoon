N = int(input())

for i in range(N):
    star = "*" * (N-i)
    spacebar = " " * i
    print(spacebar + star)