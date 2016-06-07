"""
This library includes noise injection
decorators and other utils that you can
use.
"""

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