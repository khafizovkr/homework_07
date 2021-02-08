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
