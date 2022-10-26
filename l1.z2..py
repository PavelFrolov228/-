print("введите скорость ракеты (км/с)")
v = float(input())
if 0 < v <= 7.8:
    print(0)
elif 7.8 < v < 11.2:
    print(1)
elif 11.2 <= v <= 16.4:
    print(2)
elif v > 16.4:
    print(3)
else:
    print("error")
