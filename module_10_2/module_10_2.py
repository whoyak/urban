import time
import threading

class Knight(threading.Thread):
    def __init__(self, name: str, power: int, enemies: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = enemies

    def run(self):
        days = 0
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            self.enemies -= self.power
            self.enemies = max(self.enemies, 0)
            days += 1

            print(f"{self.name} сражается {days} день(дня)... Осталось {self.enemies} воинов.")
            time.sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней!")


first_knight = Knight('Sir Lancelot', 10, 100)
second_knight = Knight("Sir Galahad", 20, 100)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()
print(f'Все битвы закончились')
