from mult_test import main
import sys

# Test input data
atk_stats = []
atk_stats.append([250, 160, 14, 0.626567125, 1.0, 1.0, 1.0])
atk_stats.append([7, 76, 14, 0.5974, 1.2, 1.0, 1.0])
def_stats = [1700, 80, 0.15]
bonus = 1.0
atk_seq = [0] + [1] * 27

# Test result data
seg_seq = [67, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1]

# Bonus values range config
start, end, step = 1.199, 1.201, 0.000001

with open('output.txt', 'w') as sys.stdout:
	main(atk_stats, def_stats, bonus, False, atk_seq, seg_seq, start, end, step)
