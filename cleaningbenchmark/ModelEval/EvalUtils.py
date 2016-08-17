"""
This module provides utilities for evaluating
models after corruption
"""

from sklearn.cross_validation import train_test_split
import numpy as np

def generateDirtyTrain(X,
	                   y,
	                   noisemodelX=None, 
	                   noisemodely=None, 
	                   test_size=0.2):

  X_train, X_test, y_train, y_test = train_test_split(X, 
  	                                                  y, 
  	                                                  test_size=test_size)
  if noisemodelX != None:
  	nmx = noisemodelX.reshape(np.shape(X_train))
  	X_train = nmx.apply(X_train)[0]

  if noisemodely != None:
  	nmx = noisemodely.reshape(np.shape(y_train))
  	y_train = nmx.apply(y_train)[0]

  return X_train, X_test, y_train, y_test

