from Feature import ContinuousFeature
from Data import Data
import nltk
import string

prefix = ""

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
      
class FileReader(SummingScentenceTag):
   def __init__(self, filename):
      super(FileReader, self).__init__()
      f = open(filename)
      self.testSet = set(f.read().split('\n'))
      f.close()
   def sumFn(self, v):
      if v[0].lower() in self.testSet:
         return 1
      else:
         return 0

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

class CausationCheck(FileReader):
	def __init__(self):
		super(CausationCheck, self).__init__(prefix + 'resources/Causation.txt')

class TentativeCheck(FileReader):
	def __init__(self):
		super(TentativeCheck, self).__init__(prefix + 'resources/Tentative.txt')
            
class FirstPersonSingularPronoun(FileReader):
	def __init__(self):
		super(FirstPersonSingularPronoun, self).__init__(prefix + 'resources/1stPersonSingularPronouns.txt')

class FirstPersonPluralPronoun(FileReader):
	def __init__(self):
		super(FirstPersonPluralPronoun, self).__init__(prefix + 'resources/1stPersonPronouns.txt')

class ThirdPersonPronoun(FileReader):
	def __init__(self):
		super(ThirdPersonPronoun, self).__init__(prefix + 'resources/3rdPersonPronouns.txt')
		
class SensoryRatioCheck(FileReader):
	def __init__(self):
		super(SensoryRatioCheck, self).__init__(prefix + 'resources/Sensory.txt')
		
class MotionTermsCheck(FileReader):
	def __init__(self):
		super(MotionTermsCheck, self).__init__(prefix + 'resources/MotionTerms.txt')
	            
class GeneralizingTermsCheck(FileReader):
   def __init__(self):
   	super(GeneralizingTermsCheck, self).__init__(prefix + 'resources/GeneralizingTerms.txt')

featureList = [
      VerbQuantity,
      ModifierCheck,
      WordQuantity,
      CausationCheck,
      TentativeCheck,
      FirstPersonSingularPronoun,
      FirstPersonPluralPronoun,
      ThirdPersonPronoun,
      SensoryRatioCheck,
      MotionTermsCheck,
      GeneralizingTermsCheck
   ]  



