#!/usr/bin/python
#
from NoiseModels.RandomNoise import GaussianNoiseModel, ZipfNoiseModel, MissingNoiseModel 
from NoiseModels.SystematicNoise import MissingSystematicNoiseModel
import numpy

z = numpy.random.randn(10,2)
g = MissingSystematicNoiseModel(numpy.shape(z),1.0,[1,0])
print g.apply(z)
