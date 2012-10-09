import unittest
import WordTypeQuantities
from Data import Data

class TestModifierCheck(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.ModifierCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)

    def test_words(self):
        v = WordTypeQuantities.ModifierCheck()
        cases = {"""I was nervous because I had never been in a strip club before, it was like entering a building where people danced on poles for money; it was exactly that type of place.""": 4, 
                 """Perhaps there are aliens on Mars, we will only truly know when we ask.""": 4,
                 """Things that seem bad always maybe appear to be worse""": 3}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)
        

class TestWordQuantity(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.WordQuantity()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)
    
    def test_words(self):
        v = WordTypeQuantities.WordQuantity()
        cases = {"""I was nervous because I had never been in a strip club before, it was like entering a building where people danced on poles for money; it was exactly that type of place.""": 33, 
                 """Perhaps there are aliens on Mars, we will only truly know when we ask.""": 14,
                 """Things that seem bad always maybe appear to be worse""": 10}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)
       

class TestTentativeCheck(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.TentativeCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)
        
    def test_with_words(self):
        v = WordTypeQuantities.TentativeCheck()
        cases = {"""I was nervous because I had never been in  a strip club before, it was like entering a building where people danced on poles for money; it was exactly that type of place.""": 0, 
                 """Perhaps there are aliens on Mars, we will only truly know when we ask.""": 1,
                 """Things that seem bad always maybe appear to be worse""": 3}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)


class TestCausationQuantity(unittest.TestCase):
    def non_test_empty(self):
        v = WordTypeQuantities.CausationCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)

    def non_test_causation(self):
        v = WordTypeQuantities.CausationCheck()
        cases = {"""I am not sorry because   I was merely repeating.""": 1, 
                 """There are three effects in effects in effects puppies. """: 3,
                 """The effect of because me turtle.""": 2}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)


class TestVerbQuantity(unittest.TestCase):
   def test_empty(self):
      v = WordTypeQuantities.VerbQuantity()
      d = Data("", True)
      assert(v.build(d) == 0)
      d = Data("", False)
      assert(v.build(d) == 0)
   def test_words(self):
      v = WordTypeQuantities.VerbQuantity()
      cases = {
            """
         Call me Ishmael. Some years ago never mind how long precisely having
         little or no money in my purse, and nothing particular to interest me on
         shore, I thought I would sail about a little and see the watery part of
         the world. It is a way I have of driving off the spleen and regulating
         the circulation. Whenever I find myself growing grim about the mouth;
         whenever it is a damp, drizzly November in my soul; whenever I find
         myself involuntarily pausing before coffin warehouses, and bringing up
         the rear of every funeral I meet; and especially whenever my hypos get
         such an upper hand of me, that it requires a strong moral principle to
         prevent me from deliberately stepping into the street, and methodically
         knocking people's hats off then, I account it high time to get to sea
         as soon as I can. This is my substitute for pistol and ball. With a
         philosophical flourish Cato throws himself upon his sword; I quietly
         take to the ship. There is nothing surprising in this. If they but knew
         it, almost all men in their degree, some time or other, cherish very
         nearly the same feelings towards the ocean with me.""": 30,
         """There now is your insular city of the Manhattoes, belted round by
         wharves as Indian isles by coral reefs commerce surrounds it with
         her surf. Right and left, the streets take you waterward. Its extreme
         downtown is the battery, where that noble mole is washed by waves, and
         cooled by breezes, which a few hours previous were out of sight of land.
         Look at the crowds of water-gazers there.""": 9

            }
      for (words, count) in cases.items():
         d = Data(words, True)
         assert(v.build(d) == count)
         d = Data(words, False)
         assert(v.build(d) == count)

if __name__ == "__main__":
   unittest.main()
