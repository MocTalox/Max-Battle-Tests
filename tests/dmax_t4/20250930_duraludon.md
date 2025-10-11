# Duraludon

Duraludon was available in T4 Dynamax Battles from September 30th to October 7th globaly during the *Steel Skyline* event.

## Summary

Duraludon has an Attack CPM value in the range `0.599994` - `0.600001`, a HP value of `20k` and a Defense CPM value in the range `0.597811` - `0.604158`, which means it simply has a CPM of `0.6`:

Stats     | Toxtricity | Duraludon
:-------- | :--------- | :--------
HP        | `20k`      | `20k`
CPM       | `0.6`      | `0.6`
*AtkMult* | `1.0`      | `1.0`
*DefMult* | `1.0`      | `1.0`
*AtkCPM*  | `0.6`      | `0.6`
*DefCPM*  | `0.6`      | `0.6`

These are the same stats as Dynamax Toxtricity which means it is safe to say that T4 Dynamax Battles have fixed stats for their bosses.

## Attack CPM tests

**Spread NWB Dragon Claw vs Lvl40 13/14/15 Charizard**

Health: [130/158 hp (28 dmg)](../../res/duraludon_01.png)

```py
from src.max_utils import mult
0.5 * 45 * (239 + 15) / ((173 + 14) * 0.7903) * 1.2
mult(28, _)
```

```
(0.5818350393700787, 0.6033844852726743)
```

Attack CPM range: `0.581836` - `0.603384`

---

**Spread NWB Dragon Claw vs Lvl20 14/12/14 Snorlax**

Health: [166/205 hp (39 dmg)](../../res/duraludon_02.png)

```py
from src.max_utils import mult
0.5 * 45 * (239 + 15) / ((169 + 12) * 0.5974) * 1.2
mult(39, _)
```

```
(0.5991421988918053, 0.6149090988626422)
```

Attack CPM range: `0.599143` - `0.614909`

---

**Spread NWB Flash Cannon vs Lvl25 15/11/14 Lapras**

Health: [120/194 hp (74 dmg)](../../res/duraludon_03.png)

```py
from src.max_utils import mult
0.5 * 100 * (239 + 15) / ((174 + 11) * 0.667934) * 1.2
mult(74, _)
```

```
(0.5918929573490813, 0.6000010800524934)
```

Attack CPM range: `0.591893` - `0.600001`

---

**Spread NWB Hyper Beam vs Lvl30 10/14/14 Drizzile**

Health: [5/129 hp (124 dmg)](../../res/duraludon_04.png)

```py
from src.max_utils import mult
0.5 * 150 * (239 + 15) / ((113 + 14) * 0.7317)
mult(124, _)
```

```
(0.599994, 0.604872)
```

Attack CPM range: `0.599994` - `0.604872`

## HP tests

Hits for first segment:
- [200 hits](https://youtu.be/htdwXmz2eTs)
- 29 hits
- 34 hits
- 50 hits
- 40 hits

> ↩️ Test references on [Defense CPM tests](#defense-cpm-tests).

```py
from src.hp_test import hp_lcm
hp_lcm(1000, [200, 29, 34, 50, 40])
```

```
[200]
```

HP value: `200` (segment), `20k` (total)

## Defense CPM tests

> 📝 Note: Using `20k` total HP.

---

**Lvl20 14/12/12 Machamp (Lvl2 G-Max Chi Strike, Counter), NWB, 24 helpers** ([battle](https://youtu.be/IOMIv4loZ-M))

Segments sequence:
- Segments #1 & #2:
  - 1 Chi Strike
- Segment #3:
  - 2 Counter
- Segment #4:
  - 11 Counter
- Segment #5:
  - 10 Counter
- Segment #6:
  - 11 Counter
- Segment #7:
  - 10 Counter
- Segment #8:
  - 11 Counter
- Segment #9:
  - 10 Counter
- Segment #10:
  - 11 Counter
- Segment #11:
  - 10 Counter
- Segment #12:
  - 11 Counter

```py
# Use this code in src/def_test.py
atk_stats = []
atk_stats.append([400, 234, 14, 0.5974, 1.2, 1.6, 1.0])
atk_stats.append([13, 234, 14, 0.5974, 1.2, 1.6, 1.0])
def_stats = [20000, 185, 1]
bonus = [1.0, 1.2]
atk_seq = [0] + [1] * 97
```

Attacks Damage:
- Chi Strike: `566` to `571` dmg
- Counter: `19` dmg

Defense CPM range: `0.597811` - `0.604158`

---

**Lvl50 15/15/15 Zacian (Metal Claw), NWB, 7 helpers**

First segment: 29 hits (7 dmg)

```py
from src.max_utils import mult
0.5 * 6 * ((332 + 15) * 0.8403) / (185 + 15) * 1.2 * 0.625 * 1.192
mult(7, _, True)
```

```
(0.5585918258571428, 0.6516904635)
```

Defense CPM range: `0.558592` - `0.651690`

---

**Lvl40 15/13/15 Zacian (Metal Claw), NWB, 0 helpers**

First segment: 34 hits (6 dmg)

```py
from src.max_utils import mult
0.5 * 6 * ((332 + 15) * 0.7903) / (185 + 15) * 1.2 * 0.625
mult(6, _, True)
```

```
(0.5141889375, 0.617026725)
```

Defense CPM range: `0.514189` - `0.617026`

---

**Lvl40 15/13/15 Zamazenta (Metal Claw), NWB, 0 helpers**

First segment: 50 hits (4 dmg)

```py
from src.max_utils import mult
0.5 * 6 * ((250 + 15) * 0.7903) / (185 + 15) * 1.2 * 0.625
mult(4, _, True)
```

```
(0.58902046875, 0.785360625)
```

Defense CPM range: `0.589021` - `0.785360`

---

**Lvl40 15/13/15 Zamazenta (Metal Claw), NWB, 2 helpers**

First segment: 40 hits (5 dmg)

```py
from src.max_utils import mult
0.5 * 6 * ((250 + 15) * 0.7903) / (185 + 15) * 1.2 * 0.625 * 1.15
mult(5, _, True)
```

```
(0.5418988312499999, 0.6773735390625)
```

Defense CPM range: `0.541899` - `0.677373`
