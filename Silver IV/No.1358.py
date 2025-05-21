W, H, X, Y, P = map(int, input().split())

count = 0
radi = H//2
for _ in range(P):
    x, y = map(int, input().split())

    if X <= x <= X+W and Y <= y <= Y+H:
        count += 1
    elif ((x-X)**2 + (y-(Y+radi))**2) <= (radi)**2:
        count += 1
    elif ((x-(X+W))**2 + (y-(Y+radi))**2) <= (radi)**2:
        count += 1

print(count)