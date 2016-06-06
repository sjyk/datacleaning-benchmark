# datacleaning-benchmark

Requires
*numpy
*usaddress

Datasets we have

* police union contributions
* stock market dataset from Luna
* Jun Yang's politican voting data
* movies dataset
* propublica

What's missing

* Noise models, model eval
* Base Data representation and how to corrupt it


Noise

* Constraint based noise
  * Start with simple functional dependency constraints
  * white does an input file of constraints look like
  * given a constraint how to generate errors
  * gvine a set of constraints, how to generate errors
* Constraint based noise + synthetic noise
* Graph of celaning opertations and applying subpaths in tnhe graph
* Samples of ground truth

What to evaluate

* Constraint based stuff
* Chris Re's stuff
* Active clean
* Normal models


How to use our benchmark in existing data cleaning system/exepreiment setups

* walk through

Benchmarks to look at

* OLTPBench
* LinearRoad
* Ask Mike


Wu:

* does test.py api look sane 