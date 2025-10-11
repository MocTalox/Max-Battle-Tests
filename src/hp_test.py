from math import ceil
from functools import reduce

def hp_lcm(limit, hits):
	"""
	Calculates the **LCM** of a list of int numbers `hits`, but with
	the idea that some of the numbers could actually represent a lower
	decimal number (for example: `12.5` been represented by `13`).
	Because of the uncertainty of numbers representation, a list of
	potential result candidates is returned (up to the `limit` value).
	So this is not actually a LCM function, but you get the idea.
	"""
	res = {}
	for hp in xlcm(limit, hits):
		mults = tuple(map(lambda hit : ceil(hp / hit), hits))
		if not any(map(lambda k : _is_mult_tuple(mults, k), res.keys())):
			res.setdefault(mults, []).append(hp)
	return [x for y in res.values() for x in y]

def xlcm(limit, hits):
	"""
	Same idea as `hp_lcm` method, but this one returns all possible
	values, including multiples of other values (which are excluded
	on the other method).
	"""
	mult_filter = lambda hp : all(_is_mult(hp, hit) for hit in hits)
	return list(filter(mult_filter, range(1, limit + 1)))

# If `tar` is a multiple of a number between `src - 1` (exclusive) and `src` (inclusive).
# IOW, if theres is an integer `k` such as: `ceil(tar / k) = src`.
def _is_mult(tar, src):
	k = ceil(tar / src)
	return (src - 1) * k < tar and tar <= src * k

# If tuple `tar` is an exact multiple of tuple `src`.
def _is_mult_tuple(tar, src):
	red = lambda a, b : a if a == b else 0
	div = lambda x : x[0] // x[1]
	return reduce(red, map(div, zip(tar, src))) > 1
