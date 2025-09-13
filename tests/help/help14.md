# Helpers bonus 14 people

## Summary

Smallest Bonus Values Range: `1.198491` - `1.199255`

Potential Bonus Value: `1.199` (as double `1.1990000009536743`)

## Tests

**Lvl20 15/14/14 Darumaka (Fire Fang) vs Grookey (T1), NWB, NFB, 14 helpers**

Sequence: `[5, 6, 5, 6, 5, 6, 6, 5, 6, 5]`

```python
atkStats = []
atkStats.append([13, 153, 15, 0.5974, 1.2, 1.6, 1.0])
defStats = [1700, 91, 0.15]
bonus = 1.0
atkSeq = [0] * 10
```

Attacks Damage: `[{95}]`

Bonus Values Range: `1.193263` - `1.205956`

---

**Lvl28 10/13/14 Blastoise (Lvl1 G-Max Cannonade) + Lvl20 10/15/13 Caterpie (Tackle) vs Trubish (T1), NWB, NFB, 14 helpers**

Sequence: `[92, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0]`

```python
atkStats = []
atkStats.append([350, 171, 10, 0.706884205, 1.2, 1.0, 1.0])
atkStats.append([5, 55, 10, 0.5974, 1.0, 1.0, 1.0])
defStats = [1700, 122, 0.15]
bonus = 1.0
atkSeq = [0] + [1] * 21
```

Attacks Damage: `[{1568}, {6}]`

Bonus Values Range: `1.198491` - `1.199255`
