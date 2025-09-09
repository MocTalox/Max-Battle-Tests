from mult_test import main

# Test input data
atkStats = []
atkStats.append([250, 160, 14, 0.626567125, 1.0, 1.0, 1.0])
atkStats.append([7, 76, 14, 0.5974, 1.2, 1.0, 1.0])
defStats = [1700, 80, 0.15]
bonus = 1.0
atkSeq = [0] + [1] * 27

# Test result data
segSeq = [67, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1]

# Bonus values range config
start, end, step = 1.199, 1.201, 0.000001

main(atkStats, defStats, bonus, atkSeq, segSeq, start, end, step)
