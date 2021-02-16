class Cell:
    def __init__(self, cells_amount):
        self.cells_amount = cells_amount

    def __add__(self, other):
        return self.cells_amount + other.cells_amount

    def __sub__(self, other):
        if self.cells_amount > other.cells_amount:
            return self.cells_amount - other.cells_amount
        else:
            return 'Результат вычитания меньше нуля'

    def __mul__(self, other):
        return self.cells_amount * other.cells_amount

    def __truediv__(self, other):
        return self.cells_amount // other.cells_amount

    def make_order(self, cells_in_line):
        lines = self.cells_amount // cells_in_line
        for line in range(lines):
            print(cells_in_line * '*')
        print(self.cells_amount % cells_in_line * '*')


cell1 = Cell(12)
cell2 = Cell(7)
cell1.make_order(3)
cell2.make_order(5)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell2 - cell1)
print(cell1 * cell2)
print(cell1 / cell2)
