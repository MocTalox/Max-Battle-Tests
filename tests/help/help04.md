# Helpers bonus 4 people

## Summary

Smallest Bonus Values Range: `1.179228` - `1.180015`

Potential Bonus Value: `1.18` (as double `1.1799999475479126`)

## Tests

**Lvl20 15/11/12 Kingler (Lvl1 G-Max Foam Burst) + Lvl20 15/14/14 Darumaka (Fire Fang) vs Omanyte (T1), NWB, NFB, 4 helpers**

Sequence: `[88, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]`

```py
# Use this code in src/help_test.py
atk_stats = []
atk_stats.append([350, 240, 15, 0.5974, 1.2, 1.0, 1.0])
atk_stats.append([13, 153, 15, 0.5974, 1.2, 0.390625, 1.0])
def_stats = [1700, 153, 0.15]
bonus = 1.0
atk_seq = [0] + [1] * 12
```

Attacks Damage: `[{1498}, {15}]`

Bonus Values Range: `1.179228` - `1.180015`
