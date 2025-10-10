# Helpers bonus 1 person

## Summary

Smallest Bonus Values Range: `1.099959` - `1.100656`

Potential Bonus Value: `1.1` (as double `1.100000023841858`)

## Tests

**Lvl35 14/15/15 Excadrill (Lvl3 Max Quake) + Lvl20 14/15/15 Krabby (Mud Shot) vs Pidove (T1), NWB, NFB, 1 helper**

Sequence: `[76, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1]`

```py
# Use this code in src/help_test.py
atk_stats = []
atk_stats.append([350, 255, 14, 0.761563838, 1.2, 0.390625, 1.0])
atk_stats.append([4, 181, 14, 0.5974, 1.0, 0.390625, 1.0])
def_stats = [1700, 80, 0.15]
bonus = 1.0
atk_seq = [0] + [1] * 51
```

Attacks Damage: `[{1298}, {8}]`

Bonus Values Range: `1.099809` - `1.100656`

---

**Lvl35 15/14/15 Excadrill (Lvl3 Max Quake) + Lvl20 15/15/15 Krabby (Mud Shot) vs Pidove (T1), NWB, NFB, 1 helper**

Sequence: `[76, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]`

```py
# Use this code in src/help_test.py
atk_stats = []
atk_stats.append([350, 255, 15, 0.761563838, 1.2, 0.390625, 1.0])
atk_stats.append([4, 181, 15, 0.5974, 1.0, 0.390625, 1.0])
def_stats = [1700, 80, 0.15]
bonus = 1.0
atk_seq = [0] + [1] * 50
```

Attacks Damage: `[{1303}, {8}]`

Bonus Values Range: `1.099959` - `1.100803`
