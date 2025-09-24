# Butterfree

Butterfree was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Result

Butterfree has the same CPM as last time, but the HP value is still unknow:

- CPM: `0.85`
- AtkMult: `0.9`
- AtkCPM: `0.765`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack verification tests

**Spread NWB Bug Buzz vs Lvl20 12/14/15 Latias**

Health: [40/122 hp (82 dmg)](../../res/butterfree_01.png)

```python
>>> 0.5 * 95 * ((167 + 15) * 0.765) / ((246 + 14) * 0.5974) * 1.2 * 1.6
81.75025108804819
>>> floor(_) + 1
82
```

> Using `AtkCPM = 0.765`, the damage **is correct!**
