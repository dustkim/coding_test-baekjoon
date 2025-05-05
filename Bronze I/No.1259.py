while True:
    number = input()
    flag = True

    if number[0] == '0':
        break

    for i in range(len(number)//2):
        if int(number[i]) != int(number[-(1+i)]):
            flag = False
    
    if flag:
        print('yes')
    else:
        print('no')