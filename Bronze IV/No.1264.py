while True:
    S = input()
    count = 0
    if S == '#':
        break
    else:
        for i in range(len(S)):
            if S[i].lower() in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        print(count)
