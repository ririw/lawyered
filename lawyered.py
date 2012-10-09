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
   help='Where to load the classifiers (overrides -t argument) [WARNING: NEVER LOAD UNTRUSTED CLASSIFIERS]')


if __name__ == "__main__":
   args = parser.parse_args()
   pwdstring = sys.argv[0]
   pwd = os.path.join(os.path.split(pwdstring)[:-1])[0]
   if pwd:
      WordTypeQuantities.prefix = pwd + "/"
   features = map(
         lambda c: c(), 
         (LexicalDiversity.featureList + WordTypeQuantities.featureList))

   learners = None
   if args.f:
      # learn from the provided files
      learningData = Data.FilesDataSet(map(file, args.f))
      testSet = Data.DataSet(learningData[:-(len(learningData)/10)])
      trainSet = Data.DataSet(learningData[9*((len(learningData)/10)):])
      for s in trainSet:
         print s
      print "#####"
      for s in testSet:
         print s
      learners = dict(map(
         lambda c: (c[0], c[1](testSet, trainSet, features)),
            Learners.learners.items()))
      for learner in learners.items():
         print learner[0]
         print "\tAccuracy: " + str(learner[1].accuracy)
         print "\tLift: " + str(learner[1].lift*100)
      classificationData = Data.FilesDataSet(map(file, args.t))
   else:
      if args.classifierLoadFile:
         with open(args.classifierLoadFile) as f:
            learners = pickle.load(f)
      else:
         if pwd:
            classifierLoadPath = pwd + \
               "/resources/defualtClassifiers.pickle"
         else:
            classifierLoadPath = "resources/defualtClassifiers.pickle"
         with open(classifierLoadPath) as f:
           learners = pickle.load(f)

   
   if args.files:
      pass
      
   if args.s:
      print learners
      with open(args.s, 'w') as f:
         pickle.dump(learners, f)
