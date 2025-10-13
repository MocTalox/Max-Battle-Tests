# Notes

## Information

### Damage formula

```
0.5 * Power * ((BaseAtk + IvAtk) * AtkCPM) / ((BaseDef + IvDef) * DefCPM) * STAB * Type * Weather * Friendship * Helpers * Blade * Target * Dodge
```

The `Friendship`, `Helpers` and `Blade` only affect your damage, and the `Target` and `Dodge` only affect the boss damage. Boss IVs are 100%, so for your damage to the boss `IvDef = 15` and for the boss damage to you `IvAtk = 15`.

```
Bonus * (floor(_) + 1)
```

The `_` denotes the output from the previous formula. The `Bonus` is an extra modifier that is `2` for your damage when using Shroom and `3`, `6` or `9` for the boss damage when it gets enraged (value depends on battle tier).

### Range of values

With this formula u can truncate the values on a range, so to have only 6 decimal digits. The min value is rounded up and the max value ronded down.

```
trunc = lambda x, y : (ceil(x * 1000000) / 1000000, floor(y * 1000000) / 1000000)
```

### CPM list for each level

- Lvl 01: `0.094`
- Lvl 02: `0.16639787`
- Lvl 03: `0.21573247`
- Lvl 04: `0.255720049`
- Lvl 05: `0.290249884`
- Lvl 06: `0.321087599`
- Lvl 07: `0.349212676`
- Lvl 08: `0.375235587`
- Lvl 09: `0.399567276`
- Lvl 10: `0.4225`
- Lvl 11: `0.443107545`
- Lvl 12: `0.462798387`
- Lvl 13: `0.481684953`
- Lvl 14: `0.499858439`
- Lvl 15: `0.517393947`
- Lvl 16: `0.534354329`
- Lvl 17: `0.550792694`
- Lvl 18: `0.56675452`
- Lvl 19: `0.582278907`
- Lvl 20: `0.5974`
- Lvl 21: `0.612157285`
- Lvl 22: `0.626567125`
- Lvl 23: `0.640652955`
- Lvl 24: `0.654435635`
- Lvl 25: `0.667934`
- Lvl 26: `0.68116492`
- Lvl 27: `0.694143653`
- Lvl 28: `0.706884205`
- Lvl 29: `0.719399095`
- Lvl 30: `0.7317`
- Lvl 31: `0.737769485`
- Lvl 32: `0.743789434`
- Lvl 33: `0.749761045`
- Lvl 34: `0.755685508`
- Lvl 35: `0.761563838`
- Lvl 36: `0.767397165`
- Lvl 37: `0.773186505`
- Lvl 38: `0.77893275`
- Lvl 39: `0.784637`
- Lvl 40: `0.7903`
- Lvl 41: `0.7953`
- Lvl 42: `0.8003`
- Lvl 43: `0.8053`
- Lvl 44: `0.8103`
- Lvl 45: `0.8153`
- Lvl 46: `0.8203`
- Lvl 47: `0.8253`
- Lvl 48: `0.8303`
- Lvl 49: `0.8353`
- Lvl 50: `0.8403`
- Lvl 51: `0.8453`
- Lvl 52: `0.8503`
- Lvl 53: `0.8553`
- Lvl 54: `0.8603`
- Lvl 55: `0.8653`

### GoFest Max Finale Behemoth moves bonus

| Bonus Tier | AE Raids | AE Max | Moves |
|:-----------|:--------:|:------:|:-----:|
| Default    | +10%     | +5%    | N/A   |
| Tier 0     | +20%     | +10%   | N/A   |
| Tier 1     | +30%     | +15%   | +5%   |
| Tier 2     | +40%     | +20%   | +10%  |
| Tier 3     | +50%     | +25%   | +15%  |

## WIP-TODO tests

### Venusaur Max Finale - HP tests

Hits for first segment:
- 225 hits
- 300 hits

`lcm(225, 300) = 900`

### Venusaur Max Finale - Defense tests

**Lvl35 15atk & 14atk Excadrill (Mud Shot), NWB, FB4, 1 helper**

First segment: 225 hits (4 dmg)

```
0.5 * 4 * ((255 + 15) * 0.761563838) / ((189 + 15) * 0.85) * 1.2 * 1.1 * 1.1
0.5 * 4 * ((255 + 14) * 0.761563838) / ((189 + 15) * 0.85) * 1.2 * 1.1 * 1.1
```

**Lvl40 15atk & 14atk Blissey (Pound), NWB, FB4, 1 helper**

First segment: 300 hits (3 dmg)

```
0.5 * 6 * ((129 + 15) * 0.7903) / ((189 + 15) * 0.85) * 1.2 * 1.1 * 1.1
0.5 * 6 * ((129 + 14) * 0.7903) / ((189 + 15) * 0.85) * 1.2 * 1.1 * 1.1
```

### Blastoise Max Finale - Defense tests

**Lvl40 15atk Zamazenta (Metal Claw) + Lvl40 15atk Zamazenta (Metal Claw), NWB, FB4, 3 helpers, Shroom**

First segment: 3 * 25 hits (8 dmg) + 25 hits (6 dmg)

```
0.5 * 6 * ((250 + 15) * 0.7903) / ((207 + 15) * 0.85) * 1.2 * 0.625 * 1.1 * 1.17
0.5 * 6 * ((250 + 14) * 0.7317) / ((207 + 15) * 0.85) * 1.2 * 0.625 * 1.1 * 1.17
```

**Lvl30 15atk Venusaur (Vine Wip), NWB, FB4, 2 helpers**

First segment: 108 hits (7 dmg)

```
0.5 * 6 * ((198 + 15) * 0.7317) / ((207 + 15) * 0.85) * 1.2 * 1.6 * 1.1 * 1.15
```

### Other HP/Defense tests

All Saturday \[slow\] (char, blas, venu, geng, snor, mach):
https://youtu.be/1UUrVPDpkSU

Kingler \[slow\]:
https://youtu.be/s7YqEapKSRc

Charizard:
https://youtu.be/BjfVPbptjKw

Gengar:
https://youtu.be/9dg6LpIIi2U
