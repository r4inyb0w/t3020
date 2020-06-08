import unittest
from code.datamunger import calc_total

class DataMungerCalcTotalTest(unittest.TestCase):
    def test_CalcTotalError(self):
        currTester = [712, 70, 140, 44, 39, 227, 93, 40, 49, 50]
        total = calc_total(currTester)
        self.assertNotEqual(total, 712)

    def test_CalcTotalCorrect(self):
        currTester = [726, 73, 142, 49, 40, 236, 93, 50, 43, 0]
        total = calc_total(currTester)
        self.assertEqual(total, 726)


if __name__== '__main__':
    unittest.main()