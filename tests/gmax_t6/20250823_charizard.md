# Charizard

Charizard was available in T6 Gigantamax Battles on August 23rd and 24th globaly during the *Go Fest: Max Finale* event.

## Summary

Charizard has the same CPM as [last time](./20250308_charizard.md), but the HP value is still unknow:

Stats     | Values
:-------- | :------
HP        | `???`
CPM       | `0.85`
*AtkMult* | `0.9`
*DefMult* | `???`
*AtkCPM*  | `0.765`
*DefCPM*  | `???`

It is thought that its HP has been changed since last time as most of the other Gigantamax bosses during this event.

## Attack verification tests

> 📝 Note: Using `0.765` Attack CPM.

---

**Spread NWB Overheat vs Lvl50 15/15/15 Blissey**

Health: 315/429 hp (114 dmg)

```py
0.5 * 160 * ((223 + 15) * 0.765) / ((169 + 15) * 0.8403) * 1.2
floor(_) + 1
```

```
114
```

The damage is the expected ✔️
