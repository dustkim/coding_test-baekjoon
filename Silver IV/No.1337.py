N = int(input())

number = [int(input()) for _ in range(N)]

number.sort()

checkList = []
for num in number:
    count = 0
    for i in range(1, 5):
        if (num+i) not in number:
            count += 1
    checkList.append(count)

checkList.sort()
print(checkList[0])