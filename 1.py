#задание 1
while True:
    try:
        N = int(input("Введите количество элементов массива: "))
        break
    except ValueError:
        print("Вы ввели не целое число. Попробуйте снова: ")
A = [0] * N
while True:
    try:
        sp = int(input("Введите '1' для самостоятельного ввода массива, либо введите любое другое число: "))
        break
    except ValueError:
        print("Вы ввели не целое число. Попробуйте снова: ")
if sp == 1:
    print("Введите", N, "элементов:")
    for k in range (N):
        while True:
            print("A[", k, "] = ", end="")
            try:
                A[k] = float(input())
                break
            except ValueError:
                print("Вы ввели не число. Попробуйте снова: ")
else:
    from random import random
    for i in range(N):
        A[i] = round(random() * 10, 1)
print("Входной массив:", A)
max = 0
nr = 0
for n in range(N):
    if A[n] > max:
        max = A[n]
        nr = n
print("Максимальный элемент массива:", max)
for m in range(N):
    if m > nr:
        A[m] = 0
print("Результат:", A)
