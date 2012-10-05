from sklearn.ensemble import RandomForestClassifier
from SciKitLearner import SciKitLearner

class RandomForest(SciKitLearner):
   def __init__(self, testSet, trainSet, classifiers):
      super(RandomForest, self).\
            __init__(testSet, trainSet, classifiers, RandomForestClassifier())
