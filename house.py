class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'Вы переехали на {new_floor} этаж, в доме {self.name}')
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'

h1 = House('ЖК Весенний', 18)
h2 = House('ЖК СНТ-АГРО', 2)
h1.go_to(8)
h2.go_to(5)
print(h1)
print(h2)
print(len(h1))
print(len(h2))









