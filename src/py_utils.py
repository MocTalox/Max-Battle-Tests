from functools import reduce
from struct import pack, unpack

def is_type(x, *types):
	return any(map(lambda t : type(x) == t, types))

def spf(x):
	"""
	Truncates value to single precision float. Recursive with lists of values.
	"""
	if is_type(x, float):
		return unpack('f', pack('f', x))[0]
	return x if is_type(x, int) else type(x)(map(spf, x))

def prod(x):
	"""
	Product of all values, or itself if its a single value.
	"""
	return x if is_type(x, int, float) else reduce(lambda a, b : a * b, x)
