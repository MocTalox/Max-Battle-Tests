# Eternatus Eternamax

Eternatus Eternamax was available in T6 Dynamax Battles on August 17th in-person on Anaheim during the *2025 Pokémon World Championships Celebration* event. Later it became available on August 23rd and 24th globaly during the *Go Fest: Max Finale* event. No tests were done on the in-person event, but some analysis revealed that the stats remained the same during both events.

## Result

Eternatus Eternamax has an AtkCPM in the range `0.674608` - `0.675086`, a HP value of `60k` and a DefCPM in the range `0.749085` - `0.753205`, which means it has a CPM of `0.75` and AtkMult of `0.9`:

- HP: `60k`
- CPM: `0.75`
- AtkMult: `0.9`
- DefMult: `1.0`
- AtkCPM: `0.675`
- DefCPM: `0.75`

## Attack CPM tests

**Spread NWB Dynamax Cannon (x2) vs Lvl50 15/12/13 Crowned Shield Zamazenta**

Health: [118/172 hp (57 dmg each)](../../res/eternatus_01.png)

*Note: Lvl3 Max Guard gives +60 base hp*

```python
>>> 0.5 * 215 * (251 + 15) / ((292 + 12) * 0.8403) * 1.2 * 0.625
83.95439128882542
>>> from src.max_utils import mult
>>> mult(57, _)
(0.6670288372093023, 0.6789400664451827)
```

> AtkCPM range = `0.667028` - `0.678940`

---

**Target NWB Flamethrower vs Lvl50 15/15/15 Blissey**

Health: 353/429 hp (76 dmg)

```python
>>> 0.5 * 65 * (251 + 15) / ((169 + 15) * 0.8403) * 2
111.82600417035323
>>> from src.max_utils import mult
>>> mult(76, _)
(0.6706847888953152, 0.6796272527472528)
```

> AtkCPM range = `0.670685` - `0.679627`

---

**Spread NWB Dynamax Cannon vs Lvl35 12/15/13 Venusaur**

Health: [4/154 hp (150 dmg)](../../res/eternatus_02.png)

```python
>>> 0.5 * 215 * (251 + 15) / ((189 + 15) * 0.761563838) * 1.2
220.86905123368157
>>> from src.max_utils import mult
>>> mult(150, _)
(0.6746078690869033, 0.6791354386780906)
```

> AtkCPM range = `0.674608` - `0.679135`

---

**Spread NWB Hyper Beam vs Lvl43 15/12/15 Blissey**

Health: [318/411 hp (93 dmg)](../../res/eternatus_03.png)

```python
>>> 0.5 * 150 * (251 + 15) / ((169 + 12) * 0.8053)
136.86948277056766
>>> from src.max_utils import mult
>>> mult(93, _)
(0.6721732130325814, 0.6794794436090225)
```

> AtkCPM range = `0.672173` - `0.679479`

---

**Spread NWB Hyper Beam vs Lvl50 15/14/12 Charizard**

Health: [80/166 hp (86 dmg)](../../res/eternatus_04.png)

```python
>>> 0.5 * 150 * (251 + 15) / ((173 + 14) * 0.8403)
126.96000473474905
>>> from src.max_utils import mult
>>> mult(86, _)
(0.6695021804511279, 0.6773786766917294)
```

> AtkCPM range = `0.669502` - `0.677379`

---

**Target (dodged 70%) NWB Hyper Beam vs Lvl40 13/14/14 Moltres**

Health: [121/174 hp (53 dmg)](../../res/eternatus_05.png)

```python
>>> 0.5 * 150 * (251 + 15) / ((181 + 14) * 0.7903) * 2 * 0.3
77.67254888601214
>>> from src.max_utils import mult
>>> mult(53, _)
(0.669477192982456, 0.6823517543859648)
```

> AtkCPM range = `0.669477` - `0.682352`

---

**Spread NWB Sludge Bomb vs Lvl44 13/15/14 Gengar**

Health: [109/136 hp (27 dmg)](../../res/eternatus_06.png)

```python
>>> 0.5 * 85 * (251 + 15) / ((149 + 15) * 0.8103) * 1.2 * 0.390625
39.87697081478404
>>> from src.max_utils import mult
>>> mult(27, _)
(0.6520053923042902, 0.6770825227775322)
```

> AtkCPM range = `0.652005` - `0.677082`

---

**Spread NWB Sludge Bomb vs Lvl43 15/15/13 Rillaboom**

Health: [91/191 hp (100 dmg)](../../res/eternatus_07.png)

```python
>>> 0.5 * 85 * (251 + 15) / ((168 + 15) * 0.8053) * 1.2 * 1.6
147.28652187454833
>>> from src.max_utils import mult
>>> mult(100, _)
(0.6721592630473242, 0.6789487505528528)
```

> AtkCPM range = `0.672159` - `0.678949`

---

**Spread NWB Sludge Bomb vs Lvl40 14/14/12 Venusaur**

Health: [101/159 hp (58 dmg)](../../res/eternatus_08.png)

```python
>>> 0.5 * 85 * (251 + 15) / ((189 + 14) * 0.7903) * 1.2
84.55976996950089
>>> from src.max_utils import mult
>>> mult(58, _)
(0.6740794117647059, 0.6859053663570691)
```

> AtkCPM range = `0.674079` - `0.685905`

---

**Spread NWB Sludge Bomb vs Lvl40 15/13/12 Excadrill**

