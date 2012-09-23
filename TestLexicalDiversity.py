import unittest
import Data
import random
import LexicalDiversity
import string

class TestLexicalDiversity(unittest.TestCase):
   numTests = 100
   def test_LexicalDiversity(self):
      numUniqueStrings = random.randint(1, TestLexicalDiversity.numTests)
      uniqueStrings = set()
      for i in range(numUniqueStrings):
         uniqueStrings.add(''.join(
         random.choice(string.letters + string.digits) for x in range(numUniqueStrings)
         ))

      numExtraStrings = random.randint(1, TestLexicalDiversity.numTests/10)
      allStrings = []
      for i in range(numExtraStrings):
         allStrings.extend(uniqueStrings)
      random.shuffle(allStrings)
      theString = ' '.join(allStrings)
      l = LexicalDiversity.LexicalDiversity()
      assert((l.build(theString)) == float(len(uniqueStrings))/float(len(uniqueStrings)*numExtraStrings))

if __name__ == "__main__":
   unittest.main()

