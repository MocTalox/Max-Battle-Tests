from math import floor, ceil
from functools import reduce
from src.hp_test import xlcm

# - `tests`: list of tuples (number of hits, number of segments, raw damage)
def hp(limit, tests):
	single = lambda test : test[1] == 1 # Change `single` filter
	hits = lambda test : test[0]
	mult = lambda hp : (hp, _get_mult(hp, tests))
	valid = lambda r : r[1][0] < r[1][1]
	return filter(valid, map(mult, xlcm(limit, map(hits, filter(single, tests)))))

def _get_mult(hp, tests):
	range = lambda test : _get_range(hp, test)
	mix = lambda r1, r2 : (max(r1[0], r2[0]), min(r1[1], r2[1]))
	return reduce(mix, map(range, tests))

def _get_range(hp, test):
	min_val = ceil(hp * test[1] / test[0])
	max_val = floor(hp * test[1] / (test[0] - 1))
	return ((min_val - 1) / test[2], max_val / test[2])

tests = []
tests.append((14, 1, 14.74801975675372))
tests.append((27, 2, 14.74801975675372))
tests.append((200, 1, 0.3565935584222115))
tests.append((100, 1, 1.9425137396215684))
tests.append((67, 1, 2.081264695708987))
print("Toxtricity")
for r in hp(100000, tests): # Up to 100k segment HP (10M total HP)
	print("HP: " + str(r[0] * 100) + " DefMult: [" + str(r[1][0]) + ", " + str(r[1][1]) + ")")

tests = []
tests.append((21, 1, 5.941641257142858))
tests.append((250, 1, 0.19657750000000002))
print("Raikou")
for r in hp(100000, tests): # Up to 100k segment HP (10M total HP)
	print("HP: " + str(r[0] * 100) + " DefMult: [" + str(r[1][0]) + ", " + str(r[1][1]) + ")")
