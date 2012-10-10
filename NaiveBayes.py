from sklearn.naive_bayes import GaussianNB
from SciKitLearner import SciKitLearner

class NaiveBayes(SciKitLearner):
   def __init__(self, testSet, trainSet, classifiers):
      super(NaiveBayes, self).\
            __init__(testSet, trainSet, classifiers, GaussianNB())
   def predict(self,example):
      print example