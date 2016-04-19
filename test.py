#!/usr/bin/python
#
from NoiseModels.RandomNoise import GaussianNoiseModel, ZipfNoiseModel, MissingNoiseModel 
from NoiseModels.SystematicNoise import MissingSystematicNoiseModel, ERNoiseModel
import numpy

z = numpy.random.randn(10,2)
g = ERNoiseModel(numpy.shape(z),1.0,[1,0], [1])
print g.apply(z)
