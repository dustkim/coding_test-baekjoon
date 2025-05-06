A, B = map(int, input().split())

sum = 0
count = 0
number = 1

while True:
    for i in range(number):
        count += 1
        if count >= A and count <= B:
            sum += number
    
    if count >= B:
        print(sum)
        break

    number += 1