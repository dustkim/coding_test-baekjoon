while True:
    try:
        a = list(input().strip())
        b = list(input().strip())

        li = []

        for i in a:
            if i in b:
                b.remove(i)
                li.append(i)
        li.sort()
        print("".join(li))
        
    except EOFError:
        break