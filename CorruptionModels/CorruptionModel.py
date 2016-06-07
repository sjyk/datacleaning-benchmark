"""
This class defines the basic structure for a CorruptionModel
object. A corruption model object differs from the NoiseModel
classes as it focuses on relational corruptions of base data
rather than feature value corruption
"""
import numpy as np
import random
import copy

class CorruptionModel(object):

  """
  Creates a CorruptionModel object.

  Data comes in as a list of lists of strings
  Output is a corrupted list of list of strings

  cols is a list of ints
  probability is the corruption rate
  """
  def __init__(self, 
               cols=[], 
               probability=0):
    
    self.cols = cols
    self.probability = probability

    """
    Argument error checks
    """
    #check to see if the shape provided is valid
    if len(cols) == 0:
       raise ValueError("Invalid cols: " + str(cols))

    #check to see if the probability is valid
    if probability < 0 or probability > 1:
      raise ValueError("Invalid probability: " + str(probability))


  """
  The apply function applies the corruption model to some 
  subset of the data.

  Data comes in as a list of lists of strings
  """
  def apply(self, X):
    clean = []
    dirty =[]

    for i in range(0, len(X)):
      if np.random.rand(1,1) >= self.probability:
        clean.append(X[i])
      else:
        dirty.append(X[i])

    result = self.corrupt(dirty)
    result.extend(clean)

    old = dirty
    old.extend(clean)

    return (result, old) 

  """
  This method should be implemented by sub-classes
  """
  def corrupt(self, X):
  	raise NotImplementedError("Please implement this method")



