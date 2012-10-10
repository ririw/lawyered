'''
Created on 11/10/2012

@author: Sam Townsend
'''
import unittest
import Data
import random
import PronounCheck
import string

class TestPronounCheck(unittest.TestCase):


    def test_PronounCheck(self):
        
        p = PronounCheck.PronounCheck()
        p.build(text)

if __name__ == "__main__":
    unittest.main()