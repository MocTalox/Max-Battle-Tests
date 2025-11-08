# Grimmsnarl

Grimmsnarl was available in T6 Gigantamax Battles from November 7th to November 9th in-person on Nagasaki during the *Pokémon GO Wild Area: Nagasaki* event. Later it became available on November 15th and 16th globaly during the *Pokémon GO Wild Area: Global* event. The stats remained the same during both events.

## Summary

Grimmsnarl has an Attack CPM value in the range `1.079394` - `1.080001`, and very likely a HP value of `70k` and a Defense CPM value of `1.2`, which means it has a CPM of `1.2` and an Attack Multiplier of `0.9`:

Stats     | Values
:-------- | :------
HP        | `70k`
CPM       | `1.2`
*AtkMult* | `0.9`
*DefMult* | `1.0`
*AtkCPM*  | `1.08`
*DefCPM*  | `1.2`

## Attack CPM tests

**Spread NWB Power-Up Punch vs Lvl42.5 15/13/15 Blissey**

Health: 338/410 hp (72 dmg)

```py
from src.max_utils import mult
0.5 * 50 * (227 + 15) / ((169 + 13) * 0.8028039) * 1.6
mult(72, _)
```

```
(1.071676859070248, 1.086770899338843)
```

Attack CPM range: `1.071677` - `1.08677`

---

**Spread NWB Foul Play vs Lvl50 15/15/14 Zacian**

Health: [140/173 hp (33 dmg)](../../res/grimmsnarl_01.png)

```py
from src.max_utils import mult
0.5 * 70 * (227 + 15) / ((240 + 15) * 0.8403) * 1.2 * 0.625
mult(33, _)
```

```
(1.0793936245572608, 1.1131246753246753)
```

Attack CPM range: `1.079394` - `1.113124`

---

**Target NWB Play Rough vs Lvl29 15/15/15 Garbodor**

Health: [10/147 hp (137 dmg)](../../res/grimmsnarl_02.png)

```py
from src.max_utils import mult
0.5 * 90 * (227 + 15) / ((164 + 15) * 0.719399095) * 1.2 * 0.625 * 2
mult(137, _)
```

```
(1.0721182472408937, 1.0800014696470768)
```

Attack CPM range: `1.072119` - `1.080001`

## HP tests

*HP tests done during this period will be uploaded soon!*

## Defense verification tests

> 📝 Note: Using `1.2` Defense CPM and `70k` total HP.

---

