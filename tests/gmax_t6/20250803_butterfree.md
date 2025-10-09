# Butterfree

Butterfree was available in T6 Gigantamax Battles on August 3rd globaly during the *Gigantamax Butterfree Max Battle Day* event.

## Summary

Butterfree has an Attack CPM value in the range `0.761276` - `0.774019`, and supposedly a HP value of `100k` and a Defense CPM value of `0.85`, which means it has a CPM of `0.85` and an Attack Multiplier of `0.9`:

Stats     | Values
:-------- | :------
HP        | `100k`
CPM       | `0.85`
*AtkMult* | `0.9`
*DefMult* | `1.0`
*AtkCPM*  | `0.765`
*DefCPM*  | `0.85`

## Attack CPM tests

**Spread NWB Bug Buzz vs Lvl50 15/15/11 Cinderace**

Health: [134/168 hp (34 dmg)](../../res/butterfree_02.png)

```py
from src.max_utils import mult
0.5 * 95 * (167 + 15) / ((163 + 15) * 0.8403) * 1.2 * 0.625
mult(34, _)
```

```
(0.7612758357432043, 0.7843448004626954)
```

Attack CPM range: `0.761276` - `0.784344`

---

**Spread NWB Bug Buzz vs Lvl50 15/15/15 Zacian**

Health: 158/173 hp (15 dmg)

```py
from src.max_utils import mult
0.5 * 95 * (167 + 15) / ((240 + 15) * 0.8403) * 1.2 * 0.390625
mult(15, _)
```

```
(0.7402804858299595, 0.7931576633892423)
```

Attack CPM range: `0.740281` - `0.793157`

---

**Spread NWB Bug Buzz vs Lvl50 15/15/15 Blissey**

Health: 377/429 hp (52 dmg)

```py
from src.max_utils import mult
0.5 * 95 * (167 + 15) / ((169 + 15) * 0.8403) * 1.2
mult(52, _)
```

```
(0.7601094274146907, 0.7750135338345866)
```

Attack CPM range: `0.760110` - `0.775013`

---

**Spread NWB Signal Beam vs Lvl50 15/15/15 Blissey**

Health: 388/429 hp (41 dmg)

```py
from src.max_utils import mult
0.5 * 75 * (167 + 15) / ((169 + 15) * 0.8403) * 1.2
mult(41, _)
```

```
(0.7551413919413921, 0.7740199267399269)
```

Attack CPM range: `0.755142` - `0.774019`

---

**Spread Windy Psychic vs Lvl50 15/15/15 Blissey**

Health: 377/429 hp (52 dmg)

```py
from src.max_utils import mult
0.5 * 95 * (167 + 15) / ((169 + 15) * 0.8403) * 1.2
mult(52, _)
```

```
(0.7601094274146907, 0.7750135338345866)
```

Attack CPM range: `0.760110` - `0.775013`

## HP tests

Hits for first segment:
- 200 hits

