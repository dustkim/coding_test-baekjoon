T = int(input())

find = T // 5

if find == 0:
    print("1")
elif T % 5 == 0:
    print(find)
else:
    print(find + 1)