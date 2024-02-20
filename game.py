field = [['-' for i in range(3)] for j in range(3)]   # Создание двумерного массива

def visual():   # Функция визуализации поля
    print('  0 1 2')
    for i in range(3):
        row = ' '.join(field[i])
        print(f'{i} {row}')

def coordinates():   # Функция запроса координат
    while True:

        x = input('Введите координату строки: ')
        y = input('Введите координату столбца: ')

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа')
            continue

        x = int(x)
        y = int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print('Вы ввели неправильные координаты')
            continue

        if field[x][y] != '-':
            print('Клетка занята')
            continue

        return x, y

def win():   # Функция проверки выиграшной комбинации

    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != '-':
            return True

    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] != '-':
            return True

    if (field[0][0] == field[1][1] == field[2][2] != '-') or (field[0][2] == field[1][1] == field[2][0] != '-'):
        return True

num = 0

while True:
    num += 1

    visual()

    if num % 2 == 0:
        print('Ходит крестик')
        x, y = coordinates()
        field[x][y] = 'X'
    else:
        print('Ходит нолик')
        x, y = coordinates()
        field[x][y] = '0'

    winner = win()

    if winner:
        visual()
        print(f'Победили {field[x][y]}-ки')
        break

    if num == 9:
        visual()
        print('Ничья')
        break





