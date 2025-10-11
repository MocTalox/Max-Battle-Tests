# Eternatus Eternamax

Eternatus Eternamax was available in T6 Dynamax Battles on August 17th in-person on Anaheim during the *2025 Pokémon World Championships Celebration* event. Later it became available on August 23rd and 24th globaly during the *Go Fest: Max Finale* event. No tests were done on the in-person event, but some analysis revealed that the stats remained the same during both events.

## Summary

Eternatus Eternamax has an Attack CPM value in the range `0.674608` - `0.675085`, a HP value of `60k` and a Defense CPM value in the range `0.749085` - `0.753205`, which means it has a CPM of `0.75` and AtkMult of `0.9`:

Stats     | Values
:-------- | :------
HP        | `60k`
CPM       | `0.75`
*AtkMult* | `0.9`
*DefMult* | `1.0`
*AtkCPM*  | `0.675`
*DefCPM*  | `0.75`

## Attack CPM tests

**Spread NWB Dynamax Cannon (x2) vs Lvl50 15/12/13 Zamazenta**

Health: [118/172 hp (57 dmg each)](../../res/eternatus_01.png)

> 📝 Note: Lvl3 Max Guard gives +60 base HP.

```py
from src.max_utils import mult
0.5 * 215 * (251 + 15) / ((292 + 12) * 0.8403) * 1.2 * 0.625
mult(57, _)
```

```
(0.6670288372093023, 0.6789400664451827)
```

Attack CPM range: `0.667029` - `0.678940`

---

**Target NWB Flamethrower vs Lvl50 15/15/15 Blissey**

Health: 353/429 hp (76 dmg)

```py
from src.max_utils import mult
0.5 * 65 * (251 + 15) / ((169 + 15) * 0.8403) * 2
mult(76, _)
```

```
(0.6706847888953152, 0.6796272527472528)
```

Attack CPM range: `0.670685` - `0.679627`

---

**Spread NWB Dynamax Cannon vs Lvl35 12/15/13 Venusaur**

Health: [4/154 hp (150 dmg)](../../res/eternatus_02.png)

```py
from src.max_utils import mult
0.5 * 215 * (251 + 15) / ((189 + 15) * 0.761563838) * 1.2
mult(150, _)
```

```
(0.6746078690869033, 0.6791354386780906)
```

Attack CPM range: `0.674608` - `0.679135`

---

**Spread NWB Hyper Beam vs Lvl43 15/12/15 Blissey**

Health: [318/411 hp (93 dmg)](../../res/eternatus_03.png)

```py
from src.max_utils import mult
0.5 * 150 * (251 + 15) / ((169 + 12) * 0.8053)
mult(93, _)
```

```
(0.6721732130325814, 0.6794794436090225)
```

Attack CPM range: `0.672174` - `0.679479`

---

**Spread NWB Hyper Beam vs Lvl50 15/14/12 Charizard**

Health: [80/166 hp (86 dmg)](../../res/eternatus_04.png)

```py
from src.max_utils import mult
0.5 * 150 * (251 + 15) / ((173 + 14) * 0.8403)
mult(86, _)
```

```
(0.6695021804511279, 0.6773786766917294)
```

Attack CPM range: `0.669503` - `0.677378`

---

**Target (dodged 70%) NWB Hyper Beam vs Lvl40 13/14/14 Moltres**

Health: [121/174 hp (53 dmg)](../../res/eternatus_05.png)

```py
from src.max_utils import mult
0.5 * 150 * (251 + 15) / ((181 + 14) * 0.7903) * 2 * 0.3
mult(53, _)
```

```
(0.669477192982456, 0.6823517543859648)
```

Attack CPM range: `0.669478` - `0.682351`

---

**Spread NWB Sludge Bomb vs Lvl44 13/15/14 Gengar**

Health: [109/136 hp (27 dmg)](../../res/eternatus_06.png)

```py
from src.max_utils import mult
0.5 * 85 * (251 + 15) / ((149 + 15) * 0.8103) * 1.2 * 0.390625
mult(27, _)
```

```
(0.6520053923042902, 0.6770825227775322)
```

