N = int(input())

Student_N = []
for _ in range(N):
    Student_N.append(input())

length = len(Student_N[0])
count = 0
flag = True
for i in range(1, length+1):
    check = set()
    for num in Student_N:
        check.add(num[-i:])
    if len(check) == N:
        print(i)
        break