from sklearn import tree
from Data import DataSet
import numpy as np

class ClassificationTree(object):
   def __init__(self, testSet, trainSet, classifiers):
      assert(isinstance(testSet, DataSet))
      assert(isinstance(trainSet, DataSet))
      assert(isinstance(classifiers, list))
      classes = [1, 0]
      self.classMap = {True: classes[0], False: classes[1]}
      self.inverseClasses = {classes[0]: 'Truth', classes[1]: 'Lie'}

      testFeatures = []
      testClasses = []
      trainFeatures = []
      trainClasses = []

      self.classifiers = classifiers

      for instance in testSet:
         testFeature = []
         for classifier in classifiers:
            testFeature.append(classifier.build(instance))
         testFeatures.append(testFeature)
         testClasses.append(self.classMap[instance.isTrue])
      for instance in trainSet:
         trainFeature = []
         for classifier in classifiers:
            trainFeature.append(classifier.build(instance))
         trainFeatures.append(trainFeature)
         trainClasses.append(self.classMap[instance.isTrue])

      clt = tree.DecisionTreeClassifier()
      self.classificationTree = clt.fit(trainFeatures, trainClasses)
      print testFeatures
      pred_class = self.classificationTree.predict(testFeatures)
      total_errors = (pred_class != np.array(testClasses)).sum()
      self.accuracy = 1.0 - float(total_errors)/float(len(testClasses))

   def classify(self, instances):
      features = []
      for instance in instances:
         feature = []
         for classifier in self.classifiers:
            feature.append(classifier.build(instance))
         features.append(feature)
      return map(lambda r: self.inverseClasses[r], self.classificationTree.predict(features))
