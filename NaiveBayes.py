class NaiveBayes(object):
   def __init__(self, testSet, trainSet, classifiers):
      assert(isInstance(testSet, DataSet))
      assert(isInstance(trainSet, DataSet))
      assert(isInstance(classifiers, list))
      testFeatures = []
      trainFeatures = []
      for instance in testSet:
         testFeature = []
         for classifier in classifiers:
            testFeature.append(classifier.build(instance))
         testFeatures.append((testFeature, str(instance.isTrue)))
      for instance in trainSet:
         trainFeature = []
         for classifier in classifiers:
            trainFeature.append(classifier.build(instance))
         trainFeatures.append((trainFeature, str(instance.isTrue)))


   def classify(self, instance):

