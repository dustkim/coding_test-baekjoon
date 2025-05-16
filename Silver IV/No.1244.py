N = int(input())
Switch = list(map(int, input().split()))
Students = int(input())

New_Switch = []

for _ in range(Students):
    sex, number = map(int, input().split())
    if sex == 1:
        for i in range(1, len(Switch)+1):
            if i%number == 0 and Switch[i-1] == 0:
                Switch[i-1] = 1
            elif i%number == 0 and Switch[i-1] == 1:
                Switch[i-1] = 0
    else:
        index = number-1
        for i in range(len(Switch)):
            if index-i < 0 or index+i >= len(Switch):
                break
            if Switch[index-i] == Switch[index+i] and Switch[index+i] == 0:
                Switch[index-i] = 1
                Switch[index+i] = 1
            elif Switch[index-i] == Switch[index+i] and Switch[index+i] == 1:
                Switch[index-i] = 0
                Switch[index+i] = 0
            else:
                break

for i in range(0, len(Switch), 20):
    print(*Switch[i:i+20])