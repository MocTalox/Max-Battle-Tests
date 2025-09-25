# Rillaboom

Rillaboom was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Result

Rillaboom has the same CPM as last time, but the HP value is still unknow:

- CPM: `1.0`
- AtkMult: `0.9`
- AtkCPM: `0.9`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack verification tests

**Spread Sunny Energy Ball vs Lvl48 11/14/14 Metagross**

Health: [122/169 hp (47 dmg)](../../res/rillaboom_01.png)

```python
>>> 0.5 * 90 * ((239 + 15) * 0.9) / ((228 + 14) * 0.8303) * 1.2 * 0.625 * 1.2
46.07664460620128
>>> floor(_) + 1
47
```

> Using `AtkCPM = 0.9`, the damage **is correct!**

---

**Spread Sunny Grass Knot vs Lvl40 15/12/14 Latias**

Health: [115/161 hp (46 dmg)](../../res/rillaboom_02.png)

```python
>>> 0.5 * 90 * ((239 + 15) * 0.9) / ((246 + 12) * 0.7903) * 1.2 * 0.625 * 1.2
45.40666040861728
>>> floor(_) + 1
46
```

> Using `AtkCPM = 0.9`, the damage **is correct!**

---

**Target (dodged 55%) Sunny Earth Power vs Lvl50 13/13/13 Crowned Sword Zacian**

Health: [79/172 hp (93 dmg)](../../res/rillaboom_03.png)

```python
>>> 0.5 * 100 * ((239 + 15) * 0.9) / ((240 + 13) * 0.8403) * 1.6 * 1.2 * 2 * 0.45
92.90414349477106
>>> floor(_) + 1
93
```

> Using `AtkCPM = 0.9`, the damage **is correct!**

---

**Target NWB Grass Knot vs Lvl50 15/15/15 Metagross**

Health: [96/172 hp (76 dmg)](../../res/rillaboom_04.png)

```python
>>> 0.5 * 90 * ((239 + 15) * 0.9) / ((228 + 15) * 0.8403) * 1.2 * 0.625 * 2
75.56824943472569
>>> floor(_) + 1
76
```

> Using `AtkCPM = 0.9`, the damage **is correct!**

---

**Spread NWB Earth Power vs Lvl40 15/15/15 Blissey**

Health: [324/403 hp (79 dmg)](../../res/rillaboom_05.png)

```python
>>> 0.5 * 100 * ((239 + 15) * 0.9) / ((169 + 15) * 0.7903)
78.60251197949046
>>> floor(_) + 1
79
```

> Using `AtkCPM = 0.9`, the damage **is correct!**

---

**Spread NWB Earth Power vs Lvl31.5 12/15/13 Charizard**

Health: [95/147 hp (52 dmg)](../../res/rillaboom_06.png)

```python
>>> 0.5 * 100 * ((239 + 15) * 0.9) / ((173 + 15) * 0.7407855746190005) * 0.625
51.29510011356439
>>> floor(_) + 1
52
```

> Using `AtkCPM = 0.9`, the damage **is correct!**
