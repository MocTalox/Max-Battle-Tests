# Bugs

## Max Dupe

**Garbodor Quad Battle: NWB, FB4, 11 helpers** ([battle](https://youtu.be/Y_Uvlxegbi0))

With the tests done to [Garbodor during November 1st](/tests/gmax_t6/20251101_garbodor.md) we obtained the exact stats of this boss. However, when testing the following run these stats did not accurately represent the observed segment drops... almost. We are facing the bug known as *Max Dupe*, where max moves sometimes are duplicated as the player uses two max moves on the same turn.

This bug is perfectly observed during the 1st max phase: on the 1st turn the 2nd and 4th player used two max moves at the same time, resulting in them having just *1 Max Moves left* on the 2nd turn while the other two players still had *2 Max Moves left* (displayed on the bottom of the screen), and then been unable to attack during the 3rd turn. With this sequence of attacks (6 max moves on the 1st turn, 4 on the 2nd and 2 on the 3rd) we obtain enough damage to turn the 4th segment during the 2nd turn, but with a regular sequence (4 max moves per turn) the damage would not be enough, which means this bug explains the observed segment drops.

Considering this, the damage stays correct until the 8th cycle. At that point, everything becomes chaotic with barely any segment drop fits the expected damage, but with a nice coincidence: If we were to add exactly the damage of 2 max moves, this issue gets perfectly fixed. Doing so the damage stays correct until nearly the end. So, if you think about this, during max phase #1 the bug happened during the 1st turn, but if this happens during the last turn, you will actually get the duplicate moves while not getting removed from other turns, meaning you could get extra damage for the whole run. This is what we think that happened during max phase #7, it feels it is not a coincidence at all. Finally, one additional max move during the max phase #24 would fix the remaining issues at the end of the run resulting in perfect calculations at the end.

This may sound as a crazy workaround and yes, it shocked us in the research team, but consider the following points:
- The damage calculations per move are right, as if we consider we made a mistake before 8th cycle, the calculated damage from the segment #36 to #82 is exactly 46008, the expected value. The same happens for #36 to #41, #46, #51, #55 and #68.
- We actually did not made a mistake counting the max moves, as it is an extremely simple task with little margin of error and multiple members of the team counted and double checked 2 or 3 times the amount of moves over the whole run.
- The glitch is perfectly observed during max phase #1.

Attacks damage:
- Lvl40 15atk Excadrill
  - Mud Shot: `5` dmg
  - Lv3 Max Quake: `377` dmg
- Lvl40 14atk Excadrill
  - Mud Shot: `5` dmg
  - Lv3 Max Quake: `375` dmg

> 📝 Note: Using `1.4` Defense CPM and `100k` total HP.

```py
# 15atk Mud Shot
0.5 * 4 * ((255 + 15) * 0.7903) / ((164 + 15) * 1.4) * 1.2 * 1.6 * 1.1 * 1.196
floor(_) + 1

# 15atk Max Quake
0.5 * 350 * ((255 + 15) * 0.7903) / ((164 + 15) * 1.4) * 1.2 * 1.6 * 1.1 * 1.196
floor(_) + 1

# 14atk Mud Shot
0.5 * 4 * ((255 + 14) * 0.7903) / ((164 + 15) * 1.4) * 1.2 * 1.6 * 1.1 * 1.196
floor(_) + 1

# 14atk Max Quake
0.5 * 350 * ((255 + 14) * 0.7903) / ((164 + 15) * 1.4) * 1.2 * 1.6 * 1.1 * 1.196
floor(_) + 1
```

Segments sequence:
- Segments #1 & #2:
  - 103 Mud Shot
  - 1 Max Quake (14atk)
  - 5 Max Quake (15atk) # Duplicte 2 on the first turn
- Segments #3 & #4:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #5:
  - 1 Max Quake (14atk)
  - 1 Max Quake (15atk) # Remove 2 on the last turn
- Segment #6:
  - 92 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #7 & #8:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #9 & #10:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #11 & #12:
  - 101 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #13:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #14 & #15:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #16:
  - 91 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #17 & #18:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #19 & #20:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #21 & #22:
  - 101 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #23:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #24 & #25:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #26 & #27:
  - 100 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #28:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #29 & #30:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #31 & #32:
  - 93 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #33:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #34 & #35:
  - 1 Max Quake (14atk)
  - 5 Max Quake (15atk) # Duplicte 2 on the last turn
- Segment #36:
  - 44 Mud Shot
- Segment #37:
  - 47 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #38 & #39:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #40:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #41:
  - 52 Mud Shot
- Segment #42:
  - 50 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #43 & #44:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #45:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #46:
  - 48 Mud Shot
- Segment #47:
  - 45 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segments #48 & #49:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #50:
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #51:
  - 51 Mud Shot
- Segment #52:
  - 145 Mud Shot
  - 2 Max Quake (15atk)
- Segment #53:
  - 3 Max Quake (15atk)
- Segment #54:
  - 3 Max Quake (15atk)
- Segment #55:
  - 51 Mud Shot
- Segment #56:
  - 51 Mud Shot
  - 1 Max Quake (14atk)
  - 3 Max Quake (15atk)
- Segment #57:
  - 1 Max Quake (14atk)
- Segment #58:
  - 92 Mud Shot
  - 1 Max Quake (14atk)
  - 1 Max Quake (15atk)
- Segment #59:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #60:
  - 2 Max Quake (15atk)
- Segment #61:
  - 102 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segments #62 & #63:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #64:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #65:
  - 92 Mud Shot
  - 1 Max Quake (14atk)
  - 1 Max Quake (15atk)
- Segment #66:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #67:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #68:
  - 80 Mud Shot
- Segment #69:
  - 23 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #70:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #71:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #72:
  - 93 Mud Shot
  - 1 Max Quake (15atk)
- Segment #73:
  - 1 Max Quake (14atk)
  - 1 Max Quake (15atk)
- Segment #74:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #75:
  - 101 Mud Shot
  - 3 Max Quake (15atk)
- Segments #76 & #77:
  - 3 Max Quake (15atk)
- Segment #78:
  - 3 Max Quake (15atk)
- Segment #79:
  - 93 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #80:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #81:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #82:
  - 4 Mud Shot
- Segment #83:
  - 97 Mud Shot
  - 1 Max Quake (14atk)
  - 1 Max Quake (15atk)
- Segment #84:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #85:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segments #86 & #87:
  - 92 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #88:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #89:
  - 92 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #90:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #91:
  - 1 Max Quake (15atk)
- Segment #92:
  - 70 Mud Shot
  - 1 Max Quake (14atk)
  - 1 Max Quake (15atk)
- Segments #93 & #94:
  - 1 Max Quake (14atk)
  - 4 Max Quake (15atk) # Duplicte 1 on the last turn
- Segment #95:
  - 82 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #96:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segments #97 & #98:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #99:
  - 70 Mud Shot
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)
- Segment #100:
  - 1 Max Quake (14atk)
  - 2 Max Quake (15atk)

```py
from src.max_utils import seg
dmg = (5, 375, 377)
print(seg(dmg, (103, 1, 5), 1000))
print(seg(dmg, (103, 2, 8), 1000))
print(seg(dmg, (103, 3, 9), 1000))
print(seg(dmg, (195, 4, 12), 1000))
print(seg(dmg, (195, 5, 15), 1000))
print(seg(dmg, (195, 6, 18), 1000))
print(seg(dmg, (296, 7, 21), 1000))
print(seg(dmg, (296, 8, 24), 1000))
print(seg(dmg, (296, 9, 27), 1000))
print(seg(dmg, (387, 10, 30), 1000))
print(seg(dmg, (387, 11, 33), 1000))
print(seg(dmg, (387, 12, 36), 1000))
print(seg(dmg, (488, 13, 39), 1000))
print(seg(dmg, (488, 14, 42), 1000))
print(seg(dmg, (488, 15, 45), 1000))
print(seg(dmg, (588, 16, 48), 1000))
print(seg(dmg, (588, 17, 51), 1000))
print(seg(dmg, (588, 18, 54), 1000))
print(seg(dmg, (681, 19, 57), 1000))
print(seg(dmg, (681, 20, 60), 1000))
print(seg(dmg, (681, 21, 65), 1000))
print(seg(dmg, (725, 21, 65), 1000))
print(seg(dmg, (772, 22, 68), 1000))
print(seg(dmg, (772, 23, 71), 1000))
print(seg(dmg, (772, 24, 74), 1000))
print(seg(dmg, (824, 24, 74), 1000))
print(seg(dmg, (874, 25, 77), 1000))
print(seg(dmg, (874, 26, 80), 1000))
print(seg(dmg, (874, 27, 83), 1000))
print(seg(dmg, (922, 27, 83), 1000))
print(seg(dmg, (967, 28, 86), 1000))
print(seg(dmg, (967, 29, 89), 1000))
print(seg(dmg, (967, 30, 92), 1000))
print(seg(dmg, (1018, 30, 92), 1000))
print(seg(dmg, (1163, 30, 94), 1000))
print(seg(dmg, (1163, 30, 97), 1000))
print(seg(dmg, (1163, 30, 100), 1000))
print(seg(dmg, (1214, 30, 100), 1000))
print(seg(dmg, (1265, 31, 103), 1000))
print(seg(dmg, (1265, 32, 103), 1000))
print(seg(dmg, (1357, 33, 104), 1000))
print(seg(dmg, (1357, 34, 106), 1000))
print(seg(dmg, (1357, 34, 108), 1000))
print(seg(dmg, (1459, 35, 110), 1000))
print(seg(dmg, (1459, 36, 112), 1000))
print(seg(dmg, (1459, 37, 114), 1000))
print(seg(dmg, (1551, 38, 115), 1000))
print(seg(dmg, (1551, 39, 117), 1000))
print(seg(dmg, (1551, 40, 119), 1000))
print(seg(dmg, (1631, 40, 119), 1000))
print(seg(dmg, (1654, 41, 121), 1000))
print(seg(dmg, (1654, 42, 123), 1000))
print(seg(dmg, (1654, 43, 125), 1000))
print(seg(dmg, (1747, 43, 126), 1000))
print(seg(dmg, (1747, 44, 127), 1000))
print(seg(dmg, (1747, 45, 129), 1000))
print(seg(dmg, (1848, 45, 132), 1000))
print(seg(dmg, (1848, 45, 135), 1000))
print(seg(dmg, (1848, 45, 138), 1000))
print(seg(dmg, (1941, 46, 140), 1000))
print(seg(dmg, (1941, 47, 142), 1000))
print(seg(dmg, (1941, 48, 144), 1000))
print(seg(dmg, (1945, 48, 144), 1000))
print(seg(dmg, (2042, 49, 145), 1000))
print(seg(dmg, (2042, 50, 147), 1000))
print(seg(dmg, (2042, 51, 149), 1000))
print(seg(dmg, (2134, 52, 151), 1000))
print(seg(dmg, (2134, 53, 153), 1000))
print(seg(dmg, (2226, 54, 155), 1000))
print(seg(dmg, (2226, 55, 157), 1000))
print(seg(dmg, (2226, 55, 158), 1000))
print(seg(dmg, (2296, 56, 159), 1000))
print(seg(dmg, (2296, 57, 163), 1000))
print(seg(dmg, (2378, 58, 165), 1000))
print(seg(dmg, (2378, 59, 167), 1000))
print(seg(dmg, (2378, 60, 169), 1000))
print(seg(dmg, (2448, 61, 171), 1000))
print(seg(dmg, (2448, 62, 173), 1000))
```

```
Seg: 2 | Extra: 775 dmg | Total: 2775 dmg
Seg: 4 | Extra: 281 dmg | Total: 4281 dmg
Seg: 5 | Extra: 33 dmg | Total: 5033 dmg
Seg: 6 | Extra: 999 dmg | Total: 6999 dmg
Seg: 8 | Extra: 505 dmg | Total: 8505 dmg
Seg: 10 | Extra: 11 dmg | Total: 10011 dmg
Seg: 12 | Extra: 22 dmg | Total: 12022 dmg
Seg: 13 | Extra: 528 dmg | Total: 13528 dmg
Seg: 15 | Extra: 34 dmg | Total: 15034 dmg
Seg: 16 | Extra: 995 dmg | Total: 16995 dmg
Seg: 18 | Extra: 501 dmg | Total: 18501 dmg
Seg: 20 | Extra: 7 dmg | Total: 20007 dmg
Seg: 22 | Extra: 18 dmg | Total: 22018 dmg
Seg: 23 | Extra: 524 dmg | Total: 23524 dmg
Seg: 25 | Extra: 30 dmg | Total: 25030 dmg
Seg: 27 | Extra: 36 dmg | Total: 27036 dmg
Seg: 28 | Extra: 542 dmg | Total: 28542 dmg
Seg: 30 | Extra: 48 dmg | Total: 30048 dmg
Seg: 32 | Extra: 19 dmg | Total: 32019 dmg
Seg: 33 | Extra: 525 dmg | Total: 33525 dmg
Seg: 35 | Extra: 785 dmg | Total: 35785 dmg
Seg: 36 | Extra: 5 dmg | Total: 36005 dmg
Seg: 37 | Extra: 746 dmg | Total: 37746 dmg
Seg: 39 | Extra: 252 dmg | Total: 39252 dmg
Seg: 40 | Extra: 758 dmg | Total: 40758 dmg
Seg: 41 | Extra: 18 dmg | Total: 41018 dmg
Seg: 42 | Extra: 774 dmg | Total: 42774 dmg
Seg: 44 | Extra: 280 dmg | Total: 44280 dmg
Seg: 45 | Extra: 786 dmg | Total: 45786 dmg
Seg: 46 | Extra: 26 dmg | Total: 46026 dmg
Seg: 47 | Extra: 757 dmg | Total: 47757 dmg
Seg: 49 | Extra: 263 dmg | Total: 49263 dmg
Seg: 50 | Extra: 769 dmg | Total: 50769 dmg
Seg: 51 | Extra: 24 dmg | Total: 51024 dmg
Seg: 52 | Extra: 503 dmg | Total: 52503 dmg
Seg: 53 | Extra: 634 dmg | Total: 53634 dmg
Seg: 54 | Extra: 765 dmg | Total: 54765 dmg
Seg: 55 | Extra: 20 dmg | Total: 55020 dmg
Seg: 56 | Extra: 781 dmg | Total: 56781 dmg
Seg: 57 | Extra: 156 dmg | Total: 57156 dmg
Seg: 58 | Extra: 368 dmg | Total: 58368 dmg
Seg: 59 | Extra: 497 dmg | Total: 59497 dmg
Seg: 60 | Extra: 251 dmg | Total: 60251 dmg
Seg: 61 | Extra: 890 dmg | Total: 61890 dmg
Seg: 63 | Extra: 19 dmg | Total: 63019 dmg
Seg: 64 | Extra: 148 dmg | Total: 64148 dmg
Seg: 65 | Extra: 360 dmg | Total: 65360 dmg
Seg: 66 | Extra: 489 dmg | Total: 66489 dmg
Seg: 67 | Extra: 618 dmg | Total: 67618 dmg
Seg: 68 | Extra: 18 dmg | Total: 68018 dmg
Seg: 69 | Extra: 262 dmg | Total: 69262 dmg
Seg: 70 | Extra: 391 dmg | Total: 70391 dmg
Seg: 71 | Extra: 520 dmg | Total: 71520 dmg
Seg: 72 | Extra: 362 dmg | Total: 72362 dmg
Seg: 73 | Extra: 114 dmg | Total: 73114 dmg
Seg: 74 | Extra: 243 dmg | Total: 74243 dmg
Seg: 75 | Extra: 879 dmg | Total: 75879 dmg
Seg: 77 | Extra: 10 dmg | Total: 77010 dmg
Seg: 78 | Extra: 141 dmg | Total: 78141 dmg
Seg: 79 | Extra: 735 dmg | Total: 79735 dmg
Seg: 80 | Extra: 864 dmg | Total: 80864 dmg
Seg: 81 | Extra: 993 dmg | Total: 81993 dmg
Seg: 82 | Extra: 13 dmg | Total: 82013 dmg
Seg: 83 | Extra: 250 dmg | Total: 83250 dmg
Seg: 84 | Extra: 379 dmg | Total: 84379 dmg
Seg: 85 | Extra: 508 dmg | Total: 85508 dmg
Seg: 87 | Extra: 97 dmg | Total: 87097 dmg
Seg: 88 | Extra: 226 dmg | Total: 88226 dmg
Seg: 89 | Extra: 815 dmg | Total: 89815 dmg
Seg: 90 | Extra: 944 dmg | Total: 90944 dmg
Seg: 91 | Extra: 321 dmg | Total: 91321 dmg
Seg: 92 | Extra: 423 dmg | Total: 92423 dmg
Seg: 94 | Extra: 306 dmg | Total: 94306 dmg
Seg: 95 | Extra: 845 dmg | Total: 95845 dmg
Seg: 96 | Extra: 974 dmg | Total: 96974 dmg
Seg: 98 | Extra: 103 dmg | Total: 98103 dmg
Seg: 99 | Extra: 582 dmg | Total: 99582 dmg
Seg: 100 | Extra: 711 dmg | Total: 100711 dmg
```

All the segments flip at the expected moment ✔️
