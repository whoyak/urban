import unittest
import logging
from Runner import Runner  # Импортируем класс Runner

# Настройка логирования
logging.basicConfig(
    filename='runner_tests.log',  # Имя файла для логов
    level=logging.INFO,  # Уровень логирования
    format='%(asctime)s - %(levelname)s - %(message)s',  # Формат сообщения
    encoding='utf-8'  # Кодировка
)

def skip_if_frozen(func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            print(f"Тест {func.__name__} пропущен: Тесты в этом кейсе заморожены")
            raise unittest.SkipTest(f'Тесты в этом кейсе заморожены')
        return func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @skip_if_frozen
    def test_walk(self):
        try:
            # Попробуем передать отрицательную скорость
            self.runner1 = Runner("Usain", -5)  # Это вызовет исключение ValueError
            self.runner1.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner: {e}")  # Логируем предупреждение

    @skip_if_frozen
    def test_run(self):
        try:
            # Попробуем передать неверный тип для имени
            self.runner1 = Runner(123, 10)  # Это вызовет исключение TypeError
            self.runner1.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f"Неверный тип данных для объекта Runner: {e}")  # Логируем предупреждение

    @skip_if_frozen
    def test_challenge(self):
        self.runner1.run()
        self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)
