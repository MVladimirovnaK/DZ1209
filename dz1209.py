''' Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть'''

'''N = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Нужно перевернуть {orel} монет с орла на решку.')
elif orel == reshka:
    print(f'Нужно перевернуть {orel} монет с орла на решку.')
else:
    print((f'Нужно перевернуть {reshka} монет с решки на орла.'))'''

'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две 
подсказки. Он называет сумму этих чисел S и их произведение power. Помогите Кате отгадать задуманные Петей числа.'''

'''x = abs(int(input('Введите первое натуральное число X ')))
y = abs(int(input('Введите второе натуральное число Y ')))
S = x + y # система уравнений
P = x * y
print(S, P)
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2) # через D нашли, что корня 2
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)'''

'''Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.'''

N = abs(int(input('Введите число N: ')))
counter = 0
power = 2 # степень
for i in range(N):
    if counter != 1:
        power = power ** i
        if power <= N:
            print(power, end=' ')
            power = 2
        else:
            counter = 1
    else:
        i = N