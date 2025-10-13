# Toxtricity

Toxtricity was available in T6 Gigantamax Battles on November 16th and 17th in-person on Fukuoka during the *Pokémon GO Wild Area: Fukuoka* event. Later it became available on November 23rd and 24th globaly during the *Pokémon GO Wild Area: Global* event. The stats remained the same during both events.

## Summary

Stats     | Values
:-------- | :------
HP        | `100k`
CPM       | `0.9`
*AtkMult* | `1.15`
*DefMult* | `1.45`
*AtkCPM*  | `1.035`
*DefCPM*  | `1.305`

## Attack CPM tests

*Attack CPM Tests done during this period will be uploaded soon!*

## HP tests

> 🛠️ Dev note: No proper HP tests were done this time. The HP value of `100k` was obtained directly from [Defense verification tests](#defense-verification-tests), which was the only *decently pretty* value that fulfilled the tests done on that section. This was the same aproach used on early HP testing.

## Defense verification tests

> 📝 Note: Using `1.305` Defense CPM and `100k` total HP.

---

**Lvl50 15atk Excadrill (Mud Shot) + Lvl50 15atk Gengar (Shadow Claw) + Lvl50 15atk Greedent (Mud Shot), NWB, 4 helpers**

Attacks damage:
- Excadrill Mud Shot: `9` dmg
- Gengar Shadow Claw: `5` dmg
- Greedent Mud Shot: `5` dmg

```py
# Excadrill Mud Shot
0.5 * 4 * ((255 + 15) * 0.8403) / ((140 + 15) * 1.305) * 1.2 * 2.56 * 1.18
floor(_) + 1

# Gengar Shadow Claw
0.5 * 6 * ((261 + 15) * 0.8403) / ((140 + 15) * 1.305) * 1.2 * 1.18
floor(_) + 1

# Greedent Mud Shot
0.5 * 4 * ((160 + 15) * 0.8403) / ((140 + 15) * 1.305) * 2.56 * 1.18
floor(_) + 1
```

```
9
5
5
```

Segments sequence:
- Segment #1:
  - 85 Excadrill Mud Shot
  - 15 Gengar Shadow Claw
  - 32 Greedent Mud Shot

```py
from src.max_utils import seg
print(seg((9, 5, 5), (85, 15, 32), 1000))
```

```
Seg: 1 | Extra: 0 dmg | Total: 1000 dmg
```

The segment flips at the expected moment ✔️
