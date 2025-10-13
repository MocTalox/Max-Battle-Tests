# Toxtricity

Toxtricity was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Summary

Toxtricity has received a nerf to its Attack and Defense Multipliers since [last time](./20241116_toxtricity.md). Toxtricity has an Attack CPM value in the range `0.807268` - `0.813343` and very likely a HP value of `100k` and a Defense CPM value of `0.9`, which means it has the same CPM, an Attack Multiplier of `0.9` and a Defense Multiplier of `1.0`.

Stats     | Values
:-------- | :------
HP        | `100k`
CPM       | `0.9`
*AtkMult* | `0.9`
*DefMult* | `1.0`
*AtkCPM*  | `0.81`
*DefCPM*  | `0.9`

## Attack CPM tests

**Spread Cloudy Power-Up Punch vs Lvl27 14/14/15 Excadrill**

Health: [84/178 hp (94 dmg)](../../res/toxtricity_01.png)

```py
from src.max_utils import mult
0.5 * 50 * (224 + 15) / ((129 + 14) * 0.694143653) * 1.6 * 1.2
mult(94, _)
```

```
(0.8046911123820608, 0.8133437049883195)
```

Attack CPM range: `0.804692` - `0.813343`

---

**Spread NWB Wild Charge vs Lvl27 14/14/15 Excadrill**

Health: [136/178 hp (42 dmg)](../../res/toxtricity_02.png)

```py
from src.max_utils import mult
0.5 * 90 * (224 + 15) / ((129 + 14) * 0.694143653) * 1.2 * 0.390625
mult(42, _)
```

```
(0.8072676621803688, 0.8269571173554998)
```

Attack CPM range: `0.807268` - `0.826957`

---

**Spread NWB Wild Charge vs Lvl44 15/11/15 Eternatus**

Health: [189/229 hp (40 dmg)](../../res/toxtricity_03.png)

```py
from src.max_utils import mult
0.5 * 90 * (224 + 15) / ((192 + 11) * 0.8103) * 1.2 * 0.625
mult(40, _)
```

```
(0.7953070013947001, 0.8156994886099488)
```

Attack CPM range: `0.795308` - `0.815699`

---

**Spread NWB Wild Charge vs Lvl40 12/14/15 Metagross**

Health: [107/162 hp (55 dmg)](../../res/toxtricity_04.png)

```py
from src.max_utils import mult
0.5 * 90 * (224 + 15) / ((228 + 14) * 0.7903) * 1.2
mult(55, _)
```

```
(0.8002200836820085, 0.8150389741205641)
```

Attack CPM range: `0.800221` - `0.815038`

---

**Spread Cloudy Power-Up Punch vs Lvl40 15/12/14 Latias**

Health: [143/161 hp (18 dmg)](../../res/toxtricity_05.png)

```py
from src.max_utils import mult
0.5 * 50 * (224 + 15) / ((246 + 12) * 0.7903) * 0.625 * 1.2
mult(18, _)
```

```
(0.7735019916317992, 0.819002108786611)
```

Attack CPM range: `0.773502` - `0.819002`

---

**Target (dodged 60%) Cloudy Acid Spray vs Lvl43 15/15/13 Rillaboom**

Health: [166/191 hp (25 dmg)](../../res/toxtricity_06.png)

```py
from src.max_utils import mult
0.5 * 20 * (224 + 15) / ((168 + 15) * 0.8053) * 1.2 * 1.6 * 1.2 * 2 * 0.4
mult(25, _)
```

```
(0.8028782034518829, 0.8363314619290446)
```

Attack CPM range: `0.802879` - `0.836331`

---

**Target (dodged 55%) Cloudy Acid Spray vs Lvl40 13/14/14 Moltres**

Health: [157/174 hp (17 dmg)](../../res/toxtricity_07.png)

```py
from src.max_utils import mult
0.5 * 20 * (224 + 15) / ((181 + 15) * 0.7903) * 1.2 * 1.2 * 2 * 0.45
mult(17, _)
```

```
(0.8001384369027326, 0.8501470892091534)
```

Attack CPM range: `0.800139` - `0.850147`

## HP tests

