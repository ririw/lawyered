from sklearn import tree
from Data import DataSet
import numpy as np
from SciKitLearner import SciKitLearner

class ClassificationTree(SciKitLearner):
   def __init__(self, testSet, trainSet, classifiers):
      super(ClassificationTree, self).\
            __init__(testSet, trainSet, classifiers, 
                  tree.DecisionTreeClassifier())
