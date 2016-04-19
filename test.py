#!/usr/bin/python
#
from NoiseModels.RandomNoise import GaussianNoiseModel, ZipfNoiseModel, MissingNoiseModel 
from NoiseModels.SystematicNoise import MissingSystematicNoiseModel, ERNoiseModel
import numpy
import sklearn.datasets
from sklearn import svm
from ModelEval.EvalUtils import generateDirtyTrain

d = sklearn.datasets.load_digits(n_class=2)
print d['data'], d['target']

g = ZipfNoiseModel(numpy.shape(d['data']),0.1,[], z=4)
X_train, X_test, y_train, y_test = generateDirtyTrain(d['data'], d['target'], g,None)
clf = svm.SVC()
clf.fit(X_train, y_train)  
print clf.score(X_test, y_test) 


