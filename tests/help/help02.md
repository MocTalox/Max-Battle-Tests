# Helpers bonus 2 people

## Summary

Smallest Bonus Values Range: `1.149838` - `1.150017`

Potential Bonus Value: `1.15` (as double `1.149999976158142`)

## Tests

**Lvl40 14/15/14 Venusaur (Lvl3 G-Max Vine Lash, Razor Leaf) vs Wailmer (T2), NWB, FB4, 2 helpers**

Sequence: `[58, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 2]`

```py
# Use this code in src/help_test.py
atk_stats = []
atk_stats.append([450, 198, 14, 0.7903, 1.2, 1.6, 1.0])
atk_stats.append([13, 198, 14, 0.7903, 1.2, 1.6, 1.0])
def_stats = [5000, 68, 0.38]
bonus = 1.1
atk_seq = [0] + [1] * 25
```

Attacks Damage: `[{2902, 2903}, {84}]`

Bonus Values Range: `1.149226` - `1.150017`

---

**Lvl35 14/15/15 Excadrill (Lvl3 Max Quake) + Lvl20 14/15/15 Wooloo (Take Down) vs Pidove (T1), NWB, NFB, 2 helpers**

Sequence: `[79, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2]`

```py
# Use this code in src/help_test.py
atk_stats = []
atk_stats.append([350, 255, 14, 0.761563838, 1.2, 0.390625, 1.0])
atk_stats.append([7, 76, 14, 0.5974, 1.2, 1.0, 1.0])
def_stats = [1700, 80, 0.15]
bonus = 1.0
atk_seq = [0] + [1] * 19
```

Attacks Damage: `[{1357}, {19}]`

Bonus Values Range: `1.149838` - `1.150685`
