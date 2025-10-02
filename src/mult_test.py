from math import floor, ceil
from functools import reduce
from struct import pack, unpack

# Truncates value to float precision
# Recursive with lists of values
def _to_float(x):
	if type(x) == int:
		return x
	if type(x) == float:
		return unpack('f', pack('f', x))[0]
	return list(map(_to_float, x))

# Calculates output damage
def _dmg(atk_stats, def_stats, bonus, extra_bonus):
	attack = (atk_stats[1] + atk_stats[2]) * atk_stats[3]
	defense = (def_stats[1] + 15) * def_stats[2]
	raw = 0.5 * atk_stats[0] * attack / defense * atk_stats[4] * atk_stats[5] * atk_stats[6] * bonus
	return floor(raw * extra_bonus) + 1

# Calculates HP and remaining segments sequence
def _hp_seq(total_hp, atks):
	hp = total_hp
	res = [(hp, 100)]
	for atk in atks:
		hp = hp - atk
		res.append((hp, ceil(100 * hp / total_hp)))
	return res

# Product of all bonuses, or itself if its a single value
def _prod_bonus(x):
	if type(x) == int or type(x) == float:
		return x
	return reduce(lambda a, b : a * b, x)

def main(atk_stats, def_stats, bonus, atk_seq, seg_seq, start, end, step, inv = False):
	"""
	Calculates an additional bonus value for a test (within the `start`-`end`-`step` range).
	If `seg_seq` is informed, obtains the range of bonus values that satisfies that sequence.
	Else (`seg_seq` is `None`), obtains all segment sequence for the range of bonus values.
	If `inv` is `True`, the bonus will be calculated inverted (useful for defense bonuses).
	- `atk_stats`: List of lists with [`power`, `base_atk`, `iv_atk`,
	`atk_cpm`, `stab`, `type`, `weather`], one per each attack type.
	- `def_stats`: List with [`total_hp`, `base_def`, `def_cpm`].
	- `bonus`:     Static bonuses, list of `friend`, `helpers`, etc.
	- `atk_seq`:   Attacks sequence (index of the `atk_stats` list).
	- `seg_seq`:   Segment drops sequence (can be `None`).
	"""
	res_range = {}
	atk_stats = _to_float(atk_stats)
	def_stats = _to_float(def_stats)
	bonus = _prod_bonus(_to_float(bonus))
	step = round(1 / step)
	start, end = round(start * step), round(end * step)
	for k in [x / step for x in range(start, end + 1)]:
		fk = 1 / _to_float(k) if inv else _to_float(k)
		dmgs = tuple(map(lambda s : _dmg(s, def_stats, bonus, fk), atk_stats))
		segs = _hp_seq(def_stats[0], map(lambda atk : dmgs[atk], atk_seq))
		segs = list(map(lambda n : segs[n - 1][1] - segs[n][1], range(1, len(segs))))
		if seg_seq == None:
			print(str(k) + " -> " + str(dmgs) + ": " + str(segs))
		elif segs == seg_seq:
			res_range[k] = dmgs
	if len(res_range) != 0:
		minx, maxx = min(res_range), max(res_range)	
		print(str(minx) + " -> " + str(res_range[minx]))
		print(str(maxx) + " -> " + str(res_range[maxx]))
	elif seg_seq != None:
		print("No result found on range: " + str(start / step) + " - " + str(end / step))
