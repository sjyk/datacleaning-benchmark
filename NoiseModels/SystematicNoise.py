"""
This module defines a collection of systematic
statistical noise classes. 
"""

import numpy
import NoiseModel

"""
This model implements Missing Values that
are not at random, i.e., disproportionately
affect high-value features.
"""
class MissingSystematicNoiseModel(NoiseModel.NoiseModel):
  """
  K is the number of features to corrupt
  p is the fraction of the top records to 
  corrupt (within the selected set)
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               k=1,
               p=0.1):

    super(MissingSystematicNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    self.k = k
    self.p = p
  

  def corrupt(self, X):
    hvfeature = self.feature_importance[0]
    means = numpy.mean(X,axis=0)
    Ns = numpy.shape(X)[0]
    ps = numpy.shape(X)[1]
    Y = X

    for i in numpy.argsort(X[:,hvfeature]):
      if numpy.random.rand(1,1) < self.p:
        a = numpy.random.choice(self.feature_importance[0:self.k],1)
        Y[i,a] = means[a]

    return Y


"""
This model implements noise that resembles entity resolution noise
"""
class ERNoiseModel(NoiseModel.NoiseModel):
  """
  Applies ER Noise to a subset of ks features
  p is the error rate
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               ks= [],
               z = 3):

    super(ERNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    self.ks = ks
    self.z = z

  def corrupt(self, X):
    Ns = numpy.shape(X)[0]
    ps = numpy.shape(X)[1]
    for i in range(0, Ns):
      ern = numpy.random.zipf(self.z,(1,1))
      eri = numpy.random.choice(range(0,Ns),ern)
      for j in eri:
      	X[j,self.ks] = X[i,self.ks]
    return X


