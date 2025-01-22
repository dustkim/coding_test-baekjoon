# baekjoon no.2480

x, y, z = map(int, input().split())

if (x == y == z):
    print("{}".format(10000+(x*1000)))
elif(x == y or x == z):
    print("{}".format(1000+(x*100)))
elif(y == z):
    print("{}".format(1000+(y*100)))
else:
    if(x > y and x > z):
        print("{}".format(x*100))
    elif(y > x and y > z):
        print("{}".format(y*100))
    elif(z > x and z > y):
        print("{}".format(z*100))