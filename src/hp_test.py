from math import ceil

def hp_lcm(limit, hits):
	res = {}
	for hp in lcm_x(limit, hits):
		mults = tuple(map(lambda hit : ceil(hp / hit), hits))
		if not any(map(lambda k : _is_mult_tuple(mults, k), res.keys())):
			res.setdefault(mults, []).append(hp)
	return [x for y in res.values() for x in y]

def _is_mult_tuple(tar, src):
	k = round(tar[0] / src[0])
	mult_ind = lambda i, k : src[i] * k == tar[i]
	mult_all = lambda n, k : all(map(lambda i : mult_ind(i, k), range(n)))
	return any(map(lambda k : mult_all(len(tar), k), range(2, k + 1)))

def lcm_x(limit, hits):
	"""
	Calculates the **LCM** of a list of int numbers `hits`, but with
	the idea that some of the numbers could actually represent a lower
	decimal number (for example: `12.5` been represented by `13`).
	Because of the uncertainty of numbers representation, a list of
	potential result candidates is returned (up to the `limit` value).
	So this is not actually a LCM function, but you get the idea.
	"""
	mult_filter = lambda hp : all(_is_mult_x(hp, hit) for hit in hits)
	return list(filter(mult_filter, range(1, limit + 1)))

def _is_mult_x(tar, src):
	"""
	If `tar` is a multiple of a number between `src - 1` (exclusive)
	and `src` (inclusive).
	IOW, if theres is an integer `k` such as: `ceil(tar / k) = src`.
	"""
	k = ceil(tar / src)
	return (src - 1) * k < tar and tar <= src * k