> 🛠️ Dev note: No proper HP tests were done this time. The HP value of `100k` was obtained directly from [Defense verification tests](#defense-verification-tests), which was the only *decently pretty* value that fulfilled the tests done on that section. This was the same aproach used on early HP testing.

## Defense verification tests

> 📝 Note: Using `0.9` Defense CPM and `100k` total HP.

---

**Lvl50 15atk Zamazenta (Metal Claw, Behemoth Bash) + Lvl50 15atk Excadrill (Lv3 Max Quake, Mud Shot), Sunny, FB4, 5 helpers** ([battle](https://youtu.be/aExVyUgir0s))

Attacks damage:
- Metal Claw: `5` dmg
- Behemoth Bash: `113` dmg
- Max Quake: `1370` dmg
- Mud Shot: `16` dmg

```py
# Metal Claw
0.5 * 6 * ((250 + 15) * 0.8403) / ((140 + 15) * 0.9) * 1.2 * 0.625 * 1.1 * 1.187
floor(_) + 1

# Behemoth Bash
0.5 * 143.75 * ((250 + 15) * 0.8403) / ((140 + 15) * 0.9) * 1.2 * 0.625 * 1.1 * 1.187
floor(_) + 1

# Max Quake
0.5 * 350 * ((255 + 15) * 0.8403) / ((140 + 15) * 0.9) * 1.2 * 2.56 * 1.2 * 1.1 * 1.187
floor(_) + 1

# Mud Shot
0.5 * 4 * ((255 + 15) * 0.8403) / ((140 + 15) * 0.9) * 1.2 * 2.56 * 1.2 * 1.1 * 1.187
floor(_) + 1
```

```
5
113
1370
16
```

Segments sequence:
- Segments #1 to #3:
  - 90* Metal Claw
  - 2 Max Quake
- Segments #4 & #5:
  - 2 Max Quake
- Segment #6:
  - 6 Mud Shot
- Segments #7 to #9:
  - 3 Mud Shot
  - 71* Metal Claw
  - 2 Max Quake
- Segments #10 & #11:
  - 2 Max Quake
- Segments #12 to #14:
  - 2 Max Quake
- Segment #15:
  - 22 Mud Shot
- Segments #16 to #18:
  - 34 Mud Shot
  - 26* Metal Claw
  - 2 Behemoth Bash
  - 2 Max Quake
- Segments #19 & #20:
  - 1 Max Quake
- Segments #21 & #22:
  - 2 Max Quake
- Segment #23:
  - 8 Mud Shot
  - 24 Metal Claw

> 🛠️ Dev note: The (*) indicate the number could be +1 higher (because as a duo you can collect up to 101 max energy during a round). To make the tests fit perfectly, we had to add 1 or 2 extra Metal Claw to the mix.

```py
from src.max_utils import seg
dmg = (5, 113, 1370, 16)
print(seg(dmg, (90, 0, 2, 0), 1000))
print(seg(dmg, (90, 0, 4, 0), 1000))
print(seg(dmg, (90, 0, 4, 6), 1000))
print(seg(dmg, (162, 0, 6, 9), 1000)) # +1 extra MC
print(seg(dmg, (162, 0, 8, 9), 1000))
print(seg(dmg, (162, 0, 10, 9), 1000))
print(seg(dmg, (162, 0, 10, 31), 1000))
print(seg(dmg, (188, 2, 12, 65), 1000))
print(seg(dmg, (188, 2, 13, 65), 1000))
print(seg(dmg, (188, 2, 15, 65), 1000))
print(seg(dmg, (212, 2, 15, 73), 1000))
```

```
Seg: 3 | Extra: 190 dmg | Total: 3190 dmg
Seg: 5 | Extra: 930 dmg | Total: 5930 dmg
Seg: 6 | Extra: 26 dmg | Total: 6026 dmg
Seg: 9 | Extra: 174 dmg | Total: 9174 dmg
Seg: 11 | Extra: 914 dmg | Total: 11914 dmg
Seg: 14 | Extra: 654 dmg | Total: 14654 dmg
Seg: 15 | Extra: 6 dmg | Total: 15006 dmg
Seg: 18 | Extra: 646 dmg | Total: 18646 dmg
Seg: 20 | Extra: 16 dmg | Total: 20016 dmg
Seg: 22 | Extra: 756 dmg | Total: 22756 dmg
Seg: 23 | Extra: 4 dmg | Total: 23004 dmg
```

All the segments flip at the expected moment ✔️
