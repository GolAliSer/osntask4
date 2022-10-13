#бонусное задание
while True:
    try:
        N = int(input("Введите количество элементов массива A: "))
        break
    except ValueError:
        print("Вы ввели не целое число. Попробуйте снова: ")
A = [0] * N
from random import randint
for i in range(N):
        A[i] = randint(0, 99)
print("Входной массив:", A)
while True:
    try:
        Delta = int(input("Введите Delta: "))
        break
    except ValueError:
        print("Вы ввели не целое число. Попробуйте снова: ")
min = 100
nr = 0
for n in range(N):
    if A[n] < min:
        min = A[n]
        nr = n
print("Минимальный элемент массива:", min)
k = 0
for m in range(N):
    if A[m] - min == Delta:
        k += 1
print("Результат:", k)
