#задание 1
N = int(input("Введите количество элементов массива: "))
A = [0] * N
sp = int(input("Введите '1' для самостоятельного ввода массива, либо введите любое другое число: "))
if sp == 1:
    print("Введите", N, "элементов:")
    for k in range (N):
        print("A[", k, "] = ", end="")
        A[k] = float(input())
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
