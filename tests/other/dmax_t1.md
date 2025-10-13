# Dynamax T1 Boss

## Summary

Dynamax T1 bosses have an Attack CPM value in the range `0.149998` - `0.150003`, a HP value of `1700` and a Defense CPM value in the range `0.15` - `0.15`, which means it simply has a CPM of `0.15`:

> 🛠️ Dev self-note: Edit the range when defense cpm tests are added.

Stats     | Values
:-------- | :------
HP        | `1700`
CPM       | `0.15`
*AtkMult* | `1.0`
*DefMult* | `1.0`
*AtkCPM*  | `0.15`
*DefCPM*  | `0.15`

## Attack CPM tests

**Drilbur Spread Partly Cloudy Rock Tomb vs Lvl21 13def Abra**

Health: [47/65 hp (18 dmg)](../../res/t1_01.png)

```py
from src.max_utils import mult
0.5 * 65 * (154 + 15) / ((82 + 13) * 0.612157285) * 1.2
mult(18, _)
```

```
(0.14999757476483083, 0.1588209615157032)
```

Attack CPM range: `0.149998` - `0.158820`

---

**Drilbur Spread NWV Drill Run vs Lvl21 14def Abra**

Health: [42/64 hp (22 dmg)](../../res/t1_02.png)

```py
from src.max_utils import mult
0.5 * 85 * (154 + 15) / ((82 + 14) * 0.612157285) * 1.2
mult(22, _)
```

```
(0.14318471824573617, 0.1500030381621998)
```

Attack CPM range: `0.143185` - `0.150003`
