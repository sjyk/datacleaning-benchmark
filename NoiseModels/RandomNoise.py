"""
This module defines a collection of random
noise modules--that is they do not use the
features.
"""
import numpy
import NoiseModel

"""
This model implements Gaussian Noise
"""
class GaussianNoiseModel(NoiseModel.NoiseModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               mu=0,
           sigma=1):

    super(GaussianNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    self.mu = mu
    self.sigma = sigma
  

  def corrupt(self, X):
  	Ns = numpy.shape(X)[0]
  	ps = numpy.shape(X)[1]
  	Z = numpy.random.randn(Ns,ps)*self.sigma + self.mu
  	return X + Z


"""
This model implements Laplace Noise
"""
class LaplaceNoiseModel(NoiseModel.NoiseModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               mu=0,
               b=1):

    super(LaplaceNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    self.mu = mu
    self.b = b
  

  def corrupt(self, X):
  	Ns = numpy.shape(X)[0]
  	ps = numpy.shape(X)[1]
  	Z = numpy.random.laplace(self.mu, self.b, (Ns,ps))
  	return X + Z


"""
Zipfian Noise, simulates high-magnitude outliers
"""
class ZipfNoiseModel(NoiseModel.NoiseModel):
  
  """
  z is the Zipfian Scale Parameter
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               z=3):

    super(ZipfNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    self.z = z
  

  def corrupt(self, X):
  	Ns = numpy.shape(X)[0]
  	ps = numpy.shape(X)[1]
  	Z = numpy.random.zipf(self.z, (Ns,ps))
  	return X + Z


"""
Simulates Random Missing Data With a Placeholder Value
Picks an attr at random and sets the value to be missing
"""
class MissingNoiseModel(NoiseModel.NoiseModel):
  
  """
  ph is the Placeholder value that missing attrs are set to.
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               ph=-1):

    super(MissingNoiseModel, self).__init__(shape, 
    	                             probability, 
    	                             feature_importance)
    self.ph = ph
  

  def corrupt(self, X):
  	Ns = numpy.shape(X)[0]
  	ps = numpy.shape(X)[1]
  	Y = numpy.copy(X)
  	for i in range(0, Ns):
  		a = numpy.random.choice(ps,1)
  		Y[i,a] = self.ph
  	return Y


