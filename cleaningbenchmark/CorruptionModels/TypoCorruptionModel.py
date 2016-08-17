import numpy
import CorruptionModel
import copy
import random
import os

path = os.path.dirname(__file__)+"/"

"""
This model implements a model that simulates Typos in a document
"""
class TypoCorruptionModel(CorruptionModel.CorruptionModel):
  
  """
  Mu and Sigma are Params
  """
  def __init__(self,  
               cols=[], 
               probability=0,
               typoprob=0,
               dbname=path+"data/Typos.txt"):

    super(TypoCorruptionModel, self).__init__(cols, 
    	                                      probability)
    self.lookup_index = {}
    self.typoprob = typoprob
    f = open(dbname, "rb+")
    line = f.readline()

    while line != "":
      comps = line.strip().split()
      if comps[1] not in self.lookup_index:
        self.lookup_index[comps[1]] = []
      self.lookup_index[comps[1]].append(comps[0])
      line = f.readline()

  def corrupt(self, X):
    Y = copy.deepcopy(X)
    for i in range(0, len(Y)):
      Y[i] = self.lookup(Y[i])

    return Y

  def lookup(self, x):
    rtn = []
    for i in range(0, len(x)):
      if i in self.cols:
        rtn.append(self.typoCol(x[i]))
      else:
        rtn.append(x[i])
    return rtn

#fix cases
  def typoCol(self, x):
    result = []
    for word in x.split():
      if numpy.random.rand(1,1) > self.typoprob: 
        result.append(word)
      elif word.lower() in self.lookup_index:
        typo = random.choice(self.lookup_index[word.lower()])
        result.append(typo)
      #if not in skip
    return ' '.join(result)
