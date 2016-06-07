import numpy
import CorruptionModel
import copy
import os
import pickle
import random
import urllib

#path = os.path.dirname(__file__)+"/"

"""
This model implements a corruption model that simulates 
html escape parsing errors
"""
class EscapeCorruptionModel(CorruptionModel.CorruptionModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self,  
               cols=[], 
               probability=0):

    super(EscapeCorruptionModel, self).__init__(cols, 
    	                                      probability)

    #self.lookup_index = pickle.load(open(dbname,'rb'))

    #print self.lookup_index 

  def corrupt(self, X):
    Y = copy.deepcopy(X)
    for i in range(0, len(Y)):
      Y[i] = self.lookup(Y[i])

    return Y

  def lookup(self, x):
    rtn = []
    for i in range(0, len(x)):
      if i in self.cols:
        rtn.append(urllib.quote_plus(x[i]))
      else:
        rtn.append(x[i])
    
    return rtn
