import unittest

from bowling_score_calculator import BowlingScoreCalculator


class BowlingScoreCalculatorTest(unittest.TestCase):
    def test(self):
        calculator = BowlingScoreCalculator()
        self.assertEqual(193, calculator.seq_score("6/XXX3/X3/2/4/X31"))
        self.assertEqual(150, calculator.seq_score("3/15XXX8-3/-/368/7"))


if __name__ == '__main__':
    unittest.main()
