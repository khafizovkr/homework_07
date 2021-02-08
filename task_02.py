# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def __str__(self):
        return self.cloth_consumption

    @abstractmethod
    def cloth_consumption(self):
        pass


class Coat(Clothes):
    @property
    def cloth_consumption(self):
        return f'Количетво ткани на пальто {round(self.size / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    @property
    def cloth_consumption(self):
        return f'Количетво ткани на костюм {round(self.height * 2 + 0.3, 2)}'


coat = Coat(48, 1.78)
suit = Suit(48, 1.78)

print(coat)
print(suit)
