from math import floor

def is_number(x):
	"""
	Checks if a value `x` is a real number (`int` or `float`).
	"""
	return type(x) == int or type(x) == float


def seg_calc(dmg, hp):
	"""
	Converts the damage to segments:
	- First:  Number of segments.
	- Second: Extra damage done to next segment.
	- Third:  Total damage (same as input `dmg`).
	"""
	return (floor(dmg / hp), dmg % hp, dmg)

def seg_str(s, xd, td):
	"""
	Converts `seg_calc` result to readable string.
	"""
	return "Seg: " + str(s) + " | Extra: " + str(xd) + " dmg | Total: " + str(td) + " dmg\n"

def seg_print(dmg, hp):
	"""
	Prints `seg_str` result to output file.
	"""
	return print(seg_str(*seg_calc(dmg, hp)))

def mult(res, base, inv = False):
	"""
	Calculates the possible multiplier values needed to produce the
	resulting damage `res`, by being multiplied to a base damage `base`.
	The value `res` can be a single value or a range of values.
	IOW, multiplier values `k` which fulfill:
	- `floor(base * k) + 1 = res` (single dmg value)
	- `res_min <= floor(base * k) + 1 <= res_max` (range of dmg values)
	"""
	return _mult_aux(res, res, base, inv) if is_number(res) else _mult_aux(res[0], res[1], base, inv)

# Range of values which fulfill: `res_min <= floor(base * mult) + 1 <= res_max`
def _mult_aux(res_min, res_max, base, inv = False):
	return (base / res_max, base / (res_min - 1)) if inv else ((res_min - 1) / base, res_max / base)
