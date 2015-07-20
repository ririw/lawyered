import unittest
from TestSciKitClassifier import TestSciKitClassifier
import NaiveBayes

class TestNaiveBayes(unittest.TestCase, TestSciKitClassifier):
   def testedClass(self):
      return NaiveBayes.NaiveBayes

if __name__=="__main__":
   unittest.main()
