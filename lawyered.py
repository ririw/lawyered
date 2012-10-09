import argparse
import LexicalDiversity
import WordTypeQuantities 
import Data
import sys
import os.path

parser = argparse.ArgumentParser(
      description="Run lie detection on some files")
parser.add_argument(
   'files',
   metavar='fileList', 
   type=str,
   nargs='*',
   help='the list of files with statements to classify')
parser.add_argument(
   '--tf',
   metavar='trainFiles', 
   type=str,
   nargs='+',
   help='A list of files upon which to train classifiers')
parser.add_argument(
   '--f',
   metavar='fileList', 
   type=str,
   nargs='+',
   help='the list of files with statements to classify')


if __name__ == "__main__":
   args = parser.parse_args()
   pwdstring = sys.argv[0]
   pwd = os.path.join(os.path.split(pwdstring)[:-1])[0]
   WordTypeQuantities.prefix = pwd
   features = map(lambda c: c(), (LexicalDiversity.featureList + WordTypeQuantities.featureList))

   if args.files:
      data = Data.FilesDataSet(map(file, args.files))
      print data
   
