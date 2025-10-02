from math import floor

# Converts the damage to segments:
# - First: number of segments
# - Second: extra dmg done to next segment
# - Third: total dmg (same as input)

# Calculates the segment damage
seg_calc = lambda dmg, hp : (floor(dmg / hp), dmg % hp, dmg)

# Converts `seg_calc` result to readable string
seg_str = lambda s, xd, td : "Seg: " + str(s) + " | Extra: " + str(xd) + " dmg | Total: " + str(td) + " dmg\n"

# Prints `seg_str` result to output file
seg_print = lambda dmg, hp : print(seg_str(*seg_calc(dmg, hp)))

# Calculates the possible multiplier values needed to produce
# the resulting damage, by being multiplied to a base damage.
# IOW, values which fulfill: floor(base * mult) + 1 = res
mult = lambda res, base : ((res - 1) / base, res / base)
