S, I = map(int, input().split())
list1 = []

team1 = (S+I)//2
team2 = S - team1

if (S+I)%2 == 0 and team2 >= 0:
    list1.append(team1)
    list1.append(team2)
else:
    list1.append(-1)

list1.sort(reverse=True)
print(*list1)