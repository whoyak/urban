import math


class Figure:
    sides_count = 0

    def __init__(self, sides: list, color=None, filled: bool = False):
        self.__sides = sides if all(isinstance(side, int) and side > 0 for side in sides) else []
        self.__color = color if color and self.__is_valid_color(*color) else [0, 0, 0]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r: int, g: int, b: int):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        return False

    def set_color(self, r: int, g: int, b: int):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]
        else:
            print(f'Некорректные значения цвета. Цвет остался прежним.')

    def __is_valid_sides(self,sides):
        if not all(isinstance(side,int) and side > 0 for side in sides):
            return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self,*new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        else:
            print("Количество сторон не совпадает с ожидаемым ")
            return self.__sides



class Circle(Figure):
    sides_count = 1
    def __init__(self, color=None, len_square: float = 0, filled: bool = False):
        self.__len_square = len_square
        self.__radius = len_square/(2*math.pi)
        super().__init__([len_square], color, filled)

    def get_square(self):
        return math.pi*self.__radius**2

class Triangle(Figure):
    sides_count = 3
    def __init__(self,a:float,b:float,c:float,color = None,filled:bool=False):
        super().__init__([a,b,c],color,filled)

    def get_sides(self):
        return self.__sides

    def get_square(self,):
        a,b,c = self.get_sides()
        s = (a+b+c)/2
        area = math.sqrt(s*(s-a)*(s-b)*(s-c))
        return area

class Cube(Figure):
    sides_count = 12

    def __init__(self, color=None, side: int = 1, filled: bool = False):
        sides = [side] * self.sides_count
        super().__init__(sides, color, filled)

    def set_side(self, side):
        self.__sides = [side] * self.sides_count

    def get_volume(self):
        return self._Figure__sides[0] ** 3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())