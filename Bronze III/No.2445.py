N = int(input())

for i in range(N):
    star = "*" * (i+1)
    spacebar = " " * (2*(N-i-1))
    print(star + spacebar + star)

for i in range(N-2, -1, -1):
    star = "*" * (i+1)
    spacebar = " " * (2*(N-i-1))
    print(star + spacebar + star)