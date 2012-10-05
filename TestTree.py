import unittest
import Data
from Feature import ContinuousFeature,DiscreetFeature
import random
import ClassificationTree
import string
import numpy as np
class MoreThan10Chars(DiscreetFeature):
   def build(self, data):
      return self.test(data.string)
   def test(self, string):
      return len(string) > 10
class MoreThan2Caps(DiscreetFeature):
   def build(self, data):
      return self.test(data.string)
   def test(self, string):
      return len(filter(lambda c: c in string.uppercase, string)) > 2
class NumChars(ContinuousFeature):
   def build(self, data):
      return len(data.string)
class NumCaps(ContinuousFeature):
   def build(self, data):
      return len(filter(lambda c: c in string.uppercase, data.string))
   def test(self, strin):
      return len(filter(lambda c: c in string.uppercase, strin))



class TestClassificationTree(unittest.TestCase):
   trainSize = 200
   testSize = 200
   def buildDataSet(self, classifiers, classificationFn):
      trainStrs = [''.join(random.choice(string.letters + string.digits) 
         for x in range(random.randrange(20)))
         for y in range(self.trainSize)]
      testStrs = [''.join(random.choice(string.letters + string.digits) 
         for x in range(random.randrange(20)))
         for y in range(self.testSize)]
      trainItems = map(lambda s: Data.Data(s, classificationFn(s)),
            trainStrs)
      testItems = map(lambda s: Data.Data(s, classificationFn(s)),
            testStrs)
      trainSet = Data.DataSet(trainItems)
      testSet = Data.DataSet(testItems)
      return ClassificationTree.ClassificationTree(testSet, trainSet, classifiers)

   def test_OneR_success(self):
      mt10c = MoreThan10Chars()
      classificationFn = mt10c.test
      classifiers = [MoreThan10Chars()]
      bayes = self.buildDataSet(classifiers, classificationFn)
      assert(bayes.accuracy > 0.9)
   def test_OneR_fail(self):
      mt10c = MoreThan10Chars()
      classificationFn = lambda s: random.random()>0.5
      classifiers = [MoreThan10Chars()]
      bayes = self.buildDataSet(classifiers, classificationFn)
      assert(bayes.accuracy < 0.7)
   def testTwoR_success(self):
      mt10c = MoreThan10Chars()
      classificationFn = mt10c.test
      classifiers = [MoreThan10Chars(), NumChars()]
      bayes = self.buildDataSet(classifiers, classificationFn)
      assert(bayes.accuracy > 0.7)
   def testThreeR_compex(self):
      mt10c = MoreThan10Chars()
      nCaps = NumCaps()
      classificationFn = lambda s: mt10c.test(s) or \
            (nCaps.test(s) + random.random()*0.5 > 1)
      classifiers = [MoreThan10Chars(), NumChars(), NumCaps()]
      bayes = self.buildDataSet(classifiers, classificationFn)
      assert(bayes.accuracy > 0.7)
   def testOneR_complex(self):
      nCaps = NumCaps()
      classificationFn = lambda s: (nCaps.test(s) + random.random()*0.5 > 1)
      classifiers = [MoreThan10Chars(), NumChars(), NumCaps()]
      bayes = self.buildDataSet(classifiers, classificationFn)
      assert(bayes.accuracy > 0.7)
   def test_classify(self):
      mt10c = MoreThan10Chars()
      classificationFn = mt10c.test
      classifiers = [MoreThan10Chars()]
      bayes = self.buildDataSet(classifiers, classificationFn)
      assert(bayes.accuracy > 0.9)
      dataset = [Data.Data("asdfqwer", False),
            Data.Data("asdasdasdad", False)
            ]
      result =  bayes.classify(dataset) 
      assert(result[0] == 'Lie')
      assert(result[1] == 'Truth')

if __name__=="__main__":
   unittest.main()
