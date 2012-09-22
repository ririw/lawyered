from Feature import ContinuousFeature
from Data import Data
import nltk


class StringStructure(ContinuousFeature):
   def tag(self, data):
      tokens = nltk.word_tokenize(data)
      tagged = nltk.pos_tag(tokens)
      return nltk.chunk.ne_chunk(tagged)
   def stepSum(self, itemToCountFn, data):
      stepSum = 0
      tagged = self.tag(data.string)
      for w in tagged:
         print w
         if len(w) == 2:
            stepSum += itemToCountFn(w[1])
      return stepSum

class VerbQuantity(StringStructure):
   def build(self, data):
      assert(isinstance(data, Data))
      return self.stepSum(verbSum, data)

def verbSum(v):
   if "VB" in v:
      return 1
   else:
      return 0