**Grimmsnarl Solo Test: NWB, 15+ helpers** ([battle](https://youtu.be/yRSTG8lUuRE))

Attacks damage:
- Lvl50 15atk Zacian
  - Metal Claw: `11` dmg

```py
# Metal Claw
0.5 * 6 * ((332 + 15) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.2
floor(_) + 1
```

Segments sequence:
- Segment #1:
  - 64 Metal Claw

```py
from src.max_utils import seg
print(seg(11, 64, 700))
```

```
Seg: 1 | Extra: 4 dmg | Total: 704 dmg
```

All the segments flip at the expected moment ✔️

---

**Grimmsnarl Duo Battle: Clear, FB4, 9 helpers, Shroom** ([battle](https://youtu.be/1XUpFHw4pn4))

Attacks damage:
- Lvl40 15atk Zamazenta
  - Metal Claw: `18` dmg
  - Behemoth Bash: `358` dmg
- Lvl40 12atk Zamazenta
  - Metal Claw: `18` dmg
  - Behemoth Bash: `354` dmg
- Lvl40 15atk Zacian
  - Behemoth Blade (Max): `1310` dmg

```py
# 15atk Metal Claw
0.5 * 6 * ((250 + 15) * 0.7903) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.194
2 * (floor(_) + 1)

# 15atk Behemoth Bash
0.5 * 125 * ((250 + 15) * 0.7903) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.194
2 * (floor(_) + 1)

# 12atk Metal Claw
0.5 * 6 * ((250 + 12) * 0.7903) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.194
2 * (floor(_) + 1)

# 12atk Behemoth Bash
0.5 * 125 * ((250 + 12) * 0.7903) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.194
2 * (floor(_) + 1)

# Behemoth Blade (Max)
0.5 * 350 * ((332 + 15) * 0.7903) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.194
2 * (floor(_) + 1)
```

Segments sequence:
- Segment #1:
  - 23 Metal Claw
  - 2 Behemoth Bash
- Segment #2:
  - 17 Metal Claw
- Segment #3:
  - 4 Metal Claw
  - 2 Behemoth Bash
- Segment #4:
  - 16 Metal Claw
  - 2 Behemoth Bash
- Segment #5:
  - 16 Metal Claw
- Segment #6:
  - 4 Metal Claw
  - 2 Behemoth Bash
- Segments #7 to #9:
  - 2 Metal Claw
  - 2 Behemoth Blade (Max)
- Segments #10 to #13:
  - 2 Behemoth Blade (Max)
- Segments #14 to #17:
  - 2 Behemoth Blade (Max)

```py
from src.max_utils import seg
dmg = (18, 354, 358, 1310)
print(seg(dmg, (23, 1, 1, 0), 700))
print(seg(dmg, (40, 1, 1, 0), 700))
print(seg(dmg, (44, 2, 2, 0), 700))
print(seg(dmg, (60, 3, 3, 0), 700))
print(seg(dmg, (76, 3, 3, 0), 700))
print(seg(dmg, (80, 4, 4, 0), 700))
print(seg(dmg, (82, 4, 4, 2), 700))
print(seg(dmg, (82, 4, 4, 4), 700))
print(seg(dmg, (82, 4, 4, 6), 700))
```

```
Seg: 1 | Extra: 426 dmg | Total: 1126 dmg
Seg: 2 | Extra: 32 dmg | Total: 1432 dmg
Seg: 3 | Extra: 116 dmg | Total: 2216 dmg
Seg: 4 | Extra: 416 dmg | Total: 3216 dmg
Seg: 5 | Extra: 4 dmg | Total: 3504 dmg
Seg: 6 | Extra: 88 dmg | Total: 4288 dmg
Seg: 9 | Extra: 644 dmg | Total: 6944 dmg
Seg: 13 | Extra: 464 dmg | Total: 9564 dmg
Seg: 17 | Extra: 284 dmg | Total: 12184 dmg
```

All the segments flip at the expected moment ✔️

---

**Grimmsnarl Duo Battle: Clear, FB4, 9 helpers, Shroom** ([battle 1](https://youtu.be/1XUpFHw4pn4), [battle 2](https://www.youtube.com/shorts/8ZhpOgAS4Qs))

Attacks damage:
- Lvl50 15atk Zamazenta
  - Metal Claw: `18` dmg
  - Behemoth Bash: `374` dmg
- Lvl50 14atk Zamazenta
  - Metal Claw: `18` dmg
  - Behemoth Bash: `372` dmg
- Lvl50 15atk Zacian
  - Metal Claw: `24` dmg
  - Behemoth Blade (Max): `1366` dmg

```py
# 15atk Metal Claw
0.5 * 6 * ((250 + 15) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.17
2 * (floor(_) + 1)

# 15atk Behemoth Bash
0.5 * 125 * ((250 + 15) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.17
2 * (floor(_) + 1)

# 14atk Metal Claw
0.5 * 6 * ((250 + 14) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.17
2 * (floor(_) + 1)

# 14atk Behemoth Bash
0.5 * 125 * ((250 + 14) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.17
2 * (floor(_) + 1)

# Zacian Metal Claw
0.5 * 6 * ((332 + 15) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.17
2 * (floor(_) + 1)

# Behemoth Blade (Max)
0.5 * 350 * ((332 + 15) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.1 * 1.17
2 * (floor(_) + 1)
```

Segments sequence:
- Segment #1:
  - 28 Metal Claw
  - 1 Behemoth Bash (14atk)
- Segment #2:
  - 13 Metal Claw
  - 1 Behemoth Bash (15atk)
- Segment #3:
  - 1 Behemoth Bash (14atk)
  - 15 Metal Claw
- Segment #4:
  - 6 Metal Claw
  - 2 Behemoth Bash
- Segment #5:
  - 1 Behemoth Bash (15atk)
  - 9 Metal Claw
- Segments #6 to #9:
  - 13 Metal Claw
  - 2 Behemoth Blade (Max)
- Segments #10 to #13:
  - 2 Behemoth Blade (Max)
- Segments #14 to #17:
  - 2 Behemoth Blade (Max)
- Segment #18:
  - 28 Metal Claw (Zacian)

```py
from src.max_utils import seg
dmg = (18, 372, 374, 1366, 24)
print(seg(dmg, (28, 1, 0, 0, 0), 700))
print(seg(dmg, (41, 1, 1, 0, 0), 700))
print(seg(dmg, (56, 2, 1, 0, 0), 700))
print(seg(dmg, (62, 3, 2, 0, 0), 700))
print(seg(dmg, (71, 3, 3, 0, 0), 700))
print(seg(dmg, (84, 3, 3, 2, 0), 700))
print(seg(dmg, (84, 3, 3, 4, 0), 700))
print(seg(dmg, (84, 3, 3, 6, 0), 700))
print(seg(dmg, (84, 3, 3, 6, 28), 700))
```

```
Seg: 1 | Extra: 176 dmg | Total: 876 dmg
Seg: 2 | Extra: 84 dmg | Total: 1484 dmg
Seg: 3 | Extra: 26 dmg | Total: 2126 dmg
Seg: 4 | Extra: 180 dmg | Total: 2980 dmg
Seg: 5 | Extra: 16 dmg | Total: 3516 dmg
Seg: 9 | Extra: 182 dmg | Total: 6482 dmg
Seg: 13 | Extra: 114 dmg | Total: 9214 dmg
Seg: 17 | Extra: 46 dmg | Total: 11946 dmg
Seg: 18 | Extra: 18 dmg | Total: 12618 dmg
```

All the segments flip at the expected moment ✔️

---

**Grimmsnarl Solo Test: NWB, 15+ helpers** ([battle](https://youtu.be/yRSTG8lUuRE))

Attacks damage:
- Lvl50 15atk Zacian
  - Metal Claw: `11` dmg

```py
# Metal Claw
0.5 * 6 * ((332 + 15) * 0.8403) / ((139 + 15) * 1.2) * 1.2 * 1.6 * 1.2
floor(_) + 1
```

Segments sequence:
- Segment #1:
  - 64 Metal Claw

```py
from src.max_utils import seg
print(seg(11, 64, 700))
```

```
Seg: 1 | Extra: 4 dmg | Total: 704 dmg
```

All the segments flip at the expected moment ✔️
