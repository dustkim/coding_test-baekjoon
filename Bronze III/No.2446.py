N = int(input())

for i in range(N):
    star = "*" * ((2*N-1) - (i*2))
    spacebar = " " * i
    print(spacebar + star)

for i in range(N-2, -1, -1):
    star = "*" * ((2*N-1) - (i*2))
    spacebar = " " * i
    print(spacebar + star)