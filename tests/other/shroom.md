# Max Mushroom bonus

Max Mushroom description states that *it **doubles** the damage your Pokémon deal in Max Battles*, but how does it double the damage? In this section we will covers several possibilities for Max Mushroom boost and put them to the test to see which one is correct in every possible scenario.

The possibilites are: `floor(2 * dmg) + 1`, `floor(2 * dmg) + 2`, `2 * floor(dmg) + 1`, `2 * floor(dmg) + 2`. We came up with only these 4 possiblities, as we have to double the main source of damage, leaving us with two options, multiply by `2` inside or outside the `floor` function, and optionally consider the `+ 1` term to be doubled as well or not, adding the other two options.

For each test, the symbol 💚 indicates the formula was successful and the symbol 💔 indicates the formula failed.

## Summary

The function `2 * floor(_) + 2`, or more precisely `2 * (floor(_) + 1)`, is the only one able to reproduce all the tests. This means, the Max Mushroom boost doubles the entire damage output, as if you were doing 2 attacks at the same time.

## Tests

**Lvl40 15atk Excadrill (Mud Shot) vs Rookidee (T1), NWB, NFB, T4 helpers** ([battle](https://www.youtube.com/watch?v=sqTjH5wlc6M&list=PLNBtbhpo4y2qTTY30CbyMVOxznpiyfBUF&index=2))

Real output damage: `40`

```python
>>> 0.5 * 4 * ((255 + 15) * 0.7903) / ((67 + 15) * 0.15) * 1.2 * 0.390625 * 1.2
19.516554878048783
>>> dmg = _
>>> floor(2 * dmg) + 1
40
>>> floor(2 * dmg) + 2
41
>>> 2 * floor(dmg) + 1
39
>>> 2 * floor(dmg) + 2
40
```

- `floor(2 * dmg) + 1` = `40` 💚
- `floor(2 * dmg) + 2` = `41` 💔
- `2 * floor(dmg) + 1` = `39` 💔
- `2 * floor(dmg) + 2` = `40` 💚

---

**Lvl40 15atk Excadrill (Mud Shot) vs Sobble (T1), NWB, NFB, 2 helpers** ([battle](https://www.youtube.com/watch?v=HvUw3ArgogU&list=PLNBtbhpo4y2qTTY30CbyMVOxznpiyfBUF&index=4))

Real output damage: `84`

```python
>>> 0.5 * 4 * ((255 + 15) * 0.7903) / ((79 + 15) * 0.15) * 1.2 * 1.15
41.76819574468085
>>> dmg = _
>>> floor(2 * dmg) + 1
84
>>> floor(2 * dmg) + 2
85
>>> 2 * floor(dmg) + 1
83
>>> 2 * floor(dmg) + 2
84
```

- `floor(2 * dmg) + 1` = `84` 💚
- `floor(2 * dmg) + 2` = `85` 💔
- `2 * floor(dmg) + 1` = `83` 💔
- `2 * floor(dmg) + 2` = `84` 💚

---

**Lvl40 14atk Rillaboom (Scratch) vs Gastly (T1), NWB, NFB, 3 helpers** ([battle](https://www.youtube.com/watch?v=ZmObrVYczUk&list=PLNBtbhpo4y2qTTY30CbyMVOxznpiyfBUF&index=3))

Real output damage: `46`

```python
>>> 0.5 * 6 * ((239 + 14) * 0.7903) / ((67 + 15) * 0.15) * 0.390625 * 1.17
22.288176733993904
>>> dmg = _
>>> floor(2 * dmg) + 1
45
>>> floor(2 * dmg) + 2
46
>>> 2 * floor(dmg) + 1
45
>>> 2 * floor(dmg) + 2
46
```

- `floor(2 * dmg) + 1` = `45` 💔
- `floor(2 * dmg) + 2` = `46` 💚
- `2 * floor(dmg) + 1` = `45` 💔
- `2 * floor(dmg) + 2` = `46` 💚

---

**Snorlax (Yawn)** ([battle](https://youtube.com/shorts/TS_uvoueQSA))

Real output damage: `2`

```python
>>> dmg = 0
>>> floor(2 * dmg) + 1
1
>>> floor(2 * dmg) + 2
2
>>> 2 * floor(dmg) + 1
1
>>> 2 * floor(dmg) + 2
2
```

- `floor(2 * dmg) + 1` = `1` 💔
- `floor(2 * dmg) + 2` = `2` 💚
- `2 * floor(dmg) + 1` = `1` 💔
- `2 * floor(dmg) + 2` = `2` 💚
