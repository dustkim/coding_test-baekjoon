N = int(input())

for i in range(N):
    star = "*" * (i*2+1)
    spacebar = " " * (N-(i+1))
    print(spacebar + star)