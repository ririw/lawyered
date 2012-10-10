import unittest
import WordTypeQuantities
from Data import Data

class TestGeneralizingTermsCheck(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.GeneralizingTermsCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)

    def test_words(self):
        v = WordTypeQuantities.GeneralizingTermsCheck()      
        cases = {"""Was anybody else there? asked Mr. Pumblechook.""": 1, 
                 """Yes, said I. Estella waved a blue flag, and I waved a red one, and Miss Havisham waved one sprinkled all over with little gold stars, out at the coach-window. And then we all waved our swords and hurrahed.""": 2}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)

class TestThirdPersonPronoun(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.ModifierCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)

    def test_words(self):
        v = WordTypeQuantities.ThirdPersonPronoun()
        cases = {"""Joe, who had ventured into the kitchen after me as the dustpan had retired before us, drew the back of his hand across his nose with a conciliatory air, when Mrs. Joe darted a look at him, and, when her eyes were withdrawn, secretly crossed his two forefingers, and exhibited them to me, as our token that Mrs. Joe was in a cross temper. This was so much her normal state, that Joe and I would often, for weeks together, be, as to our fingers, like monumental Crusaders as to their legs.""": 4, 
                 """No; I should not have minded that, if they would only have left me alone. But they wouldn't leave me alone.""": 2,
                 """Biddy looked down at her child, and put its little hand to her lips, and then put the good matronly hand with which she had touched it into mine.""": 4}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)

class TestFirstPersonPluralPronoun(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.ModifierCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)

    def test_words(self):
        v = WordTypeQuantities.FirstPersonPluralPronoun()
        cases = {"""My sister was not in a very bad temper when we presented ourselves in the kitchen, and Joe was encouraged by that unusual circumstance to tell her about the bright shilling. A bad un, I'll be bound, said Mrs. Joe triumphantly, or he wouldn't have given it to the boy! Let's look at it.""": 2, 
                 """As we were going with our candle along the dark passage, Estella stopped all of a sudden, and, facing round, said in her taunting manner, with her face quite close to mine""": 2,
                 """Us two being now alone, sir,began Joe.""": 1}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)

class TestFirstPersonSingularPronoun(unittest.TestCase):
    def test_empty(self):
        v = WordTypeQuantities.ModifierCheck()
        d = Data("", True)
        assert(v.build(d) == 0)
        d = Data("", False)
        assert(v.build(d) == 0)

    def test_words(self):
        v = WordTypeQuantities.FirstPersonSingularPronoun()
        cases = {"""So, I called myself Pip, and came to be called Pip.""": 2, 
                 """After darkly looking at his leg and me several times, he came closer to my tombstone, took me by both arms, and tilted me back as far as he could hold me; so that his eyes looked most powerfully down into mine, and mine looked most helplessly up into his.""": 7}
        for (words, count) in cases.items():
            d = Data(words, True)
            assert(v.build(d) == count)
            d = Data(words, False)
            assert(v.build(d) == count)
			
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
