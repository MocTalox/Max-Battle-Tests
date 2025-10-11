# Blastoise

Blastoise was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

Unfortunately no Attack CPM tests were done for Blastoise this time. The aproach has been to approximate the Attack CPM value by analysing videos. With a rough estimate of the damage done by the attacks, the results will be less accurate but still enough to give us an idea of the potential stats.

## Summary

Blastoise has an Attack CPM value in the range `0.760840` - `0.794209`, which means it has the same CPM as [last time](./20250308_blastiose.md), but the HP value is still unknow:

Stats     | Values
:-------- | :------
HP        | `???`
CPM       | `0.85`
*AtkMult* | `0.9`
*DefMult* | `???`
*AtkCPM*  | `0.765`
*DefCPM*  | `???`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack CPM tests

**Spread NWB Ice Beam vs Lvl50 15/15/15 Zamazenta** ([battle](https://www.youtube.com/shorts/LKu0I7pRmFg))

Damage: 102 dmg (enraged)

> 📝 Note: Enraged damage is x6 on T6 Gigantamax Battles.

```py
from src.max_utils import mult
0.5 * 95 * (171 + 15) / ((292 + 15) * 0.8403) * 0.625
mult(102 / 6, _)
```

```
(0.7474913140916809, 0.794209521222411)
```

Attack CPM range: `0.747492` - `0.794209`

---

**Target (dodged 65%) NWB Flash Cannon vs Lvl50 15/15/15 Zamazenta** ([battle](https://www.youtube.com/shorts/LKu0I7pRmFg))

Damage: 78 dmg (enraged)

> 📝 Note: Enraged damage is x6 on T6 Gigantamax Battles.

```py
from src.max_utils import mult
0.5 * 100 * (171 + 15) / ((292 + 15) * 0.8403) * 0.625 * 2 * 0.35
mult(78 / 6, _)
```

```
(0.7608393732718894, 0.8242426543778802)
```

Attack CPM range: `0.760840` - `0.824242`
