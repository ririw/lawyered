import unittest
from TestSciKitClassifier import TestSciKitClassifier
import RandomForest

class TestRandomForest(unittest.TestCase, TestSciKitClassifier):
   def testedClass(self):
      return RandomForest.RandomForest

if __name__=="__main__":
   unittest.main()
