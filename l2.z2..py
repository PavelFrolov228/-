numbers = [2, 3, 4, 5, 6, 7]
x_min = min(numbers)
x_max = max(numbers)
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i]*=x_min
    else:
        numbers[i]*=x_max
print("Максимальный элемент: ", x_max)
print("Минимальный элемент: ", x_min)
print(numbers)