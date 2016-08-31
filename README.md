# What is this?

This is a set of python decorators that inject a wide range of noise into your machine learning pipelines.

See `test/testcleaningbenchmark.py` for example code.  

# Installation 

Install

        pip install cleaningbenchmark

        # or
  
        python setup.py install

Test it

        python test/testcleaningbenchmark.py


# Documentation

Documentation coming soon.

## Usage

        # create noise model 
        g = EscapeCorruptionModel([0], 0.5)  

        # augment pipeline_operation to inject escape corruption noise to its first argument
        @inject(g)
        def pipeline_operation(data, args):
          return data

## List of Noise Models

TBA

