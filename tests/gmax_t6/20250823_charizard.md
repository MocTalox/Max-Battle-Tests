# Charizard

Charizard was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Result

Charizard has the same CPM as last time, but the HP value is still unknow:

- CPM: `0.85`
- AtkMult: `0.9`
- AtkCPM: `0.765`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack verification tests

**Spread NWB Overheat vs Lvl50 15/15/15 Blissey**

Health: 315/429 hp (114 dmg)

```python
>>> 0.5 * 160 * ((223 + 15) * 0.765) / ((169 + 15) * 0.8403) * 1.2
113.04658274218832
>>> floor(_) + 1
114
```

> Using `AtkCPM = 0.765`, the damage **is correct!**
