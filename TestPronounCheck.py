'''
Created on 11/10/2012

@author: Sam Townsend
'''
import unittest
import PronounCheck
from Data import Data

class TestPronounCheck(unittest.TestCase):


    def test_PronounCheck(self):
        
        p = PronounCheck.PronounCheck()
        cases = {"""I am a Cat.""": 1}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(p.build(d) == count)

if __name__ == "__main__":
    unittest.main()