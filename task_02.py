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
