'''
Created on 29/09/2012

@author: Sam Townsend
'''

from Data import Data
from Feature import ContinuousFeature
import string
import nltk

class PronounCheck(ContinuousFeature):
   def build(self, data):
       
      count = 0
      pdata = nltk.word_tokenize(data)
      tagged_data = nltk.pos_tag(pdata)
      
      for (word, tag) in tagged_data:
          if tag.startswith('PRP'):
              count += 1
      return count