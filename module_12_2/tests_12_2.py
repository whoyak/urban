import unittest
from Runner import Runner
from Runner import Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll Results:")
        for key, value in cls.all_results.items():
            formatted_results = {k: str(v) for k, v in value.items()}
            print(f'{key}: {formatted_results}')

    def test_usain_vs_nick(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results["usain_vs_nick"] = results
        self.assertTrue(results[1] == self.runner1)
        self.assertTrue(results[2] == self.runner3)

    def test_andrey_vs_nick(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["andrey_vs_nick"] = results
        self.assertTrue(results[1] == self.runner2)
        self.assertTrue(results[2] == self.runner3)

    def test_usain_andrey_vs_nick(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results["usain_andrey_vs_nick"] = results
        self.assertTrue(results[1] == self.runner1)
        self.assertTrue(results[2] == self.runner2)
        self.assertTrue(results[3] == self.runner3)
