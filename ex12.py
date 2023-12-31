# Задача №12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

print("Загаданы два числа")
sum = input("Введите сумму этих чисел: ")

while not sum.isdigit():
    print('Неверный формат')
    sum = input("Введите сумму этих чисел: ")
sum = int(sum)

prod = input("Введите произведение этих чисел: ")

while not prod.isdigit():
    print('Неверный формат')
    prod = input("Введите произведение этих чисел: ")
prod = int(prod)

n = 1
while prod != (sum - n) * n:
    n += 1
print(f"Загаданные числа {sum - n} и {n}")