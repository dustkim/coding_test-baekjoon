n, m = map(int, input().split())

row1, col1 = (n-1)//4, (n-1)%4
row2, col2 = (m-1)//4, (m-1)%4

distance = abs(row1 - row2) + abs(col1 - col2)
print(distance)