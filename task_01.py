# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух
# матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for line in self.matrix:
            print(f'\n')
            for number in line:
                f'{number}    ', end=''


my_matrix = Matrix([[31, 22], [37, 43], [51, 86]])
str(my_matrix)
