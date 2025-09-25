# Cinderace

Cinderace was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Result

Cinderace has the same CPM as last time, but the HP value is still unknow:

- CPM: `0.8`
- AtkMult: `0.9`
- AtkCPM: `0.72`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack verification tests

**Spread NWB Flamethrower vs Lvl40 11/15/14 Kabutops**

Health: [115/133 hp (18 dmg)](../../res/cinderace_01.png)

```python
>>> 0.5 * 65 * ((238 + 15) * 0.72) / ((186 + 15) * 0.7903) * 1.2 * 0.390625
17.469867856717926
>>> floor(_) + 1
18
```

> Using `AtkCPM = 0.72`, the damage **is correct!**

---

**Spread NWB Flamethrower vs Lvl50 13/13/13 Crowned Sword Zacian**

Health: [118/172 hp (54 dmg)](../../res/cinderace_02.png)

```python
>>> 0.5 * 65 * ((238 + 15) * 0.72) / ((240 + 13) * 0.8403) * 1.2 * 1.6
53.46661906461978
>>> floor(_) + 1
54
```

> Using `AtkCPM = 0.72`, the damage **is correct!**
