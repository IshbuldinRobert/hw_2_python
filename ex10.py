# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random
n = input('Введите количество монет: ')

while not n.isdigit():
    print('Некорректный ввод!!!')
    n = input('Введите количество монет: ')

n = int(n)
eagle = 0
tails = 0

print('На столе рандомной стороной лежат монетки (0 - орел, 1 - решка) \nНужно перевернуть минимальное количество монеток, чиобы все они лежали одной стороной')
for i in range(n):
    temp = random.randint(0, 1)
    print(temp)
    if temp == 0:
        eagle += 1
    elif temp == 1:
        tails += 1

if eagle < tails and eagle != 0:
    print(f'Нужно перевернуть монет: {eagle}')
elif eagle > tails and tails != 0:
    print(f'Нужно перевернуть монет: {tails}')
elif eagle == 0 or tails == 0:
    print('Все монетки лежат одной стороной, ничего переворачивать не надо (*^*)')
else:
    print(f'Орлов и решек поровну, поэтому нужно превернуть половину от количества всех монеток, т.е. {int(n / 2)}')