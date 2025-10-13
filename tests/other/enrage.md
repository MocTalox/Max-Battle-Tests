# Enrage Damage

When the boss gets enraged and his attacks get stronger, the game does not include an additional damage multiplier like all other bonuses, instead it multiplies the total output damage by a multiplier, exactly as [Max Mushrooms work](./shroom.md#summary) works, as if it was doing like 3 attacks at the same time:

```
Bonus * (floor(...) + 1)
```

However this `Bonus` value is different for each Max Battle tier.

## Summary

Tier          | Bonus
:------------ | :---:
T1 Dynamax    | 3
T2 Dynamax    | 3
T3 Dynamax    | 9
T4 Dynamax    | 9
T5 Dynamax    | 3
T5 Eternamax  | 6
T6 Gigantamax | 6

## Attack tests

### T1 Dynamax

**Caterpie Enraged Target NWB Struggle vs Lvl40 15/15/15 Metagross**

Health: 156/162 hp (6 dmg)

```py
0.5 * 35 * ((55 + 15) * 0.15) / ((228 + 15) * 0.7903) * 0.625 * 2
floor(_) + 1
6 / _
```

```
3.0
```

Enrage damage bonus: `3`

---

**Caterpie Enraged Spread NWB Struggle vs Lvl30 15/15/15 Chansey**

Health: 355/367 hp (12 dmg)

```py
0.5 * 35 * ((55 + 15) * 0.15) / ((128 + 15) * 0.7317) * 2
floor(_) + 1
12 / _
```

```
3.0
```

Enrage damage bonus: `3`

### T2 Dynamax

**Darumaka Enraged Target NWB Flame Charge vs Lvl40 15/15/15 Metagross**

Health: 27/162 hp (135 dmg)

```py
0.5 * 70 * ((153 + 15) * 0.38) / ((228 + 15) * 0.7903) * 1.2 * 1.6 * 2
floor(_) + 1
135 / _
```

```
3.0
```

Enrage damage bonus: `3`

---

**Darumaka Enraged Target NWB Flame Charge vs Lvl30 15/15/15 Chansey**

Health: 211/367 hp (156 dmg)

```py
0.5 * 70 * ((153 + 15) * 0.38) / ((128 + 15) * 0.7317) * 1.2 * 2
floor(_) + 1
156 / _
```

```
3.0
```

Enrage damage bonus: `3`

---

**Machop Enraged Target Cloudy Cross Chop vs Lvl40 15/15/15 Metagross**

Health: 96/162 hp (66 dmg)

```py
0.5 * 50 * ((137 + 15) * 0.38) / ((228 + 15) * 0.7903) * 1.2 * 1.2 * 2
floor(_) + 1
66 / _
```

```
3.0
```

Enrage damage bonus: `3`

---

**Machop Enraged Target Cloudy Cross Chop vs Lvl30 15/15/15 Chansey**

Health: 175/367 hp (192 dmg)

```py
0.5 * 50 * ((137 + 15) * 0.38) / ((128 + 15) * 0.7317) * 1.2 * 1.6 * 1.2 * 2
floor(_) + 1
192 / _
```

```
3.0
```

Enrage damage bonus: `3`

---

**Machop Enraged Spread Cloudy Low Sweep vs Lvl30 14/14/15 Metagross**

Health: 119/149 hp (30 dmg)

```py
0.5 * 40 * ((137 + 15) * 0.38) / ((228 + 14) * 0.7317) * 1.2 * 1.2
floor(_) + 1
30 / _
```

```
3.0
```

Enrage damage bonus: `3`

### T3 Dynamax

**Cryogonal Enraged Spread NWB Triple Axel vs Lvl40 15/15/15 Metagross**

Health: 45/162 hp (117 dmg)

```py
0.5 * 60 * ((190 + 15) * 0.5) / ((228 + 15) * 0.7903) * 1.2 * 0.625
floor(_) + 1
117 / _
```

```
9.0
```

Enrage damage bonus: `9`

---

**Cryogonal Enraged Spread NWB Triple Axel vs Lvl30 15/15/15 Chansey**

Health: 43/367 hp (324 dmg)

```py
0.5 * 60 * ((190 + 15) * 0.5) / ((128 + 15) * 0.7317) * 1.2
floor(_) + 1
324 / _
```

```
9.0
```

Enrage damage bonus: `9`

---

**Beldum Enraged Target NWB Iron Head vs Lvl40 14/15/15 Blissey**

Health: [151/403 hp (252 dmg)](../../res/enrage_01.png)

```py
0.5 * 60 * ((96 + 15) * 0.5) / ((169 + 15) * 0.7903) * 1.2 * 2
floor(_) + 1
252 / _
```

```
9.0
```

Enrage damage bonus: `9`

### T4 Dynamax

**Duraludon Enraged Spread NWB Dragon Claw vs Lvl50 15/15/14 Zacian**

Damage: [45 dmg](https://youtu.be/BNwF7ULnsDo?t=453)

```py
0.5 * 45 * ((239 + 15) * 0.6) / ((240 + 15) * 0.8403) * 1.2 * 0.244140625
floor(_) + 1
45 / _
```

```
9.0
```

Enrage damage bonus: `9`

### T5 Dynamax

**Moltres Enraged Spread NWB Ancient Power vs Lvl50 15/15/15 Zamazenta**

Damage: [60 dmg](https://youtu.be/JKGMW-iiutQ?t=413)

```py
0.5 * 70 * ((251 + 15) * 1.4) / ((292 + 15) * 0.8403) * 0.390625
floor(_) + 1
60 / _
```

```
3.0
```

Enrage damage bonus: `3`

### T5 Eternamax

**Eternatus Enraged Spread NWB Sludge Bomb vs Lvl40 15/15/15 Zamazenta**

Damage: [90 dmg](https://youtu.be/C0K5hUTWr7s?t=556)

```py
0.5 * 85 * ((251 + 15) * 0.675) / ((292 + 15) * 0.7903) * 1.2 * 0.390625
floor(_) + 1
90 / _
```

```
6.0
```

Enrage damage bonus: `6`

---

**Eternatus Enraged Target NWB Sludge Bomb vs Lvl50 14/15/14 Excadrill**

Damage: [222 dmg](https://youtu.be/oGl8aijjYrY?t=424)

```py
0.5 * 85 * ((251 + 15) * 0.675) / ((129 + 15) * 0.8403) * 1.2 * 0.244140625 * 2
floor(_) + 1
222 / _
```

```
6.0
```

Enrage damage bonus: `6`

### T6 Gigantamax

*Tests done will be uploaded soon!*
