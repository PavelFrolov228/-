a = "Where and when do you usually read"
words = a.split()
my_list = [len(word) for word in words]
result = min(my_list) + max(my_list)
print(words)
print(my_list)
print("Сумма минимального и максимального значения длин слов: ", result)