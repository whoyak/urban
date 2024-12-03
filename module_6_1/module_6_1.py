class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел(а) {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не может съесть {food.name}!")
            self.alive = False

class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел(а) {food.name}.")
            self.fed = True
        else:
            print(f"{self.name} не может съесть {food.name}!")
            self.alive = False



class Plant:

    def __init__(self,name):
        self.name = name
        self.edible = False
class Flower(Plant):

    def __init__(self, name):
        self.name = name
        self.edible = False
class Fruit(Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)