> ↩️ Test reference on [Defense verification tests](#defense-verification-tests).

HP value: A multiple of `200` (segment), `20k` (total)

## Defense verification tests

**Lvl50 15atk Blissey (Pound), NWB, 18 helpers**

> 🛠️ Dev note: The purpose of this test is to find the exact HP multiple value, due to the lack of HP tests.

Attacks damage:
- Pound: `5` dmg

> 📝 Note: Using `0.85` Defense CPM.

```py
0.5 * 6 * ((129 + 15) * 0.8403) / ((137 + 15) * 0.85) * 1.2 * 1.2
floor(_) + 1
```

```
5
```

The first segment flips at 200 hits, which means the HP value is `1000` (segment), `100k` (total).

---

**Lvl50 15atk Zamazenta (Metal Claw, Behemoth Bash) + Lvl51 15atk Cinderace (Lv3 G-Max Fireball, Tackle), Sunny, FB4, 39 helpers** ([battle](https://youtu.be/xiE5sXMGp58))

Attacks damage:
- Metal Claw: `9` dmg
- Behemoth Bash: `171` dmg
- G-Max Fireball: `1133` dmg
- Tackle: `6` dmg

> 📝 Note: Using `0.85` Defense CPM.

```py
# Metal Claw
0.5 * 6 * ((250 + 15) * 0.8403) / ((137 + 15) * 0.85) * 1.2 * 1.1 * 1.2
floor(_) + 1

# Behemoth Bash
0.5 * 125 * ((250 + 15) * 0.8403) / ((137 + 15) * 0.85) * 1.2 * 1.1 * 1.2
floor(_) + 1

# G-Max Fireball
0.5 * 450 * ((238 + 15) * 0.8453) / ((137 + 15) * 0.85) * 1.2 * 1.6 * 1.2 * 1.1 * 1.2
floor(_) + 1

# Tackle
0.5 * 5 * ((238 + 15) * 0.8453) / ((137 + 15) * 0.85) * 1.1 * 1.2
floor(_) + 1
```

```
9
171
1133
6
```

Segments sequence:
- Segment #1:
  - 90 Metal Claw
  - 1 G-Max Fireball
- Segments #2 & #3:
  - 1 G-Max Fireball
- Segments #4 & #5:
  - 2 G-Max Fireball
- Segment #6:
  - 13 Tackle
  - 59 Metal Claw
  - 1 Behemoth Bash
- Segments #7 & #8:
  - 3 Behemoth Bash
  - 4 Metal Claw
  - 2 G-Max Fireball
- Segments #9 to #11:
  - 2 G-Max Fireball
- Segments #12 & #13:
  - 2 G-Max Fireball
- Segment #14:
  - 11 Tackle
  - 52 Metal Claw

> 📝 Note: Using `100k` total HP.

```py
from src.max_utils import seg
dmg = (9, 171, 1133, 6)
print(seg(dmg, (90, 0, 1, 0), 1000))
print(seg(dmg, (90, 0, 2, 0), 1000))
print(seg(dmg, (90, 0, 4, 0), 1000))
print(seg(dmg, (149, 1, 4, 13), 1000))
print(seg(dmg, (153, 4, 6, 13), 1000))
print(seg(dmg, (153, 4, 8, 13), 1000))
print(seg(dmg, (153, 4, 10, 13), 1000))
print(seg(dmg, (205, 4, 10, 24), 1000))
```

```
Seg: 1 | Extra: 943 dmg | Total: 1943 dmg
Seg: 3 | Extra: 76 dmg | Total: 3076 dmg
Seg: 5 | Extra: 342 dmg | Total: 5342 dmg
Seg: 6 | Extra: 122 dmg | Total: 6122 dmg
Seg: 8 | Extra: 937 dmg | Total: 8937 dmg
Seg: 11 | Extra: 203 dmg | Total: 11203 dmg
Seg: 13 | Extra: 469 dmg | Total: 13469 dmg
Seg: 14 | Extra: 3 dmg | Total: 14003 dmg
```

All the segments flip at the expected moment ✔️

---

**Lvl40 14atk & 12atk Zamazenta (Metal Claw) + Lvl40 15atk Cinderace (Lv3 G-Max Fireball, Tackle), NWB, FB4, 0 helpers** ([battle](https://youtu.be/CDdnzvqpm1M))

Attacks damage:
- Metal Claw: `7` dmg
- G-Max Fireball: `736` dmg
- Tackle: `5` dmg

> 📝 Note: Using `0.85` Defense CPM.

```py
# Metal Claw (14atk)
0.5 * 6 * ((250 + 14) * 0.7903) / ((137 + 15) * 0.85) * 1.2 * 1.1
floor(_) + 1

# Metal Claw (12atk)
0.5 * 6 * ((250 + 12) * 0.7903) / ((137 + 15) * 0.85) * 1.2 * 1.1
floor(_) + 1

# G-Max Fireball
0.5 * 450 * ((238 + 15) * 0.7903) / ((137 + 15) * 0.85) * 1.2 * 1.6 * 1.1
floor(_) + 1

# Tackle
0.5 * 5 * ((238 + 15) * 0.7903) / ((137 + 15) * 0.85) * 1.1
floor(_) + 1
```

```
7
7
736
5
```

Segments sequence:
- Segments #1 & #2:
  - 98(-1?) Metal Claw
  - 2 G-Max Fireball
- Segment #3:
  - 2 G-Max Fireball
- Segments #4 & #5:
  - 3 G-Max Fireball
- Segment #6:
  - 15 Tackle
  - 14(+2?) Metal Claw

> 📝 Note: Using `100k` total HP.

```py
from src.max_utils import seg
dmg = (7, 736, 5)
print(seg(dmg, (98, 2, 0), 1000))
print(seg(dmg, (98, 4, 0), 1000))
print(seg(dmg, (98, 7, 0), 1000))
print(seg(dmg, (112, 7, 15), 1000))
```

```
Seg: 2 | Extra: 158 dmg | Total: 2158 dmg
Seg: 3 | Extra: 630 dmg | Total: 3630 dmg
Seg: 5 | Extra: 838 dmg | Total: 5838 dmg
Seg: 6 | Extra: 11 dmg | Total: 6011 dmg
```

All the segments flip at the expected moment ✔️

---

**Lvl50 15atk Zamazenta (Metal Claw) + Lvl40 14atk Zamazenta (Metal Claw) + Lvl50 15atk Cinderace (Lv3 G-Max Fireball), NWB, FB4, 0 helpers, Shroom** ([battle](https://youtu.be/oCQbnDC2ViQ))

Attacks damage:
- Metal Claw: `14` dmg
- G-Max Fireball: `1564` dmg

> 📝 Note: Using `0.85` Defense CPM.

```py
# Metal Claw (Lvl50 15atk)
0.5 * 6 * ((250 + 15) * 0.8403) / ((137 + 15) * 0.85) * 1.2 * 1.1
2 * (floor(_) + 1)

# Metal Claw (Lvl40 14atk)
0.5 * 6 * ((250 + 14) * 0.7903) / ((137 + 15) * 0.85) * 1.2 * 1.1
2 * (floor(_) + 1)

# G-Max Fireball
0.5 * 450 * ((238 + 15) * 0.8403) / ((137 + 15) * 0.85) * 1.2 * 1.6 * 1.1
2 * (floor(_) + 1)
```

```
14
14
1564
```

Segments sequence:
- Segment #1:
  - 72 Metal Claw
- Segment #2:
  - 18 Metal Claw
  - 1 G-Max Fireball
- Segments #3 & #4:
  - 1 G-Max Fireball
- Segment #5:
  - 1 G-Max Fireball
- Segment #6:
  - 4 Metal Claw

> 📝 Note: Using `100k` total HP.

```py
from src.max_utils import seg
dmg = (14, 1564)
print(seg(dmg, (72, 0), 1000))
print(seg(dmg, (90, 1), 1000))
print(seg(dmg, (90, 2), 1000))
print(seg(dmg, (90, 3), 1000))
print(seg(dmg, (94, 3), 1000))
```

```
Seg: 1 | Extra: 8 dmg | Total: 1008 dmg
Seg: 2 | Extra: 824 dmg | Total: 2824 dmg
Seg: 4 | Extra: 388 dmg | Total: 4388 dmg
Seg: 5 | Extra: 952 dmg | Total: 5952 dmg
Seg: 6 | Extra: 8 dmg | Total: 6008 dmg
```

All the segments flip at the expected moment ✔️
