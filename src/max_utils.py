from math import floor

# Converts the damage to segments:
# - First: number of segments
# - Second: extra dmg done to next segment
# - Third: total dmg (same as input)

# Calculates the segment damage
segCalc = lambda dmg, hp : (floor(dmg / hp), dmg % hp, dmg)

# Converts `segCalc` result to readable string
segStr = lambda s, xd, td : "Seg: " + str(s) + " | Extra: " + str(xd) + " dmg | Total: " + str(td) + " dmg\n"

# Prints `segStr` result to output file
segPrint = lambda dmg, hp : print(segStr(*segCalc(dmg, hp)))
