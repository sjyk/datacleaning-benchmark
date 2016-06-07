import numpy
import CorruptionModel
import copy
import os
import pickle
import random

path = os.path.dirname(__file__)+"/"

"""
This model implements an Entity Resolution Corruption Model
"""
class ERCorruptionModel(CorruptionModel.CorruptionModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self,  
               cols=[], 
               probability=0,
               dbname=path+"data/wiki_er_lookup.p"):

    super(ERCorruptionModel, self).__init__(cols, 
    	                                      probability)

    self.lookup_index = pickle.load(open(dbname,'rb'))

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
        if x[i].lower() in self.lookup_index:
          rtn.append(random.choice(self.lookup_index[x[i].lower()]))
      else:
        rtn.append(x[i])
    return rtn
