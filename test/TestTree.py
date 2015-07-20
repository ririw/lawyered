import unittest
from TestSciKitClassifier import TestSciKitClassifier
import ClassificationTree

class TestClassificationTree(unittest.TestCase, TestSciKitClassifier):
   def testedClass(self):
      return ClassificationTree.ClassificationTree

if __name__=="__main__":
   unittest.main()
