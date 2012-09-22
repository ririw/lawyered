from Feature import ContinuousFeature
from Data import Data
import nltk

class SummingScentenceTag(ContinuousFeature):
   def tag(self, data):
      """Break the string in data down into 
      tokens and then tag them with their 
      gramatical type"""
      tokens = nltk.word_tokenize(data)
      tagged = nltk.pos_tag(tokens)
      return nltk.chunk.ne_chunk(tagged)
   def totalBy(self, itemToCountFn, data):
      stepSum = 0
      tagged = self.tag(data.string)
      for w in tagged:
         if len(w) == 2:
            stepSum += itemToCountFn(w[1])
      return stepSum
   def build(self, data):
      assert(isinstance(data, Data))
      return self.totalBy(self.sumFn, data)

class VerbQuantity(SummingScentenceTag):
   def sumFn(self, v):
      if "VB" in v:
         return 1
      else:
         return 0