Health: [180/200 hp (20 dmg)](../../res/eternatus_09.png)

```python
>>> 0.5 * 85 * (251 + 15) / ((129 + 13) * 0.7903) * 1.2 * 0.244140625
29.5128763613568
>>> from src.max_utils import mult
>>> mult(20, _)
(0.6437867921568629, 0.6776703075335399)
```

> AtkCPM range = `0.643787` - `0.677670`

---

**Target (dodged 55%) Sunny Flamethrower vs Lvl40 15/12/14 Inteleon**

Health: [113/146 hp (33 dmg)](../../res/eternatus_10.png)

```python
>>> 0.5 * 65 * (251 + 15) / ((142 + 12) * 0.7903) * 0.625 * 1.2 * 2 * 0.45
47.94640700309434
>>> from src.max_utils import mult
>>> mult(33, _)
(0.6674118458539511, 0.688268466036887)
```

> AtkCPM range = `0.667412` - `0.688268`

---

**Spread Partly Cloudy Hyper Beam vs Lvl30 13/15/11 Machamp**

Health: [32/159 hp (127 dmg)](../../res/eternatus_11.png)

```python
>>> 0.5 * 150 * (251 + 15) / ((159 + 15) * 0.7317) * 1.2
188.0363631222519
>>> from src.max_utils import mult
>>> mult(127, _)
(0.6700831578947368, 0.6754012781954887)
```

> AtkCPM range = `0.670083` - `0.675401`

---

**Spread NWB Dynamax Cannon vs Lvl40 12/14/15 Metagross**

Health: [86/162 hp (76 dmg)](../../res/eternatus_12.png)

```python
>>> 0.5 * 215 * (251 + 15) / ((228 + 14) * 0.7903) * 1.2 * 0.625
112.13573044235739
>>> from src.max_utils import mult
>>> mult(76, _)
(0.6688323133414933, 0.6777500775193799)
```

> AtkCPM range = `0.668832` - `0.677750`

---

**Target NWB Dynamax Cannon vs Lvl40 15/13/15 Crowned Shield Zamazenta**

Health: [102/163 hp (121 dmg)](../../res/eternatus_13.png)

*Note: Lvl3 Max Guard gives +60 base hp*

```python
>>> 0.5 * 215 * (251 + 15) / ((292 + 13) * 0.7903) * 1.2 * 0.625 * 2
177.94653617738024
>>> from src.max_utils import mult
>>> mult(121, _)
(0.6743598531211751, 0.6799795185638515)
```

> AtkCPM range = `0.674360` - `0.679980`

---

**Spread Cloudy Sludge Bomb vs Lvl30 14/14/12 Venusaur**

Health: [73/147 hp (74 dmg)](../../res/eternatus_14.png)

```python
>>> 0.5 * 85 * (251 + 15) / ((189 + 14) * 0.7317) * 1.2 * 1.2
109.59833736268395
>>> from src.max_utils import mult
>>> mult(74, _)
(0.6660684984520125, 0.6751927244582044)
```

> AtkCPM range = `0.666068` - `0.675193`

---

**Spread NWB Dynamax Cannon vs Lvl30 15/14/15 Snorlax**

Health: [79/252 hp (173 dmg)](../../res/eternatus_15.png)

```python
>>> 0.5 * 215 * (251 + 15) / ((169 + 14) * 0.7317) * 1.2
256.26376482344057
>>> from src.max_utils import mult
>>> mult(173, _)
(0.6711834586466165, 0.6750856880573527)
```

> AtkCPM range = `0.671183` - `0.675086`

---

**Target Cloudy Sludge Bomb vs Lvl30 15/14/15 Snorlax**

Health: [87/252 hp (165 dmg)](../../res/eternatus_16.png)

```python
>>> 0.5 * 85 * (251 + 15) / ((169 + 14) * 0.7317) * 1.2 * 1.2 * 2
243.15259546038078
>>> from src.max_utils import mult
>>> mult(165, _)
(0.6744735736399825, 0.6785862173816897)
```

> AtkCPM range = `0.674474` - `0.678586`

## HP tests

Hits for 1st segment:
- [75 hits](https://youtu.be/nE_TCHLM0Tk)
- 300 hits
- 150 hits
- 120 hits
- 200 hits

```python
>>> from src.hp_test import hp_lcm
>>> hp_lcm(10000, [75, 300, 150, 120, 200])
[599, 600]
```

> Expected segment HP: `600` or a multiple.
>
> Expected HP value: `600 * 100` = `60000` (`60k`) or a multiple.

## Defense CPM tests

**Lvl50 15atk Crowned Shield Zamazenta (Metal Claw, Behemoth Bash(+3)) + Lvl50 15atk Latios (Lvl3 Max Wyrmwind, Dragon Breath), NWB, FB4, 4 helpers, Blade x5, Shroom** ([battle](https://youtu.be/nE_TCHLM0Tk))

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

*Note: Behemoth Bash power at T3 of Go Pass: Max Finale was 143.75 (+15%).*

*Note: Blade Boost bonus at T3 of Go Pass: Max Finale was x5 times effective (+25%).*

```python
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

> Attacks Damage:
> - Metal Claw: `8`
> - Behemoth Bash: `160`
> - Max Wyrmwind: `664` or `666`
> - Dragon Breath: `12`
>
> DefCPM Range: `0.749085` - `0.753205`
>
> *Note: Using `60k` total hp.*
