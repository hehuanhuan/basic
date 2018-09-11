import unittest
from basic.calculator import Count

class test1(unittest.TestCase):
    def addtest(self):
        self.Count=Count(2,3)
        self.assertEqual(self.Count.add(),5)


if __name__=="__main__":
    a=unittest.TestSuite()
    a.addTest(test1("addtest"))