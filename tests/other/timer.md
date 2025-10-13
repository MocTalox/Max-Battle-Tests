# Max Battle Timers

Max Battles have two main stages: The Phase One in which the battles carries on normaly, and Phase Two in which the boss gets **enraged** and increases its power and starts to deal a massive amount of damage, in which the team will struggle to survive and in high tier battles they wont last for too long. This is considered a *soft-end*, but this Phase Two has a real ending, the *hard-end*, in which the **battle finish** definitively.

There is a hidden timer on Max Battles and it defines the start and end of each Phase during the battle, as well as a warning 30 seconds before the start of Phase Two indicating the boss is getting **desperate**. Therefore we have 3 events during a Max Battle:
- **Desperate**: A message in the log saying *"Boss is getting desperate!"*.
- **Enrage**: A message in the log saying *"Boss's attacks are getting stronger!"*.
- **Timeout**: The battle directly ends.

> 📝 Note: The **Enrage** event happens exactly 30s after **Desperate** event, but the log message is not displayed after the boss prepares the following attack (the increased damage does not apply to the previous attack). Because of the randomness of a battle flow, the start of a Phase Two is not an exact time, it can get delayed a few seconds.

However, when going through a Max Phase this hidden timer stops, slows down or gets delayed (still not fully understood) making the events of a Max Battle take more irl time to happen, slowing down the overall length of the battle, specially important for making Phase One last longer.

## Summary

Tier             | Desperate   | Enrage      | Timeout
:--------------- | :---------: | :---------: | :---------:
T1 to T4 Dynamax | 270s (4:30) | 300s (5:00) | 480s (8:00)
T5 Dynamax       | N/A         | N/A         | N/A
T5 Eternamax     | N/A         | N/A         | N/A
T6 Gigantamax    | 180s (3:00) | 210s (3:30) | N/A

## Timer tests

**Beldum (T3)**

- *Desperate*: 4:30
- *Enrage*: After 5:00
- *MP start*: Unknown
- *MP end*: 29s later
- *Timeout*: 8:23

**Lapras (T6)**

- *Desperate*: 3:00
- *Enrage*: After 3:30
