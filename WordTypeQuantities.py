from Feature import ContinuousFeature
from Data import Data
import nltk
import string

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
            stepSum += itemToCountFn(w)
      return stepSum
   def build(self, data):
      assert(isinstance(data, Data))
      return self.totalBy(self.sumFn, data)

class VerbQuantity(SummingScentenceTag):
   def sumFn(self, v):
      if "VB" in v[1]:
         return 1
      else:
         return 0

class ModifierCheck(SummingScentenceTag):
    def sumFn(self,v):
        tags = {"JJ","JJR","JJS","JJT","NR","RB","RBR","RBT","RN","RP","WRB"}
        if v[1] in tags:
            return 1
        else:
            return 0

class WordQuantity(SummingScentenceTag):
    def sumFn(self,v):
        if v[0] in string.punctuation:
            return 0    
        else:
            return 1

class CausationCheck(SummingScentenceTag):
    def sumFn(self, v):
        f = open('Causation.txt')
        causationWords = f.read().split('\n')
        if v[0].lower() in causationWords:
            return 1
        else:
            return 0

class TentativeCheck(SummingScentenceTag):
    def sumFn(self, v):
        f = open('Tentative.txt')
        tentativeWords = f.read().split('\n')
        if v[0].lower() in tentativeWords:
            return 1
        else:
            return 0
            
class 1stPersonSingularPro(SummingScentenceTag):
    def sumFn(self, v):
        f = open('1stPersonSingularPronouns.txt')
        1stsingularpro = f.read().split('\n')
        if v[0].lower() in 1stsingularpro:
            return 1
        else:
            return 0
