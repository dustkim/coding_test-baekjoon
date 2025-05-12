L = int(input())
S = list(map(int, input().split()))
n = int(input())

if n not in S:
    S.append(n)
    S.sort()
    
    index = S.index(n)

    if index == len(S)-1:
        row = S[index-1]
        high = 1000
        
        row_count = n-row
        high_count = high-n

        result = row_count*(high_count) - 1

        print(result)        
    elif index == 0:
        row = 0
        high = S[1]

        row_count = n-row
        high_count = high-n

        result = row_count*(high_count) - 1

        print(result)
    else:
        row = S[index-1]
        high = S[index+1]

        row_count = n-row
        high_count = high-n

        result = row_count*(high_count) - 1

        print(result)
else:
    print(0)