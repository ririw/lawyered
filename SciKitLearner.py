from sklearn.naive_bayes import GaussianNB
from Data import DataSet
import numpy as np
from multiprocessing import Pool

def classify_instance(classifiers, classMap, instance):
   testFeature = []
   for classifier in classifiers:
      testFeature.append(classifier.build(instance))
   return (testFeature, classMap[instance.tag])

class SciKitLearner(object):
   def __init__(self, testSet, trainSet, classifiers, learner):
      assert(isinstance(testSet, DataSet))
      assert(isinstance(trainSet, DataSet))
      assert(isinstance(classifiers, list))
      classes = [1, 0]
      classMap = {True: 1, False: 0}
      self.inverseClassMap = {1: 'Truth', 0: 'Lie'} 

      testFeatures = []
      testClasses = []
      trainFeatures = []
      trainClasses = []

      self.classifiers = classifiers

      if True:
         for num_instance in enumerate(testSet):
            instance = num_instance[1]
            print float(num_instance[0])/float(len(testSet))
            testFeature = []
            for classifier in classifiers:
               testFeature.append(classifier.build(instance))
            testFeatures.append(testFeature)
            testClasses.append(classMap[instance.tag])
         for num_instance in enumerate(trainSet):
            instance = num_instance[1]
            print float(num_instance[0])/float(len(trainSet))
            trainFeature = []
            for classifier in classifiers:
               trainFeature.append(classifier.build(instance))
            trainFeatures.append(trainFeature)
            trainClasses.append(classMap[instance.tag])
      else:
         #see: http://stackoverflow.com/questions/5917522/unzipping-and-the-operator for an explanation of this unzip approach
         pool = Pool(processes=4)
         testFeatures, testClasses = zip(*(list(pool.map(lambda instance: classify_instance(classifiers, classMap, instance), testSet))))
         trainFeatures, trainClasses = zip(*(list(pool.map(lambda instance: classify_instance(classifiers, classMap, instance), trainSet))))

      self.learner = learner.fit(trainFeatures, trainClasses)
      pred_class = self.learner.predict(testFeatures)
      total_errors = (pred_class != np.array(testClasses)).sum()
      self.accuracy = 1.0 - float(total_errors)/float(len(testClasses))
      trueAnswers = len(filter(lambda c: c.tag, trainSet))
      falseAnswers = len(filter(lambda c: c.tag, trainSet))
      majorityAccuracy = float(max(trueAnswers, falseAnswers))/ \
            float(trueAnswers + falseAnswers)
      self.lift = (self.accuracy - majorityAccuracy)/(1.0-majorityAccuracy)

   def classify(self, instances):
      features = []
      for instance in instances:
         feature = []
         for classifier in self.classifiers:
            feature.append(classifier.build(instance))
         features.append(feature)
      return map(lambda r: self.inverseClassMap[r], self.learner.predict(features))
   
   def predict(self, example):
      feature = []
      for classifier in self.classifiers:
         feature.append(classifier.build(example))
      classification = self.learner.predict(feature)
      return self.inverseClassMap[classification[0]]
