from Data import Data
from Feature import ContinuousFeature
from Util import tokenizeAndLowercase
import string
import nltk


class LexicalDiversity(ContinuousFeature):
   def build(self, data):
      ldata = filter(lambda s: s in string.lowercase or s in string.whitespace, data.string.lower())
      tokens = tokenizeAndLowercase(ldata)
      return float(len(set(tokens)))/float(len(tokens))

featureList = [LexicalDiversity]
