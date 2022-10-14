#задание 2
while True:
    try:
        N1 = int(input("Введите количество элементов массива A: "))#вводим размерность массива А
        N2 = int(input("Введите количество элементов массива B: "))#вводим размерность массива В
        break
    except ValueError:#проверяем на ошибку ввода
        print("Вы ввели не целое число. Попробуйте снова: ")
A = [0] * N1#создаем массив А
B = [0] * N2#создаем массив В
while True:
    try:
        sp = int(input("Введите '1' для самостоятельного ввода массивов, либо введите любое другое число: "))#
        break
    except ValueError:#проверяем на ошибку ввода
        print("Вы ввели не целое число. Попробуйте снова: ")
if sp == 1:#заполнение массива с клавиатуры
    print("Введите", N1, "элементов для массива A:")
    for k in range(N1):#заполняем массив А
        while True:
            try:
                print("A[", k, "] = ", end=" ")
                A[k] = float(input())
                break
            except ValueError:#проверяем на ошибку ввода
                print("Вы ввели не число. Попробуйте снова: ")
    print("Введите", N2, "элементов для массива B:")
    for l in range(N2):#заполняем массив В
        while True:
            try:
                print("B[", l, "] = ", end=" ")
                B[l] = float(input())
                break
            except ValueError:#проверяем на ошибку ввода
                print("Вы ввели не число. Попробуйте снова: ")
else:#заполнение массива случайными числами
    from random import random
    for i in range(N1):
        A[i] = round(random() * 10, 1)
    for z in range(N2):
        B[z] = round(random() * 10, 1)
print("Входые массивы:", A, B)
print("Общие элементы массивов: ", end="")
for o in range(N1):#перебором находим общие элементы массивов
    for u in range(N2):
        if A[o] == B[u]:
            print(A[o], end = " ")