Attack CPM range: `0.652006` - `0.677082`

---

**Spread NWB Sludge Bomb vs Lvl43 15/15/13 Rillaboom**

Health: [91/191 hp (100 dmg)](../../res/eternatus_07.png)

```py
from src.max_utils import mult
0.5 * 85 * (251 + 15) / ((168 + 15) * 0.8053) * 1.2 * 1.6
mult(100, _)
```

```
(0.6721592630473242, 0.6789487505528528)
```

Attack CPM range: `0.672160` - `0.678948`

---

**Spread NWB Sludge Bomb vs Lvl40 14/14/12 Venusaur**

Health: [101/159 hp (58 dmg)](../../res/eternatus_08.png)

```py
from src.max_utils import mult
0.5 * 85 * (251 + 15) / ((189 + 14) * 0.7903) * 1.2
mult(58, _)
```

```
(0.6740794117647059, 0.6859053663570691)
```

Attack CPM range: `0.674080` - `0.685905`

---

**Spread NWB Sludge Bomb vs Lvl40 15/13/12 Excadrill**

Health: [180/200 hp (20 dmg)](../../res/eternatus_09.png)

```py
from src.max_utils import mult
0.5 * 85 * (251 + 15) / ((129 + 13) * 0.7903) * 1.2 * 0.244140625
mult(20, _)
```

```
(0.6437867921568629, 0.6776703075335399)
```

Attack CPM range: `0.643787` - `0.677670`

---

**Target (dodged 55%) Sunny Flamethrower vs Lvl40 15/12/14 Inteleon**

Health: [113/146 hp (33 dmg)](../../res/eternatus_10.png)

```py
from src.max_utils import mult
0.5 * 65 * (251 + 15) / ((142 + 12) * 0.7903) * 0.625 * 1.2 * 2 * 0.45
mult(33, _)
```

```
(0.6674118458539511, 0.688268466036887)
```

Attack CPM range: `0.667412` - `0.688268`

---

**Spread Partly Cloudy Hyper Beam vs Lvl30 13/15/11 Machamp**

Health: [32/159 hp (127 dmg)](../../res/eternatus_11.png)

```py
from src.max_utils import mult
0.5 * 150 * (251 + 15) / ((159 + 15) * 0.7317) * 1.2
mult(127, _)
```

```
(0.6700831578947368, 0.6754012781954887)
```

Attack CPM range: `0.670084` - `0.675401`

---

**Spread NWB Dynamax Cannon vs Lvl40 12/14/15 Metagross**

Health: [86/162 hp (76 dmg)](../../res/eternatus_12.png)

```py
from src.max_utils import mult
0.5 * 215 * (251 + 15) / ((228 + 14) * 0.7903) * 1.2 * 0.625
mult(76, _)
```

```
(0.6688323133414933, 0.6777500775193799)
```

Attack CPM range: `0.668833` - `0.677750`

---

**Target NWB Dynamax Cannon vs Lvl40 15/13/15 Zamazenta**

Health: [102/163 hp (121 dmg)](../../res/eternatus_13.png)

> 📝 Note: Lvl3 Max Guard gives +60 base HP.

```py
from src.max_utils import mult
0.5 * 215 * (251 + 15) / ((292 + 13) * 0.7903) * 1.2 * 0.625 * 2
mult(121, _)
```

```
(0.6743598531211751, 0.6799795185638515)
```

Attack CPM range: `0.674360` - `0.679979`

---

**Spread Cloudy Sludge Bomb vs Lvl30 14/14/12 Venusaur**

Health: [73/147 hp (74 dmg)](../../res/eternatus_14.png)

```py
from src.max_utils import mult
0.5 * 85 * (251 + 15) / ((189 + 14) * 0.7317) * 1.2 * 1.2
mult(74, _)
```

```
(0.6660684984520125, 0.6751927244582044)
```

Attack CPM range: `0.666069` - `0.675192`

---

**Spread NWB Dynamax Cannon vs Lvl30 15/14/15 Snorlax**

Health: [79/252 hp (173 dmg)](../../res/eternatus_15.png)

