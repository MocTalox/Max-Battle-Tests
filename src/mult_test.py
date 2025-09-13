from math import floor, ceil
from struct import pack, unpack

# Truncates value to float precision
# Recursive with lists of values
def f(x):
	if type(x) == int:
		return x
	if type(x) == float:
		return unpack('f', pack('f', x))[0]
	return list(map(f, x))

# Calculates output damage
def dmg(atkStats, defStats, bonus, extraBonus):
	attack = (atkStats[1] + atkStats[2]) * atkStats[3]
	defense = (defStats[1] + 15) * defStats[2]
	raw = 0.5 * atkStats[0] * attack / defense * atkStats[4] * atkStats[5] * atkStats[6] * bonus
	return floor(raw * extraBonus) + 1

# Calculates HP and remaining segments sequence
def hpSeq(totalHp, atks):
	hp = totalHp
	res = [(hp, 100)]
	for atk in atks:
		hp = hp - atk
		res.append((hp, ceil(100 * hp / totalHp)))
	return res

# Calculates an additional bonus value for a test (within the start-end-step range)
# If segSeq is informed, obtains the range of bonus values that satisfies that sequence
# Else (segSeq is None), obtains all segment sequence for the range of bonus values
# - atkStats: List of lists with [power, baseAtk, ivAtk, atkCPM, stab, type, weather]
# - defStats: List with [totalHp, baseDef, defCPM]
# - bonus:    Static bonuses, product of friend, helpers, etc
# - atkSeq:   Attacks sequence
# - segSeq:   Segment drops sequence (can be None)
def main(atkStats, defStats, bonus, atkSeq, segSeq, start, end, step):
	resRange = {}
	atkStats = f(atkStats)
	defStats = f(defStats)
	bonus = f(bonus)
	step = round(1 / step)
	start, end = round(start * step), round(end * step)
	for (k, fk) in [(x, f(x)) for x in map(lambda x : x / step, range(start, end + 1))]:
		dmgs = tuple(map(lambda s : dmg(s, defStats, bonus, fk), atkStats))
		segs = hpSeq(defStats[0], map(lambda atk : dmgs[atk], atkSeq))
		segs = list(map(lambda n : segs[n - 1][1] - segs[n][1], range(1, len(segs))))
		if segSeq == None:
			print(str(k) + " -> " + str(dmgs) + ": " + str(segs))
		elif segs == segSeq:
			resRange[k] = dmgs
	if len(resRange) != 0:
		minx, maxx = min(resRange), max(resRange)	
		print(str(minx) + " -> " + str(resRange[minx]))
		print(str(maxx) + " -> " + str(resRange[maxx]))
	elif segSeq != None:
		print("No result found on range: " + str(start / step) + " - " + str(end / step))
