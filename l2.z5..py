n = int(input("Введите количество моряков: "))
team1 = []
team2 = []
for i in range(n):
    nameage = input().split()
    name = nameage[0]
    age = int(nameage[1])
    if age > 40 or age < 20:
        team1.append(name)
    else:
        team2.append(name)

team1.sort()
team2.sort()

print("Команда 1:", end=' ')
print(*team1, sep=', ')

print("Команда 2:", end=' ')
print(*team2, sep=', ')