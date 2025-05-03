Resistance_Price = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

answer = 0
for i in range(3):
    color = input()
    if i == 0 and color in Resistance_Price:
        answer = Resistance_Price.index(color) * 10

    elif i == 1 and color in Resistance_Price:
        answer += Resistance_Price.index(color)
    else:
        answer *= pow(10, Resistance_Price.index(color))

print(answer)