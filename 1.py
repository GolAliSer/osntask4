#задание 1
while True:
    try:
        N = int(input("Введите количество элементов массива: "))#вводим размерность
        break
    except ValueError:#проверяем на ошибку ввода
        print("Вы ввели не целое число. Попробуйте снова: ")
A = [0] * N#создаем массив
while True:
    try:
        sp = int(input("Введите '1' для самостоятельного ввода массива, либо введите любое другое число для генерации случайных чисел: "))   #выбираем способ заполнения массива
        break
    except ValueError:#проверяем на ошибку ввода                                             
        print("Вы ввели не целое число. Попробуйте снова: ")
if sp == 1:#заполнение массива с клавиатуры
    print("Введите", N, "элементов:")
    for k in range (N):
        while True:
            print("A[", k, "] = ", end="")
            try:
                A[k] = float(input())
                break
            except ValueError:#проверяем на ошибку ввода
                print("Вы ввели не число. Попробуйте снова: ")
else:#заполнение массива случайными числами
    from random import random
    for i in range(N):
        A[i] = round(random() * 10, 1)
print("Входной массив:", A)
max = 0#максимальный элемент
nr = 0#номер максимального элемента
for n in range(N):#перебором находим максивамальный элемент
    if A[n] > max:
        max = A[n]
        nr = n
print("Максимальный элемент массива:", max)
for m in range(N):#перебором зануляем элементы, стоящие после максимального
    if m > nr:
        A[m] = 0
print("Результат:", A)
