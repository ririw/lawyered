class Feature(object):
   def domain(self):
      """The range of possible values this can take, as either a set
      for discreet features, or a min and max (inclusive) for continuous
      features. Return None if this cannot be know ahead of time. If this
      method is not implemented by extending classes, we assume the domain
      is unknown."""
      return None
   def build(self, data):
      """Generate the feature for some string"""
      pass
   def name(self):
      return self.__class__.__name__
class ContinuousFeature(Feature):
   pass
class DiscreetFeature(Feature):
   pass

