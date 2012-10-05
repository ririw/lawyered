from sklearn.naive_bayes import GaussianNB
from Data import DataSet
import numpy as np

class NaiveBayes(object):
   def __init__(self, testSet, trainSet, classifiers):
      assert(isinstance(testSet, DataSet))
      assert(isinstance(trainSet, DataSet))
      assert(isinstance(classifiers, list))
      classes = ['Truth', 'Lie']
      classMap = {True: classes[0], False: classes[1]}

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
         testClasses.append(classMap[instance.isTrue])
      for instance in trainSet:
         trainFeature = []
         for classifier in classifiers:
            trainFeature.append(classifier.build(instance))
         trainFeatures.append(trainFeature)
         trainClasses.append(classMap[instance.isTrue])

      gnb = GaussianNB()
      self.naiveBayesClassifier = gnb.fit(trainFeatures, trainClasses)
      pred_class = self.naiveBayesClassifier.predict(testFeatures)
      total_errors = (pred_class != np.array(testClasses)).sum()
      self.accuracy = 1.0 - float(total_errors)/float(len(testClasses))

   def classify(self, instances):
      features = []
      for instance in instances:
         feature = []
         for classifier in self.classifiers:
            feature.append(classifier.build(instance))
         features.append(feature)
      return self.naiveBayesClassifier.predict(features)
