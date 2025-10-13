# Max-Battle-Tests

Tests and stats for Max Battles bosses in Pokémon GO.

## Structure

The repository is structured in the following way:
- [Tests Docs](./tests/): Documentation for all the tests done by the team, including data, analysis and results.
- [Testing Code](./src/): Python scripts and utilities for executing and analysing tests.
- [Resources](./res/): Graphical documentation of most of the tests data, specially Attack CPM tests.

## Introduction


## Max Battles Boss Stats Explanation

Before going in detail about the testing methods, first a quick summary of the stats of the bosses. As we currently understand the max battle system, bosses have 4 main stats (besides the Pokémon species stats) which greatly influence their difficulty:
- **Combat Power Multiplier** (*CPM*): Known as the level of a Pokémon.
- **Health Points** (*HP*): The health value of the boss.
- **Attack Multiplier** (*AtkMult*): Modifier to further increase/decrease the boss output damage.
- **Defense Multiplier** (*DefMult*): Modifier to further increase/decrease the boss incoming damage.

However, when testing we wont directly obtain the values for those stats, instead we obtain the values for:
- **Attack CPM** (*AtkCPM*): Constant is equal to `AtkCPM = CPM * AtkMult`.
- **Defense CPM** (*DefCPM*): Constant is equal to `DefCPM = CPM * DefMult`.
- **HP value**: This one is obtained directly.

This leads to a massive problem, we only obtain 2 values for the 3 stats of *CPM*, *AtkMult* and *DefMult*, building a 3 variable and 2 equation system which has infinite solutions. Luckily for us, humans and PoGO players, its easy to find which solution is most likely the real one: It should have *pretty* numbers and a CPM value between `0.0` and `1.0`. This has lead to the identification of multiple **boss stats models**, which are helpful to determine the real stats of new bosses when they get released or updated.

These are some of the most common models:
- For T1 to T4 bosses: `AtkMult = 1.0` and `DefMult = 1.0`.
- For T5 bosses: `AtkMult = 2.0`, `DefMult = 1.0` and `CPM` multiple of `0.05`.
- For T6 bosses: `AtkMult = 0.9`, `DefMult = 1.0` and `CPM` multiple of `0.05`.

> Even though recently all bosses dont have a Defense Multiplier value, some old tests report that it was very likely that the bosses used to have one.

## Max Battles Boss Stats Values

### Dynamax Low Tier Bosses

These are very simple as none of them have Attack or Defense Multipliers, in other words, their Attack CPM and Defense CPM are equal, and the CPM and HP remains the same for all bosses on the same tier:

| Tier | CPM  | HP    |
|:-----|:----:|:-----:|
| T1   | 0.15 | 1700  |
| T2   | 0.38 | 5000  |
| T3   | 0.5  | 10000 |
| T4   | 0.6  | 20000 |

> My impression is that T1 HP value should have been `1666` (from `1/3 * 5000`) but got rounded to `1700`, the closest multiple of 100, which means we can expect all max bosses to have an HP value multiple of 100. Same with T2 CPM value which should have been `0.375` (from `5/2 * 0.15`, or `3/4 * 0.5`) but got rounded to `0.38`, the closes 2 decimal number, which means we can expect all bosses to have a 2 decimal CPM value at most.

### Dynamax Legendary T5 Bosses

As for now they all have an Attack Multiplier of `2.0` and no Defense Multiplier, but each boss has its own CPM and HP, to properly adjust their difficulty:

| Pokemons   | CPM  | AtkMult | HP    |
|:-----------|:----:|:-------:|:-----:|
| Articuno   | 0.7  | 2.0     | 17500 |
| Zapdos     | 0.7  | 2.0     | 13000 |
| Moltres    | 0.7  | 2.0     | 20000 |
| Raikou (1) | 0.8  | 2.0     | 20000 |
| Raikou (2) | 0.8  | 2.0     | 25000 |
| Entei      | 0.75 | 2.0     | 27000 |
| Suicune    | 0.9  | 2.0     | 22000 |
| Latias     | 0.7  | 2.0     | 25000 |
| Latios     | 0.75 | 2.0     | 23000 |

### Gigantamax and Eternamax T6 Bosses

Like Dynamax Legendary bosses, each Gigantamax boss had its own CPM and HP. Initially they didnt have an Attack Multiplier, but it was reduced a 10%, to `0.9`, after the first general nerf. However during certain events it gets modified and even receive a Defense Multiplier.

| Pokemons       | CPM  | AtkMult | DefMult | HP     |
|:---------------|:----:|:-------:|:-------:|:------:|
| Venusaur (1)   | 0.85 | 1.0     | 1.0     |  90000 |
| Venusaur (2)   | 0.85 | 0.9     | 1.0     |  90000 |
| Charizard (1)  | 0.85 | 1.0     | 1.0     |    N/A |
| Charizard (2)  | 0.85 | 0.9     | 1.0     |    N/A |
| Blastoise (1)  | 0.85 | 1.0     | 1.0     |  75000 |
| Blastoise (2)  | 0.85 | 0.9     | 1.0     |  75000 |
| Butterfree     | 0.85 | 0.9     | 1.0     | 100000 |
| Machamp        | 0.8  | 0.9     | 1.0     | 100000 |
| Gengar         | 0.85 | 0.9     | 1.0     |  80000 |
| Kingler        | 0.85 | 0.9     | 1.0     | 100000 |
| Lapras (1)     | 0.85 | 0.9     | 1.0     |  80000 |
| Lapras (2)     | 0.45 | 0.75    | 1.0     | 100000 |
| Snorlax (1)    | 0.85 | 0.9     | 1.0     | 100000 |
| Snorlax (2)    | 0.65 | 0.9     | 1.0     |    N/A |
| Rillaboom      | 1.0  | 0.9     | 1.0     | 120000 |
| Cinderace      | 0.8  | 0.9     | 1.0     |  80000 |
| Inteleon       | 0.9  | 0.9     | 1.0     | 100000 |
| Toxtricity (1) | 0.9  | 1.15    | 1.45    | 100000 |
| Toxtricity (2) | 0.9  | 0.9     | 1.0     |    N/A |
| Eternatus      | 0.75 | 0.9     | 1.0     |  60000 |

## Collaborators:

Active testers, researchers and analyzers on out team:

- [CreatorBeastGD](https://reddit.com/user/CreatorBeastGD/) (creator of [PokéChespin](https://pokechespin.net/))
- [0ShadowNo1](https://reddit.com/user/Key-Bag-4059/)
- [Pogo Raids Gameplay](https://youtube.com/@pogoraidsgameplay2527)
- [xRage](https://youtube.com/@xRage7243)
- [TheJayLife](https://youtube.com/@TheJayLife)
- [Flyfunner](https://reddit.com/user/Flyfunner/)
- People from the [Pokebattler](https://pokebattler.com/) Research Team

Some tests data has been obtained from public YouTube videos. The owners of those videos are not involved in our research; their videos are public, so we can freely use them for testing. Some are random videos, but others coms from notable short-man raiders like:

- [FrealafGB](https://youtube.com/@frealafgb)
- [J0P4K0](https://youtube.com/@J0PAK0)
- [Raphaël D](https://youtube.com/@raphaeld4313)
- [Obelisk1500](https://youtube.com/@Obelisk-qe5df)
- [Santymess](https://youtube.com/@santymess8250)


