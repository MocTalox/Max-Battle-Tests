from math import floor
from py_utils import is_type

def seg(dmg, hits, hp):
	"""
	Converts the damage to segments:
	- `Seg`:   Number of segments.
	- `Extra`: Extra damage done to next segment.
	- `Total`: Total damage.

	The parameters are:
	- `dmg`:  Tuple with the damage for each attack.
	- `hits`: Tuple with number of hits for each attack.
	- `hp`: Total HP value.
	"""
	dmg = (dmg,) if is_type(dmg, int) else dmg
	hits = (hits,) if is_type(hits, int) else hits
	dmg = sum(x * y for x, y in zip(dmg, hits))
	s, xd, td = (floor(dmg / hp), dmg % hp, dmg)
	return "Seg: " + str(s) + " | Extra: " + str(xd) + " dmg | Total: " + str(td) + " dmg"

def mult(res, base, inv = False):
	"""
	Calculates the possible multiplier values needed to produce the
	resulting damage `res`, by being multiplied to a base damage `base`.
	The value `res` can be a single value or a range of values.
	IOW, multiplier values `k` which fulfill:
	- `floor(base * k) + 1 = res` (single dmg value)
	- `res_min <= floor(base * k) + 1 <= res_max` (range of dmg values)
	"""
	return _mult_aux(res, res, base, inv) if is_type(res, int) else _mult_aux(res[0], res[1], base, inv)

# Range of values which fulfill: `res_min <= floor(base * mult) + 1 <= res_max`
def _mult_aux(res_min, res_max, base, inv = False):
	return (base / res_max, base / (res_min - 1)) if inv else ((res_min - 1) / base, res_max / base)
