import numpy as np

"""
Создать "шахматную доску" на numpy:
n - строки
m - столбцы
"""
def chessboard(n , m):
    a = np.zeros((n,m), dtype = np.int)
    a[0:n:2, 0:m:2] = 1
    a[1:n:2, 1:m:2] = 1
    return a

chessboard(3,4)


"""
Создать случайный вектор и занулить три самых больших по модулю значения
n - размер векктора
m - значения a[i] принадлежат [-m;m)
"""
def rand_v(n, m = 1):
    a = (np.random.rand(n) - 0.5) * m
    if n >= 3:
        a[np.argpartition(a, -3)[-3:]] = 0
        return a
    else:
        return a
    
rand_v(6)


"""
Диагональная матрица с квадратами натуральных чисел
N - размер матрицы NхN
"""
def matr(N):
    a = np.diag(np.arange(1, N+1, dtype = np.int)**2)
    return a
    
matr(4)


'''
Змейка 
[[ 1  6 11 16 21]
 [ 2  7 12 17 22]
 [ 3  8 13 18 23]
 [ 4  9 14 19 24]
 [ 5 10 15 20 25]]
 
n - строки
m - столбцы
'''

def snake(n, m):
    a = np.arange(1,n * m + 1).reshape(n,m).T
    a[:, 1::2] = a[::-1, 1::2]
    return a

snake(3, 5)


"""
Евклидово расстояние между вектором и всеми строчками матрицы
n - строки
m - столбцы
"""
def Euclidean_distance(n, m):
    X = np.arange(n, dtype = float)
    Y = np.arange(n * m, dtype = float).reshape(m,n)
    return ((X - Y[:])**2).sum(axis = 1)**0.5

Euclidean_distance(3, 5)


'''
Косинусное расстояние для векторов
n - размер вектора
'''
def Cosine_distance(n):
    X = np.arange(n, dtype = float)
    Y = np.arange(3, n + 3, dtype = float)

    x_y = (X * Y).sum(axis = 0)
    x_x = (X * X).sum(axis = 0)
    y_y = (Y * Y).sum(axis = 0)
    return np.arccos(x_y / (x_x**0.5 * y_y**0.5))
    
Cosine_distance(3)


"""
Косинусное расстояние между вектором и всеми строчками матрицы
n - строки
m - столбцы
"""
def Cosine_distance_matr(n, m):
    X = np.arange(n, dtype = float)
    Y = np.arange(n * m, dtype = float).reshape(m,n)

    x_y = (X * Y[:]).sum(axis = 1)
    x_x = (X * X).sum(axis = 0)
    y_y = (Y * Y).sum(axis = 1)
    return np.arccos(x_y / (x_x**0.5 * y_y**0.5))

Cosine_distance_matr(3, 4)