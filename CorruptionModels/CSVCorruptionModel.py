import numpy
import CorruptionModel
import copy
import os
import pickle
import random

#path = os.path.dirname(__file__)+"/"

"""
This model implements a corruption model that simulates 
CSV parsing errors
"""
class CSVCorruptionModel(CorruptionModel.CorruptionModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self,  
               cols=[], 
               probability=0):

    super(CSVCorruptionModel, self).__init__(cols, 
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
        pass
      else:
        rtn.append(x[i])

    for i in range(len(rtn), len(x)):
        rtn.append("")
    
    return rtn
