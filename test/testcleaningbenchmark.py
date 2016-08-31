#!/usr/bin/python


import numpy
import sklearn.datasets
from sklearn import svm

from cleaningbenchmark.Utils.Utils import *
from cleaningbenchmark.NoiseModels.RandomNoise import GaussianNoiseModel, ZipfNoiseModel, MissingNoiseModel 
from cleaningbenchmark.NoiseModels.SystematicNoise import MissingSystematicNoiseModel, ERNoiseModel
from cleaningbenchmark.CorruptionModels.AddressCorruptionModel import AddressCorruptionModel
from cleaningbenchmark.CorruptionModels.EscapeCorruptionModel import EscapeCorruptionModel
from cleaningbenchmark.CorruptionModels.ERCorruptionModel import ERCorruptionModel
from cleaningbenchmark.CorruptionModels.CSVCorruptionModel import CSVCorruptionModel
from cleaningbenchmark.CorruptionModels.TypoCorruptionModel import TypoCorruptionModel
from cleaningbenchmark.ModelEval.EvalUtils import generateDirtyTrain

def test1():
  """
  Explicitly call functions to create a noisy version of your training data
  """

  d = sklearn.datasets.load_digits(n_class=2)
  print d['data'], d['target']

  #
  # Create a model that injects zipfian noise, and generate noisy data
  #
  g = ZipfNoiseModel(numpy.shape(d['data']),0.1,[], z=4)
  X_train, X_test, y_train, y_test = generateDirtyTrain(d['data'], d['target'], g,None)


  clf = svm.SVC()
  clf.fit(X_train, y_train)  
  print clf.score(X_test, y_test) 


def test2():
  """
  Use decorator notation to add noise to a function.
  The function must take a numpy-compatible dataset as input, and generate a numpy-compatible dataset as output
  """
  a = [["United States", "a", "b"], ["UC Berkeley", "a"]]
  g = EscapeCorruptionModel([0],0.5)


  # when myETL is called, the data argument will be corrupted using the EscapeCorruptionModel
  @inject(g)
  def myETL(data):
    return data

  print myETL(a)


if __name__ == "__main__":
  test1()
  test2()




