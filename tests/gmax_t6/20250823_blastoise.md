# Blastoise

Blastoise was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Result

Unfortunately no tests were done for Blastoise this time. The aproach has been to approximate the AtkCPM by analysing videos. With a rough estimate of the damage done by the attacks, the results will be less accurate but still enough to give us an idea of the potential stats. This way we found Blastoise has an AtkCPM in the range `0.760839` - `0.794210`, which means it has the same CPM as last time, but the HP value is still unknow:

- CPM: `0.85`
- AtkMult: `0.9`
- AtkCPM: `0.765`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack CPM tests

**Spread NWB Ice Beam vs Lvl50 15/15/15 Crowned Shield Zamazenta** ([battle](https://www.youtube.com/shorts/LKu0I7pRmFg))

Damage: 102 dmg (enraged)

*Note: Enraged damage is x6 on T6 Gigantamax Battles*

```python
>>> 0.5 * 95 * (171 + 15) / ((292 + 15) * 0.8403) * 0.625
21.404930998352146
>>> from src.max_utils import mult
>>> mult(102 / 6, _)
(0.7474913140916809, 0.794209521222411)
```

> AtkCPM range = `0.747491` - `0.794210`

---

**Target (dodged 65%) NWB Flash Cannon vs Lvl50 15/15/15 Crowned Shield Zamazenta** ([battle](https://www.youtube.com/shorts/LKu0I7pRmFg))

Damage: 78 dmg (enraged)

*Note: Enraged damage is x6 on T6 Gigantamax Battles*

```python
>>> 0.5 * 100 * (171 + 15) / ((292 + 15) * 0.8403) * 0.625 * 2 * 0.35
15.772054419838422
>>> from src.max_utils import mult
>>> mult(78 / 6, _)
(0.7608393732718894, 0.8242426543778802)
```

> AtkCPM range = `0.760839` - `0.824242`
