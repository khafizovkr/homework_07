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
        m = ''
        for line in self.matrix:
            m += '\n'
            for number in line:
                m += str(number) + ' '
        return m

    def __add__(self, other):
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
        return Matrix(result)


my_matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
my_matrix2 = Matrix([[1, 1], [1, 1], [1, 1]])
sum_matrix = my_matrix1 + my_matrix2
print(my_matrix1)
print(my_matrix2)
print(sum_matrix)
