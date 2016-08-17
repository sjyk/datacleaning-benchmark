"""
This module defines a collection of
constraint based errors
"""

import numpy
import NoiseModel


class RowConstraint(object):
  def __init__(self, name):
    self.name = name

  def corrupt(self, row):
    """
    This function should be overwritten
    """
    return row

class FDRowConstraint(object):
  def __init__(self, indep_cols, dep_col):
    """
    indep_cols is the list of cols on the left side of the functional dep
    dep_col is the right side of the functional dep
    """
    self.indep_cols = indep_cols
    self.dep_cols = dep_cols



class FDNoiseModel(NoiseModel.NoiseModel):
  """
  fd is the list of functional dependencies
  """
  def __init__(self, 
               shape, 
               probability=0,
               feature_importance=[],
               fds=[]):

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


