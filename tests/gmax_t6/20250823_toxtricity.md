# Toxtricity

Toxtricity was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Result

Toxtricity got a CPM nerf, it has an AtkCPM in the range `0.807268` - `0.813344`, which means it has a CPM of `0.9` and AtkMult of `0.9`. However the HP value is still unknow:

- CPM: `0.9`
- AtkMult: `0.9`
- AtkCPM: `0.81`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack CPM tests

**Spread Cloudy Power-Up Punch vs Lvl27 14/14/15 Excadrill**

Health: [84/178 hp (94 dmg)](../../res/toxtricity_01.png)

```python
>>> 0.5 * 50 * (224 + 15) / ((129 + 14) * 0.694143653) * 1.6 * 1.2
115.57229670985151
>>> from src.max_utils import mult
>>> mult(94, _)
(0.8046911123820608, 0.8133437049883195)
```

> AtkCPM range = `0.804691` - `0.813344`

---

**Spread NWB Wild Charge vs Lvl27 14/14/15 Excadrill**

Health: [136/178 hp (42 dmg)](../../res/toxtricity_02.png)

```python
>>> 0.5 * 90 * (224 + 15) / ((129 + 14) * 0.694143653) * 1.2 * 0.390625
50.78860695257147
>>> from src.max_utils import mult
>>> mult(42, _)
(0.8072676621803688, 0.8269571173554998)
```

> AtkCPM range = `0.807268` - `0.826957`

---

**Spread NWB Wild Charge vs Lvl44 15/11/15 Eternatus**

Health: [189/229 hp (40 dmg)](../../res/toxtricity_03.png)

```python
>>> 0.5 * 90 * (224 + 15) / ((192 + 11) * 0.8103) * 1.2 * 0.625
49.03766712930624
>>> from src.max_utils import mult
>>> mult(40, _)
(0.7953070013947001, 0.8156994886099488)
```

> AtkCPM range = `0.795307` - `0.815699`

---

**Spread NWB Wild Charge vs Lvl40 12/14/15 Metagross**

Health: [107/162 hp (55 dmg)](../../res/toxtricity_04.png)

```python
>>> 0.5 * 90 * (224 + 15) / ((228 + 14) * 0.7903) * 1.2
67.48143554649714
>>> from src.max_utils import mult
>>> mult(55, _)
(0.8002200836820085, 0.8150389741205641)
```

> AtkCPM range = `0.800220` - `0.815039`

---

**Spread Cloudy Power-Up Punch vs Lvl40 15/12/14 Latias**

Health: [143/161 hp (18 dmg)](../../res/toxtricity_05.png)

```python
>>> 0.5 * 50 * (224 + 15) / ((246 + 12) * 0.7903) * 0.625 * 1.2
21.97796538847479
>>> from src.max_utils import mult
>>> mult(18, _)
(0.7735019916317992, 0.819002108786611)
```

> AtkCPM range = `0.773502` - `0.819002`

---

**Target (dodged 60%) Cloudy Acid Spray vs Lvl43 15/15/13 Rillaboom**

Health: [166/191 hp (25 dmg)](../../res/toxtricity_06.png)

```python
>>> 0.5 * 20 * (224 + 15) / ((168 + 15) * 0.8053) * 1.2 * 1.6 * 1.2 * 2 * 0.4
29.892454293583697
>>> from src.max_utils import mult
>>> mult(25, _)
(0.8028782034518829, 0.8363314619290446)
```

> AtkCPM range = `0.802878` - `0.836331`

---

**Target (dodged 55%) Cloudy Acid Spray vs Lvl40 13/14/14 Moltres**

Health: [157/174 hp (17 dmg)](../../res/toxtricity_07.png)

```python
>>> 0.5 * 20 * (224 + 15) / ((181 + 15) * 0.7903) * 1.2 * 1.2 * 2 * 0.45
19.996539676227318
>>> from src.max_utils import mult
>>> mult(17, _)
(0.8001384369027326, 0.8501470892091534)
```

> AtkCPM range = `0.800138` - `0.850147`
