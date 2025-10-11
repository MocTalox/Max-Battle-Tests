# Butterfree

Butterfree was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Summary

Butterfree has the same stats as [last time](./20250803_butterfree.md):

## Attack verification tests

> 📝 Note: Using `0.765` Attack CPM.

---

**Spread NWB Bug Buzz vs Lvl20 12/14/15 Latias**

Health: [40/122 hp (82 dmg)](../../res/butterfree_01.png)

```py
0.5 * 95 * ((167 + 15) * 0.765) / ((246 + 14) * 0.5974) * 1.2 * 1.6
floor(_) + 1
```

```
82
```

The damage is the expected ✔️

## Defense verification tests

> 📝 Note: Using `0.85` Defense CPM and `100k` total HP.

---

**Lvl40 15atk & 14atk Blissey (Pound), NWB, FB4, 2 helpers**

Attacks damage:
- Pound (15atk): `5` dmg
- Pound (14atk): `4` dmg

```py
# Pound (15atk)
0.5 * 6 * ((129 + 15) * 0.7903) / ((137 + 15) * 0.85) * 1.2 * 1.1 * 1.15
floor(_) + 1

# Pound (14atk)
0.5 * 6 * ((129 + 14) * 0.7903) / ((137 + 15) * 0.85) * 1.2 * 1.1 * 1.15
floor(_) + 1
```

```
5
4
```

Segments sequence:
- Segment #1:
  - 113 Pound (15atk)
  - 109 Pound (14atk)

```py
from src.max_utils import seg
print(seg((5, 4), (113, 109), 1000))
```

```
Seg: 1 | Extra: 1 dmg | Total: 1001 dmg
```

The segment flips at the expected moment ✔️
