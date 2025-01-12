import unittest
from tests_12_3 import RunnerTest, TournamentTest


def suite():
    test_suite = unittest.TestSuite()

    test_suite.addTest(unittest.makeSuite(RunnerTest))
    test_suite.addTest(unittest.makeSuite(TournamentTest))

    return test_suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
