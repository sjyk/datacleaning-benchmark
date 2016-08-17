"""
This library includes noise injection
decorators and other utils that you can
use.
"""
import numpy as np

#This gives you a decorator that you can use to corrupt data
def inject(model, gt=False):
	def decorator(func):
		def function_helper(*args, **kwargs):
			clean = func(*args, **kwargs)
			if gt:
				return clean
			else:
				return model.apply(clean)[0]

		return function_helper

	return decorator


#collects and prints statistics about the
#dirty data
def collect_statistics(data, model, udf, metric, trials=10):
	trials_data = np.zeros((trials,1))
	for i in range(0, trials):
		res = model.apply(data)
		dirty = res[0]
		clean = res[1]
		trials_data[i,1] = metric(udf(dirty), udf(clean))
	print "T=", trials, "runs:", np.mean(trials_data)
	return trials_data
