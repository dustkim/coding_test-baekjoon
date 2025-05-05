N = input()

count = 1
N_copy = +int(N)

while True:
    new = 0
    div = N_copy//10 + N_copy%10
    new = (N_copy%10) * 10 + div%10
    if new == int(N):
        print(count)
        break
    N_copy = new   
    count += 1
