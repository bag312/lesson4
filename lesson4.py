#Задание 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
#необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
#Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка в у.е. '))
        bonus = int(input('Премия в у.е. '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Ошибка. Вы ввели не число')
sal()

#Задание 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

list = [18, 32, 5, 1, 71, 35, 44, 120]
new_list = [el for num, el in enumerate(list) if list[num - 1] < list[num]]
print(f'Исходный список {list}')
print(f'Новый список {new_list}')


#Задние 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#Задние 4.Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
#соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
new_list = [el for el in list if list.count(el) == 1]

print(new_list)


#Задние 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
#В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат
#вычисления произведения всех элементов списка. Подсказка: использовать функцию reduce().

from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#Задние 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
#При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fibo_gen().
#Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
#Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break 

#Задние 6. Реализовать два небольших скрипта:
#а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el) # беконечный цикл!

from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el) # беконечный цикл!

