import unittest
from Runner import Runner  # Замените на правильный путь к классу Runner


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        # Создаём объект Runner с произвольным именем
        runner = Runner("John")

        # Вызываем метод walk 10 раз
        for _ in range(10):
            runner.walk()

        # Проверяем, что distance после 10 вызовов метода walk равен 50
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        # Создаём объект Runner с произвольным именем
        runner = Runner("Jane")

        # Вызываем метод run 10 раз
        for _ in range(10):
            runner.run()

        # Проверяем, что distance после 10 вызовов метода run равен 100
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        # Создаём два объекта Runner с разными именами
        runner1 = Runner("John")
        runner2 = Runner("Jane")

        # Вызываем методы run и walk 10 раз соответственно
        for _ in range(10):
            runner1.run()
        for _ in range(10):
            runner2.walk()

        # Проверяем, что distance у объектов различаются
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
