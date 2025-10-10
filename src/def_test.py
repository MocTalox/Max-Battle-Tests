from src.mult_test import main
import sys

# Test input data
atk_stats = []
atk_stats.append([400, 234, 14, 0.5974, 1.2, 1.6, 1.0])
atk_stats.append([13, 234, 14, 0.5974, 1.2, 1.6, 1.0])
def_stats = [20000, 185, 1]
bonus = [1.0, 1.2]
atk_seq = [0] + [1] * 97

# Bonus values range config
start, end, step = 0.59, 0.61, 0.000001

with open('output.txt', 'w') as sys.stdout:
	main(atk_stats, def_stats, bonus, False, atk_seq, None, start, end, step, True)
