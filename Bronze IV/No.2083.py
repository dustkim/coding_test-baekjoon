while True:
    member = input().split()
    if member[0] == '#':
        break
    else:
        if int(member[1]) > 17 or int(member[2]) >= 80:
            print(f"{member[0]} Senior")
        else:
            print(f"{member[0]} Junior")