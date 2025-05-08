Today = list(map(int, input().split()))
Dday = list(map(int, input().split()))

count = 0
while True:
    if Today == Dday:
        break
    elif (Today[0]%4 == 0 and Today[0]%100 != 0) or Today[0]%400 == 0:
        if Today[1] in [1, 3, 5, 7, 8, 10, 12] and Today[2] > 31:
            if Today[1] == 12:
                Today[0] += 1
                Today[1] = 1
                Today[2] = 1
            else:
                Today[1] += 1
                Today[2] = 1
        elif Today[1] in [4, 6, 9, 11] and Today[2] > 30:
            Today[1] += 1
            Today[2] = 1
        elif Today[1] == 2 and Today[2] > 29:
            Today[1] += 1
            Today[2] = 1
        else:
            Today[2] += 1
            count += 1
    elif (Today[0]%4 !=0 and Today[0]%100 == 0) or Today[0]%400 != 0:
        if Today[1] in [1, 3, 5, 7, 8, 10, 12] and Today[2] > 31:
            if Today[1] == 12:
                Today[0] += 1
                Today[1] = 1
                Today[2] = 1
            else:
                Today[1] += 1
                Today[2] = 1
        elif Today[1] in [4, 6, 9, 11] and Today[2] > 30:
            Today[1] += 1
            Today[2] = 1
        elif Today[1] == 2 and Today[2] > 28:
            Today[1] += 1
            Today[2] = 1
        else:
            Today[2] += 1
            count += 1
    
if count > 365242:
    print("gg")
else:
    print(f"D-{count}")



# datetime 모듈을 사용한 방식
# from datetime import date

# y1, m1, d1 = map(int, input().split())
# y2, m2, d2 = map(int, input().split())

# start_day = date(y1, m1, d1)
# end_day = date(y2, m2, d2)

# term = (end_day - start_day).days

# if term > 365242:
#     print("gg")
# else:
#     print(f"D-{term}")