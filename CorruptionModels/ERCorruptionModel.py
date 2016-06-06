import numpy
import CorruptionModel
import copy

"""
This model implements an Entity Resolution Corruption Model
"""
class ERCorruptionModel(CorruptionModel.CorruptionModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self,  
               cols=[], 
               probability=0):

    super(ERCorruptionModel, self).__init__(cols, 
    	                                      probability)

  def corrupt(self, X):
    Y = copy.deepcopy(X)
    for i in range(0, len(Y)):
      Y[i] = self.lookup(Y[i])

    return Y

  def lookup(self, x):
    rtn = []
    for i in range(0, len(x)):
      if i in self.cols:
        rtn.append("test")
      else:
        rtn.append(x[i])
    return rtn
