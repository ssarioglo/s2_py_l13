import random

def pm(t):
    for i in t:
        print(i)

#Создаем две матрицы 10 х 10
print("Введите размерности матриц (a b): ", end='')
a, b = map(int, input().split())

m1 = [[random.randint(0, 9) for i in range(b)] for i in range(a)]      # Заполняем матрицы случайными числами
m2 = [[random.randint(0, 9) for i in range(b)] for i in range(a)]      #
m3 = [[0 for i in range(b)] for i in range(a)]                          # Матрицу результата заполняем нулями

print("Матрица 1")
pm(m1)
print()
print("Матрица 2")
pm(m2)

#Циклом проходим по элементам и складываем
for i in range(0, a):   
    for j in range(0, b):
        m3[i][j] = m1[i][j] + m2[i][j]

print()
print("Матрица 3, сумма двух предыдущих")
pm(m3)