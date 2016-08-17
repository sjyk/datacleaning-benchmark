#!/usr/bin/env python2.7
try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
from setuptools import setup, find_packages

setup(name="cleaningbenchmark",

      # semantic versioning is a simple way to define versions
      # http://semver.org/
      version="0.0.1",

      description="",
      license="MIT",
      author="Sanjay Krishnan",
      author_email="",
      url="https://github.com/sjyk/datacleaning-benchmark",
      packages = find_packages(),
      include_package_data = True,

      # ensures that pipexample is defined as a module
      package_dir = {'cleaningbenchmark' : 'cleaningbenchmark'},

      # ensures that pipexample/*.txt is included in the package
      package_data={
        #'datasets':['*.txt']
      },

      # ensures that runexample.py can be run from the command line as a program
      scripts = [
        'test/testcleaningbenchmark.py'
      ],
      install_requires = [
        'click', 'scikit-learn', 'numpy', 'usaddress'
      ],
      keywords= "")
