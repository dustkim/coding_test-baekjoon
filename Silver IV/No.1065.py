N = int(input())

count = 99
if N <= 99:
    count = N
    print(N)
else:
    for i in range(100, N+1):
        if 100 <= i <= 999:
            array = list(str(i))
            if (int(array[0]) - int(array[1])) == (int(array[1]) - int(array[2])):
                count += 1
        elif i >= 1000:
            array = list(str(i))
            if (int(array[0]) - int(array[1])) == (int(array[1]) - int(array[2])) == (int(array[2]) - int(array[3])):
                count += 1
    print(count)


# 코드를 더 단순하게 바꾸면..
# count = 0
# for i in range(1, N+1):
#     array = list(map(int, str(i)))
#     if len(array) < 2:
#         count += 1
#     else:
#         difference = array[0] - array[1]
#         if all(array[k] - array[k+1] == difference for k in range(len(array)-1)):
#             count += 1

# print(count)