import numpy
import CorruptionModel
import copy
import random
import os
import usaddress

path = os.path.dirname(__file__)+"/"

"""
This model implements a model that simulates corruptions to
US addresses
"""
class AddressCorruptionModel(CorruptionModel.CorruptionModel):
  
  def __init__(self,  
               cols=[], 
               probability=0,
               typoprob=0,
               dbname=path+"data/Address.txt"):

    super(AddressCorruptionModel, self).__init__(cols, 
    	                                      probability)
    if len(cols) > 1:
      raise ValueError("Address Model only allows for single cols: " + str(cols))

    self.typoprob = typoprob

    self.term_alts = [ ['road','rd', 'rd.'], ['ave','avenue', 'ave.'], 
                       ['street','st', 'st.'], ['boulevard', 'blvd', 'blvd.'],
                       ['expressway', 'exp', 'expy', 'exp.'], ['hwy', 'highway', 'hwy.']]
    

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
    print usaddress.parse(x)
    for r in usaddress.parse(x):
      if numpy.random.rand(1,1) > self.typoprob:
        result.append(str(r[0]))
      elif r[1] == 'ZipCode':
        pass
      elif r[1] == 'StreetNamePostType':
        newr = str(r[0])
        for i in self.term_alts:
          if newr.lower() in i:
            newr = random.choice(i)
        result.append(newr)
      else:
        result.append(str(r[0]))

    return ' '.join(result)
