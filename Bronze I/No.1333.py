N, L, D = map(int, input().split())

song_t = 0
time_s = []
phone = 0

for i in range(N):
    time_s.append((song_t, song_t + L - 1))
    song_t += L + 5

while True:
    flag = True
    for s, e in time_s:
        if s <= phone <= e:
            flag = False
            break
    
    if flag:
        print(phone)
        break

    phone += D