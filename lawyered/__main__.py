import argparse
import LexicalDiversity
import WordTypeQuantities
import Learners
import Data
import sys
import os.path
import pickle

parser = argparse.ArgumentParser(
      description="Run lie detection on some files")
parser.add_argument(
   'files',
   metavar='fileList',
   type=str,
   nargs='*',
   help='the list of files with statements to classify')
parser.add_argument(
   '-t',
   metavar='trainFiles',
   type=str,
   nargs='+',
   help='A list of files upon which to train classifiers')
parser.add_argument(
   '-f',
   metavar='fileList',
   type=str,
   nargs='+',
   help='the list of files with statements to classify')
parser.add_argument(
   '-s',
   metavar='classifierSaveFile',
   type=str,
   help='Where to save the produced classifiers')
parser.add_argument(
   '-l',
   metavar='classifierLoadFile',
   type=str,
   help='Where to load the classifiers (overrides -t argument)\n [WARNING: NEVER LOAD UNTRUSTED CLASSIFIERS]')
parser.add_argument(
   '-c',
   metavar='learningAlgorithm',
   type=str,
   help='Select the type of learning algorithm {NaiveBayes, RandomForest, ClassificationTree}')


if __name__ == "__main__":
   args = parser.parse_args()
   pwdstring = ""
   pwd = os.path.join(os.path.split(pwdstring)[:-1])[0]
   if pwd:
      WordTypeQuantities.prefix = pwd + "/"
   features = map(
         lambda c: c(),
         (LexicalDiversity.featureList + WordTypeQuantities.featureList))

   learners = None
   if args.c:
      # default classifier is RandomForest
      classifier = args.c
   else:
      classifier = 'RandomForest'

   if args.t:
      # learn from the provided files
      learningData = Data.FilesDataSet(map(file, args.t))
      testSet = Data.DataSet(learningData[:8*(len(learningData)/10)])
      trainSet = Data.DataSet(learningData[8*((len(learningData)/10)):])
      #for s in trainSet:
         #print s
      #print "#####"
      #for s in testSet:
         #print s
      learners = dict(map(
         lambda c: (c[0], c[1](testSet, trainSet, features)),
            Learners.learners.items()))
      #import debug
      learner = Learners.learners[classifier](testSet, trainSet, features)
      print "\tAccuracy: " + str(learner.accuracy)
      print "\tLift: " + str(learner.lift*100)
   else:
      if args.l:
         with open(args.l) as f:
            learners = pickle.load(f)
      else:
         if pwd:
            classifierLoadPath = pwd + \
               "/resources/defaultClassifiers.pickle"
         else:
            classifierLoadPath = "resources/defaultClassifiers.pickle"
         with open(classifierLoadPath) as f:
            learners = pickle.load(f)
      learner = Learners.learners[classifier]


   if args.f:
      print "\nClassifying using file: ", args.f
      # Assuming we are using the entire test set
      # from a previously loaded model(s) in "learners"
      testData = Data.FilesDataSet(map(file, args.f))
      learner = learners[classifier]
      for example in testData:
          print example.string
          classification = learner.predict(example)
          print classification

   if args.s:
      print learners
      with open(args.s, 'w') as f:
         pickle.dump(learners, f)
