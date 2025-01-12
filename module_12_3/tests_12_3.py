import unittest
from Runner import Runner
from Runner import Tournament

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
        self.runner1.walk()
        self.runner1.walk()
        self.runner1.walk()
        self.assertEqual(self.runner1.distance, 10 * 3)

    @skip_if_frozen
    def test_run(self):
        self.runner1.run()
        self.runner1.run()
        self.runner1.run()
        self.assertEqual(self.runner1.distance, 10 * 2 * 3)

    @skip_if_frozen
    def test_challenge(self):
        self.runner1.run()
        self.runner2.walk()
        self.assertNotEqual(self.runner1.distance, self.runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrey", 9)
        self.runner3 = Runner("Nick", 3)

    @skip_if_frozen
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.assertEqual(results[1], self.runner1)
        self.assertEqual(results[2], self.runner3)

    @skip_if_frozen
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(results[1], self.runner2)
        self.assertEqual(results[2], self.runner3)

    @skip_if_frozen
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.assertEqual(results[1], self.runner1)
        self.assertEqual(results[2], self.runner2)
        self.assertEqual(results[3], self.runner3)
