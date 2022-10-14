#бонусное задание
while True:
    try:
        N = int(input("Введите количество элементов массива A: "))#вводим размерность
        break
    except ValueError:#проверяем на ошибку ввода
        print("Вы ввели не целое число. Попробуйте снова: ")
A = [0] * N#создаем массив
from random import randint
for i in range(N):#заполняем массив случайными числами
        A[i] = randint(0, 99)
print("Входной массив:", A)
while True:
    try:
        Delta = int(input("Введите Delta: "))#вводим значение delta
        break
    except ValueError:#проверяем на ошибку ввода
        print("Вы ввели не целое число. Попробуйте снова: ")
min = 100#минимальное число
nr = 0#номер минимального числа
for n in range(N):#перебором находим минимальное число
    if A[n] < min:
        min = A[n]
        nr = n
print("Минимальный элемент массива:", min)
k = 0#счетчик количества элементов
for m in range(N):#
    if A[m] - min == Delta:
        k += 1
print("Результат:", k)
