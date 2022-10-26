lst_numbers = list(map(int, input('Введите числа через пробел: ').split()))
if len(lst_numbers) < 4:
    print("Вы ввели менее 4 чисел")
    quit()

lst_no_extremum = [lst_number for lst_number in lst_numbers if
                   lst_number != max(lst_numbers) and lst_number != min(lst_numbers)]
print(lst_numbers)
print(lst_no_extremum)