```py
from src.max_utils import mult
0.5 * 215 * (251 + 15) / ((169 + 14) * 0.7317) * 1.2
mult(173, _)
```

```
(0.6711834586466165, 0.6750856880573527)
```

Attack CPM range: `0.671184` - `0.675085`

---

**Target Cloudy Sludge Bomb vs Lvl30 15/14/15 Snorlax**

Health: [87/252 hp (165 dmg)](../../res/eternatus_16.png)

```py
from src.max_utils import mult
0.5 * 85 * (251 + 15) / ((169 + 14) * 0.7317) * 1.2 * 1.2 * 2
mult(165, _)
```

```
(0.6744735736399825, 0.6785862173816897)
```

Attack CPM range: `0.674474` - `0.678586`

## HP tests

Hits for first segment:
- [75 hits](https://youtu.be/nE_TCHLM0Tk)
- 300 hits
- 150 hits
- 120 hits
- 200 hits

> ↩️ Test references on [Defense CPM tests](#defense-cpm-tests).

```py
from src.hp_test import hp_lcm
hp_lcm(10000, [75, 300, 150, 120, 200])
```

```
[599, 600]
```

HP value: `600` (segment), `60k` (total)

## Defense CPM tests

**Lvl50 15atk Zamazenta (Metal Claw, Behemoth Bash(+3)) + Lvl50 15atk Latios (Lvl3 Max Wyrmwind, Dragon Breath), NWB, FB4, 4 helpers, Blade x5, Shroom** ([battle](https://youtu.be/nE_TCHLM0Tk))

Segments sequence:
- Segment #1:
  - 75 Metal Claw
- Segment #2:
  - 5 Metal Claw
  - 4 Behemoth Bash
- Segments #3 & #4:
  - 6 Metal Claw
  - 2 Max Wyrmwind
- Segments #5 & #6:
  - 2 Max Wyrmwind
- Segments #7 & #8:
  - 2 Max Wyrmwind
- Segment #9:
  - 8 Dragon Breath

> 📝 Note: Behemoth Bash power at T3 of Go Pass: Max Finale was 143.75 (+15%).

> 📝 Note: Blade Boost bonus at T3 of Go Pass: Max Finale was x5 times effective (+25%).

```py
# Use this code in src/def_test.py
atk_stats = []
atk_stats.append([6, 250, 15, 0.8403, 1.2, 1.0, 1.0])
atk_stats.append([143.75, 250, 15, 0.8403, 1.2, 1.0, 1.0])
atk_stats.append([350, 268, 15, 0.8403, 1.2, 1.6, 1.0])
atk_stats.append([6, 268, 15, 0.8403, 1.2, 1.6, 1.0])
def_stats = [60000, 505, 1]
bonus = [1.1, 1.18, 1.25]
atk_seq = [0] * 80 + [1] * 4 + [0] * 6 + [2] * 6 + [3] * 8
# Shroom flag -> True
```

Attacks Damage:
- Metal Claw: `8`
- Behemoth Bash: `160`
- Max Wyrmwind: `664` or `666`
- Dragon Breath: `12`

Defense CPM range: `0.749085` - `0.753205`

> 📝 Note: Using `60k` total HP.

---

**Lvl35 15atk & 14atk Excadrill (Mud Shot), NWB, FB4, 1 helper**

First segment: 200 hits (3 dmg)

> 🛠️ Dev note: Included to reference HP tests. Too lazy to document, because results were poo 💩

---

**Lvl40 15atk & 14atk Blissey (Pound), NWB, FB4, 0 helpers**

First segment: 300 hits (2 dmg)

> 🛠️ Dev note: Included to reference HP tests. Too lazy to document, because results were poo 💩

---

**Lvl50 15atk Zacian (Metal Claw), NWB, 40 helpers**

First segment: 150 hits (4 dmg)

> 🛠️ Dev note: Included to reference HP tests. Too lazy to document, because results were poo 💩

---

**Lvl50 15atk Zacian (Metal Claw), NWB, 40 helpers, Blade**

First segment: 120 hits (5 dmg)

> 🛠️ Dev note: Included to reference HP tests. Too lazy to document, because results were poo 💩
