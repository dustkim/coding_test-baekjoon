T = int(input())

fibonacci_List = [(1, 0), (0, 1)]

for i in range(2, 41):
    zero = fibonacci_List[i-1][0] + fibonacci_List[i-2][0]
    one = fibonacci_List[i-1][1] + fibonacci_List[i-2][1]
    fibonacci_List.append((zero, one))

for _ in range(T):
    case = int(input())
    print(fibonacci_List[case][0], fibonacci_List[case][1])