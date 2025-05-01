N = int(input())

for i in range(N):
    star = "*" * ((N*2-1) - (i*2))
    spacebar = " " * i
    print(spacebar + star)