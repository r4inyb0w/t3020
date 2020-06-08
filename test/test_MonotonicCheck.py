import unittest
import io
import sys
from code.datamunger import check_monotonic

currTester = [712, 70, 140, 44, 39, 227, 93, 40, 49, 50]
prev = [800,0,0,0,0,0,0,0,0,0]
strVal = ''

class DataMungerMonotonicTest(unittest.TestCase):   
    def test_MonotonicCheck(self):
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        check_monotonic(prev, currTester)
        sys.stdout = sys.__stdout__

        n = 4

        self.assertEqual(captureOutput.getvalue(), 'Monotonic error at column 0 comparing lines 21 and 22   values 712 and 800\n')

if __name__== '__main__':
    unittest.main()