"""
This class defines the basic structure for a NoiseModel
object. A noise model object takes in a numpy matrix and
outputs another numpy matrix with the same shape.
"""
import numpy as np
import random
import copy

class NoiseModel(object):

  """
  Creates a NoiseModel object.

  shape defines the shape of the input matrix N x p
  
  probability defines the probability that a 
  row in the input matrix is transformed

  feature_importance is a sorted sequence of 
  features of decreasing importance
  """
  def __init__(self,
               shape=(1,1), 
               probability=0,
               feature_importance=[]):
    
    self.shape = shape
    self.probability = probability

    if feature_importance == []:
      self.feature_importance = range(0,shape[1])
    else:
      self.feature_importance = feature_importance

    """
    Argument error checks
    """

    #check to see if the shape provided is valid
    if len(shape) != 2 or \
       shape[0] <= 0 or \
       shape[1] <= 0:
       raise ValueError("Invalid shape: " + str(shape))
  
    #check to see if the probability is valid
    if probability < 0 or probability > 1:
    	raise ValueError("Invalid probability: " + str(probability))

    if sorted(self.feature_importance) != range(0,shape[1]):
    	raise ValueError("Invalid feature_importance: " + str(self.feature_importance))

  """
  The apply function applies the noise model to some 
  subset of the data and performs the necessary error
  checks to make sure sizes are preserved.
  """
  def apply(self, X):
    xshape = np.shape(X)

    if xshape != self.shape:
    	raise ValueError("The input does not match the shape of the Noise Model")

    #sample from data
    N = self.shape[0]
    Ns = int(round(N*self.probability))
    all_indices = range(0,N)
    random.shuffle(all_indices)
    tocorrupt = all_indices[0:Ns]
    self.argselect = tocorrupt
    clean = all_indices[Ns:]
    
    return (np.vstack((self.corrupt(X[tocorrupt,:]), X[clean,:])), np.vstack((X[tocorrupt,:], X[clean,:])))

  """
  This method should be implemented by sub-classes
  """
  def corrupt(self, X):
  	raise NotImplementedError("Please implement this method")

  """
  This method allows for dynamic reshaping of the noise model
  """
  def reshape(self, shape, feature_importance=[]):
    ret = copy.deepcopy(self)
    ret.shape = shape
    if feature_importance == []:
      ret.feature_importance = range(0,shape[1])
    else:
      ret.feature_importance = feature_importance

    #check to see if the shape provided is valid
    if len(shape) != 2 or \
       shape[0] <= 0 or \
       shape[1] <= 0:
       raise ValueError("Invalid shape: " + str(shape))

    if sorted(ret.feature_importance) != range(0,shape[1]):
    	raise ValueError("Invalid feature_importance: " + str(ret.feature_importance))
    return ret






