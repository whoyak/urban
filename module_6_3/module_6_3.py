import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, cords=None, speed: float = 0.0):
        self._cords = cords if cords is not None else [0, 0, 0]
        self.speed = speed

    def move(self, dx: float, dy: float, dz: float):
        new_x = self._cords[0] + dx * self.speed
        new_y = self._cords[1] + dy * self.speed
        new_z = self._cords[2] + dz * self.speed
        if new_z < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = new_x
            self._cords[1] = new_y
            self._cords[2] = new_z

    def get_cords(self):
        return print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            return "Sorry, I'm peaceful :)"
        else:
            return "Be careful, I'm attacking you 0_0"

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print("No sound")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        return print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz
        self.speed /= 2


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    sound = "Click-click-click"

    def __init__(self, cords=None, speed: float = 0.0):
        super().__init__(cords, speed)

    def move(self, dx, dy, dz):
        super().move(dx, dy, dz)

    def lay_eggs(self):
        return super().lay_eggs()


db = Duckbill([0, 0, 0], 10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
