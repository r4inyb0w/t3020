import unittest
from code.datamunger import check_row

prev = [0,0,0,0,0,0,0,0,0,0]

class DataMungerRowCheckTest(unittest.TestCase):
    def test_RowCheckMissing(self):
        strVal = ['80', '', '', '', '', '', '', '', '', '']
        result = check_row(2, prev, strVal)
        self.assertEqual(result, False)
    
    def test_RowCheckFull(self):
        strValFull = ['748', '73', '143', '49', '43', '237', '97', '50', '56', '']
        resultFull = check_row(2, prev, strValFull)
        self.assertEqual(resultFull, True)


if __name__== '__main__':
    unittest.main()
    